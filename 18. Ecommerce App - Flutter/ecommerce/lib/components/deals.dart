import 'package:flutter/material.dart';

class DealsSection extends StatelessWidget {
  final List<Deal> deals;  // Define a list of deals

  const DealsSection({Key? key, required this.deals}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Section title
          Text(
            'Deals',
            style: Theme.of(context).textTheme.headline6,  // Use your app's theme
          ),
          
          // Display deals in a grid view
          GridView.builder(
            shrinkWrap: true,
            physics: NeverScrollableScrollPhysics(),  // To prevent scrolling within the grid
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,  // Number of columns
              childAspectRatio: 3 / 4,  // Aspect ratio of each grid item
              mainAxisSpacing: 8.0,  // Spacing between rows
              crossAxisSpacing: 8.0,  // Spacing between columns
            ),
            itemCount: deals.length,  // Number of deals
            itemBuilder: (context, index) {
              final deal = deals[index];
              return DealItem(
                deal: deal,
              );
            },
          ),
        ],
      ),
    );
  }
}

// Define a Deal class to represent each deal
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

// Define a custom widget for each deal item
class DealItem extends StatelessWidget {
  final Deal deal;

  const DealItem({Key? key, required this.deal}) : super(key: key);

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
          // Deal image
          Expanded(
            child: Image.asset(
              deal.imageUrl,
              fit: BoxFit.cover,
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
                  style: Theme.of(context).textTheme.subtitle1,
                ),
                
                // Deal prices
                Row(
                  children: [
                    // Old price
                    Text(
                      '\$${deal.oldPrice.toStringAsFixed(2)}',
                      style: TextStyle(
                        color: Colors.grey,
                        decoration: TextDecoration.lineThrough,
                      ),
                    ),
                    
                    const SizedBox(width: 8.0),
                    
                    // New price
                    Text(
                      '\$${deal.newPrice.toStringAsFixed(2)}',
                      style: TextStyle(
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
    );
  }
}
