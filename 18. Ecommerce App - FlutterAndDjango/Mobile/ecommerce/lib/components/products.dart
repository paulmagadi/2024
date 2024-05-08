import 'package:flutter/material.dart';
import '../screens/products.dart';

// Define a class to represent each featured product
class AllProduct {
  final String imageUrl;
  final String title;
  final double price;

  AllProduct({
    required this.imageUrl,
    required this.title,
    required this.price,
  });
}

class ProductsSection extends StatelessWidget {
  final List<AllProduct> allProducts; // List of featured products

  const ProductsSection({Key? key, required this.allProducts})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Section title row with title and "See More" button
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // Section title
                Text(
                  'Products',
                  style: Theme.of(context).textTheme.titleLarge,
                ),

                // "See More" button
                TextButton(
                  onPressed: () {
                    // Navigate to the FeaturedScreen
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => ProductsScreen(),
                      ),
                    );
                  },
                  child: const Text('See More'),
                ),
              ],
            ),
          ),

          // Grid view of featured products
          GridView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 3, // Number of columns
              childAspectRatio: 3 / 4, // Aspect ratio of each grid item
              mainAxisSpacing: 2.0,
              crossAxisSpacing: 2.0,
            ),
            itemCount: allProducts.length,
            itemBuilder: (context, index) {
              final product = allProducts[index];
              return AllProductItem(
                product: product,
              );
            },
          ),
        ],
      ),
    );
  }
}

// Define a custom widget for each featured product item
class AllProductItem extends StatelessWidget {
  final AllProduct product;

  const AllProductItem({Key? key, required this.product}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 2.0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(8.0),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Product image
          Expanded(
            child: Image.asset(
              product.imageUrl,
              fit: BoxFit.cover,
            ),
          ),

          // Product details
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Product title
                Text(
                  product.title,
                  style: Theme.of(context).textTheme.titleMedium,
                ),

                // Product price
                Text(
                  '\$${product.price.toStringAsFixed(2)}',
                  style: const TextStyle(
                    color: Colors.green,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
