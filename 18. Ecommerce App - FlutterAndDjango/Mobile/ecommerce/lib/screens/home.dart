import 'package:flutter/material.dart';
import '../models/product_data.dart';
import '../models/product_model.dart';
import '../models/model_converters.dart';

import '../components/category_menu.dart';
import '../components/banner.dart';
import '../components/banner_carousel.dart';

import '../components/deals.dart';
// import '../components/featured.dart';
import '../components/products.dart';
// import '../components/new_arrivals.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: FutureBuilder<List<Product>>(
        future: fetchProducts(), // Fetch products from backend
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            // Display loading spinner while waiting for data
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            // Display error message if fetching data fails
            return Center(child: Text('${snapshot.error}'));
          }

          // If data is successfully fetched, display the home page UI
          final products = snapshot.data!;

          // Filter products for different sections based on conditions
          // final featuredProducts =
          //     products.where((product) => product.isFeatured).toList();
          final dealsProducts =
              products.where((product) => product.isSale).toList();
          // final newProducts =
          //     products.where((product) => product.isNew).toList();

          List<Deal> deals = dealsProducts.map(convertProductToDeal).toList();
          // List<FeaturedProduct> featured =
          //     featuredProducts.map(convertProductToFeaturedProduct).toList();
          List<AllProduct> allProducts =
              products.map(convertProductToAllProduct).toList();
          // List<NewItem> newProductsList =
          //     newProducts.map(convertProductToNewProduct).toList();

          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Horizontal menu for categories
              const Padding(
                padding: EdgeInsets.symmetric(vertical: 8.0),
                child: CategoryMenu(),
              ),

              // Banner section
              const Padding(
                padding: EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
                child: BannerSection(),
              ),

              // BannerCarousel component
              const BannerCarousel(),

              // DealsSection component
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8.0),
                child: DealsSection(deals: deals),
              ),

              // FeaturedSection component
              // Padding(
              //   padding: const EdgeInsets.symmetric(vertical: 8.0),
              //   child: FeaturedSection(featuredProducts: featured),
              // ),

              // // New Arrivals section
              // Padding(
              //   padding: const EdgeInsets.symmetric(vertical: 8.0),
              //   child: NewArrivalsSection(newItems: newProductsList),
              // ),

              // All Products section
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8.0),
                child: ProductsSection(allProducts: allProducts),
              ),
            ],
          );
        },
      ),
    );
  }
}
