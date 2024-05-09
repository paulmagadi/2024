import 'package:flutter/material.dart';
import '../screens/deals.dart';

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

class DealsSection extends StatelessWidget {
  final List<Deal> deals;

  const DealsSection({Key? key, required this.deals}) : super(key: key);

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

                // "See More" button with arrow icon
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
                return DealItem(deal: deal);
              },
            ),
          ),
        ],
      ),
    );
  }
}

// Custom widget to represent each deal item
class DealItem extends StatelessWidget {
  final Deal deal;

  const DealItem({Key? key, required this.deal}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
          horizontal: 4.0), // Adjust padding as needed
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
              borderRadius:
                  const BorderRadius.vertical(top: Radius.circular(8.0)),
              child: Image.network(
                deal.imageUrl,
                height: 100.0, // Adjust height as needed
                width: 100.0, // Adjust width as needed
                fit: BoxFit.contain, // Changed to BoxFit.cover
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
                    deal.title,
                    style: Theme.of(context).textTheme.titleMedium,
                  ),

                  const SizedBox(
                      height: 4.0), // Add spacing between title and prices

                  // Deal prices
                  Row(
                    children: [
                      // Old price
                      Text(
                        '\$${deal.oldPrice.toStringAsFixed(2)}',
                        style: const TextStyle(
                          color: Colors.grey,
                          decoration: TextDecoration.lineThrough,
                        ),
                      ),

                      const SizedBox(width: 8.0),

                      // New price
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
    );
  }
}