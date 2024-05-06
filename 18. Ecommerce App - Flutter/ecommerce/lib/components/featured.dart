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
  final List<FeaturedProduct> featuredProducts; // List of featured products

  const FeaturedSection({Key? key, required this.featuredProducts})
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
                        builder: (context) => FeaturedScreen(),
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
            itemCount: featuredProducts.length,
            itemBuilder: (context, index) {
              final product = featuredProducts[index];
              return FeaturedProductItem(
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
                  style: TextStyle(
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
