import 'package:flutter/material.dart';
import '../screens/featured.dart';

// Define a class to represent each featured product
class FeaturedProduct {
  final String imageUrl;
  final String title;
  final double price;

  FeaturedProduct({
    required this.imageUrl,
    required this.title,
    required this.price,
  });
}

class FeaturedSection extends StatelessWidget {
  final List<FeaturedProduct> featuredProducts;

  const FeaturedSection({Key? key, required this.featuredProducts})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Section title row
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // Section title
                Text(
                  'Featured Products',
                  style: Theme.of(context).textTheme.titleLarge,
                ),

                // "See More" button
                TextButton(
                  onPressed: () {
                    // Navigate to the FeaturedScreen
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const FeaturedScreen(),
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
              crossAxisCount:
                  2, // Adjust number of columns for different screen sizes
              childAspectRatio: 2 / 3, // Adjust aspect ratio for better layout
              mainAxisSpacing: 8.0,
              crossAxisSpacing: 8.0,
            ),
            itemCount: featuredProducts.length,
            itemBuilder: (context, index) {
              final product = featuredProducts[index];
              return FeaturedProductItem(product: product);
            },
          ),
        ],
      ),
    );
  }
}

// Define a custom widget for each featured product item
class FeaturedProductItem extends StatelessWidget {
  final FeaturedProduct product;

  const FeaturedProductItem({Key? key, required this.product})
      : super(key: key);

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
            child: Image.network(
              product
                  .imageUrl, // Use Image.network if the images are hosted remotely
              fit: BoxFit.cover,
              errorBuilder: (context, error, stackTrace) {
                // Error handling for failed image loading
                return const Icon(Icons.error, color: Colors.red);
              },
              loadingBuilder: (context, child, loadingProgress) {
                if (loadingProgress == null) {
                  return child;
                } else {
                  // Display a CircularProgressIndicator while the image is loading
                  return const Center(child: CircularProgressIndicator());
                }
              },
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
