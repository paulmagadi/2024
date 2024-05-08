// import 'package:flutter/material.dart';
// import '../components/category_menu.dart';
// import '../components/banner.dart';
// import '../components/banner_carousel.dart';
// import '../components/deals.dart';
// import '../components/featured.dart';
// import '../components/products.dart';
// import 'package:http/http.dart' as http;

// class HomeScreen extends StatelessWidget {
//   const HomeScreen({Key? key}) : super(key: key);

//   @override
//   Widget build(BuildContext context) {
//     return SingleChildScrollView(
//       child: Column(
//         crossAxisAlignment: CrossAxisAlignment.start,
//         children: [
//           // Horizontal menu for categories
//           const Padding(
//             padding: EdgeInsets.symmetric(vertical: 8.0),
//             child: CategoryMenu(),
//           ),

//           // Banner section
//           const Padding(
//             padding: EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
//             child: BannerSection(),
//           ),

//           // BannerCarousel component
//           const BannerCarousel(),

//           //DealsSection component
//           Padding(
//             padding: const EdgeInsets.symmetric(vertical: 8.0),
//             child: DealsSection(

//               deals: [

//                 Deal(
//                   imageUrl: 'assets/images/products/1.jpg',
//                   title: 'Deal 1',
//                   oldPrice: 19.99,
//                   newPrice: 14.99,
//                 ),
//                 // Deal(
//                 //   imageUrl: 'assets/images/products/2.jpg',
//                 //   title: 'Deal 2',
//                 //   oldPrice: 49.99,
//                 //   newPrice: 39.99,
//                 // ),
//                 Deal(
//                   imageUrl: 'assets/images/products/3.jpg',
//                   title: 'Deal 3',
//                   oldPrice: 22.99,
//                   newPrice: 22.99,
//                 ),
//                 Deal(
//                   imageUrl: 'assets/images/products/4.jpg',
//                   title: 'Deal 4',
//                   oldPrice: 29.99,
//                   newPrice: 24.99,
//                 ),
//                 Deal(
//                   imageUrl: 'assets/images/products/5.jpg',
//                   title: 'Deal 5',
//                   oldPrice: 59.99,
//                   newPrice: 33.99,
//                 ),
//               ],
//             ),
//           ),

//           // FeaturedSection component
//           Padding(
//             padding: const EdgeInsets.symmetric(vertical: 8.0),
//             child: FeaturedSection(
//               featuredProducts: [
//                 FeaturedProduct(
//                   imageUrl: 'assets/images/products/1.jpg',
//                   title: 'Product 1',
//                   price: 39.99,
//                 ),
//                 FeaturedProduct(
//                   imageUrl: 'assets/images/products/2.jpg',
//                   title: 'Product 2',
//                   price: 29.99,
//                 ),
//                 FeaturedProduct(
//                   imageUrl: 'assets/images/products/3.jpg',
//                   title: 'Product 3',
//                   price: 29.99,
//                 ),
//                 FeaturedProduct(
//                   imageUrl: 'assets/images/products/4.jpg',
//                   title: 'Product 4',
//                   price: 29.99,
//                 ),
//                 FeaturedProduct(
//                   imageUrl: 'assets/images/products/5.jpg',
//                   title: 'Product 5',
//                   price: 29.99,
//                 ),
//                 FeaturedProduct(
//                   imageUrl: 'assets/images/products/6.jpg',
//                   title: 'Product 6',
//                   price: 29.99,
//                 ),
//                 // Add more FeaturedProduct objects as needed...
//               ],
//             ),
//           ),

//           // All Products
//           Padding(
//             padding: const EdgeInsets.symmetric(vertical: 8.0),
//             child: ProductsSection(
//               allProducts: [
//                 AllProduct(
//                   imageUrl: 'assets/images/products/1.jpg',
//                   title: 'Product 1',
//                   price: 39.99,
//                 ),
//                 AllProduct(
//                   imageUrl: 'assets/images/products/2.jpg',
//                   title: 'Product 2',
//                   price: 29.99,
//                 ),
//                 AllProduct(
//                   imageUrl: 'assets/images/products/3.jpg',
//                   title: 'Product 3',
//                   price: 29.99,
//                 ),
//                 AllProduct(
//                   imageUrl: 'assets/images/products/4.jpg',
//                   title: 'Product 4',
//                   price: 29.99,
//                 ),
//                 AllProduct(
//                   imageUrl: 'assets/images/products/5.jpg',
//                   title: 'Product 5',
//                   price: 29.99,
//                 ),
//                 AllProduct(
//                   imageUrl: 'assets/images/products/6.jpg',
//                   title: 'Product 6',
//                   price: 29.99,
//                 ),
//                 // Add more Product objects as needed...
//               ],
//             ),
//           ),
//           // Add other sections such as featured products, promotions, etc.
//         ],
//       ),
//     );
//   }
// }

import 'package:flutter/material.dart';
import '../models/data.dart'; // Import the data functions and model classes
import '../screens/product_details.dart'; // Import the product details screen

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // appBar: AppBar(
      //   title: const Text('Home'),
      // ),
      body: FutureBuilder<List<Product>>(
        future: fetchProducts(), // Fetch data from the backend
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            // Show a loading indicator while waiting for data
            return const Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            // Show an error message if data fetching fails
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            final products = snapshot.data!;

            // Display the list of products
            return ListView.builder(
              itemCount: products.length,
              itemBuilder: (context, index) {
                final product = products[index];
                return ListTile(
                  title: Text(product.name),
                  subtitle: Text('\$${product.price.toStringAsFixed(2)}'),
                  onTap: () {
                    // Navigate to ProductDetailsScreen when a product is tapped
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) =>
                            ProductDetailsScreen(product: product),
                      ),
                    );
                  },
                );
              },
            );
          }
        },
      ),
    );
  }
}
