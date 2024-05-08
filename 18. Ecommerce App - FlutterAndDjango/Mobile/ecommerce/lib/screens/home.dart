import 'package:flutter/material.dart';
import '../models/product_data.dart';
import '../models/product_model.dart';

import '../components/category_menu.dart';
import '../components/banner.dart';
import '../components/banner_carousel.dart';

import '../components/deals.dart';
import '../components/featured.dart';
import '../components/products.dart';

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

          AllProduct convertProductToAllProduct(Product product) {
            return AllProduct(
              imageUrl: product.image,
              title: product.name,
              price: product.price,
            );
          }

          Deal convertProductToDeal(Product product) {
            return Deal(
              imageUrl: product.image,
              title: product.name,
              oldPrice: product.price, // Use the product's price as old price
              newPrice:
                  product.salePrice, // Use sale price or price as new price
            );
          }

          FeaturedProduct convertProductToFeaturedProduct(Product product) {
            return FeaturedProduct(
              imageUrl: product.image,
              title: product.name,
              price: product.price,
            );
          }

          // Filter products for different sections based on conditions
          final featuredProducts =
              products.where((product) => product.isFeatured).toList();
          final dealsProducts =
              products.where((product) => product.isSale).toList();

          List<Deal> deals = dealsProducts.map(convertProductToDeal).toList();
          List<FeaturedProduct> featured =
              featuredProducts.map(convertProductToFeaturedProduct).toList();
          List<AllProduct> allProducts =
              products.map(convertProductToAllProduct).toList();

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
                child: DealsSection(
                  deals: deals,
                ),
              ),

              // FeaturedSection component
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8.0),
                child: FeaturedSection(
                  featuredProducts: featured,
                ),
              ),

              // All Products section
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8.0),
                child: ProductsSection(
                  allProducts: allProducts,
                ),
              ),

              // Add other sections as needed...
            ],
          );
        },
      ),
    );
  }
}
