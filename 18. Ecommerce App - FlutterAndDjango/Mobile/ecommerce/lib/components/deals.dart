import 'package:flutter/material.dart';
import '../screens/deals.dart';
import '../screens/product_details.dart';
import '../models/product_model.dart';

// Define a class to represent each deal
class Deal {
  final String imageUrl;
  final String title;
  final double oldPrice;
  final double newPrice;

  Deal({
    required this.imageUrl,
    required this.title,
    required this.oldPrice,
    required this.newPrice,
  });
}

const int maxNameLength = 20;

class DealsSection extends StatelessWidget {
  final List<Deal> deals;
  final List<Product> products; // Add a list of Product objects

  const DealsSection({Key? key, required this.deals, required this.products})
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
                  'Deals',
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                // "See More" button and icon
                Row(
                  children: [
                    TextButton(
                      onPressed: () {
                        // Navigate to the DealsScreen
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const DealsScreen(),
                          ),
                        );
                      },
                      child: const Text('See More'),
                    ),
                    const Icon(
                      Icons.keyboard_double_arrow_right,
                      size: 16.0,
                      color: Colors.grey,
                    ),
                  ],
                ),
              ],
            ),
          ),
          // Horizontally scrolling list of deals
          SizedBox(
            height: 180, // Adjust height as needed
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: deals.length,
              itemBuilder: (context, index) {
                final deal = deals[index];
                // Find the associated Product object using the deal title or other identifying properties
                final product = products.firstWhere(
                  (product) => product.name == deal.title,
                  orElse: () => throw Exception('No matching Product found'),

                  // Handle the case when no matching product is found
                );

                // Only pass the product if it was found
                // ignore: unnecessary_null_comparison
                if (product != null) {
                  return DealItem(deal: deal, product: product);
                }
                // Otherwise, return an empty container or some other placeholder
                return Container();
              },
            ),
          ),
        ],
      ),
    );
  }
}

class DealItem extends StatelessWidget {
  final Deal deal;
  final Product product;

  const DealItem({Key? key, required this.deal, required this.product})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Truncate product name if it exceeds the maximum length
    String truncatedName = product.name.length > maxNameLength
        ? '${product.name.substring(0, maxNameLength)}...'
        : product.name;
    return GestureDetector(
      onTap: () {
        // Navigate to the ProductDetailsScreen when the deal item is clicked
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ProductDetailsScreen(product: product),
          ),
        );
      },
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 4.0),
        child: Card(
          elevation: 2.0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8.0),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Deal image
              ClipRRect(
                borderRadius: BorderRadius.vertical(top: Radius.circular(8.0)),
                child: Image.network(
                  deal.imageUrl,
                  height: 100.0,
                  width: 100,
                  fit: BoxFit.contain,
                  semanticLabel:
                      deal.title, // Add semantic label for accessibility
                ),
              ),

              // Deal details
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Deal title
                    Text(
                      truncatedName,
                      style: Theme.of(context).textTheme.titleSmall,
                    ),
                    const SizedBox(height: 4.0),
                    // Deal prices
                    Row(
                      children: [
                        // Old price (struck through)
                        Text(
                          '\$${deal.oldPrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.grey,
                            decoration: TextDecoration.lineThrough,
                          ),
                        ),
                        const SizedBox(width: 8.0),
                        // New price (highlighted)
                        Text(
                          '\$${deal.newPrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.red,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
