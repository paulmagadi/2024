import 'package:flutter/material.dart';
import '../screens/deals.dart';

class NewItem {
  final String imageUrl;
  final String title;
  final double oldPrice;
  final double newPrice;
  final bool isNew;
  final bool isSale; // Add this property

  NewItem({
    required this.imageUrl,
    required this.title,
    required this.oldPrice,
    required this.newPrice,
    required this.isNew,
    required this.isSale, // Initialize this property
  });
}

class NewArrivalsSection extends StatelessWidget {
  final List<NewItem> newItems;

  const NewArrivalsSection({Key? key, required this.newItems})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Section title and "See More" button
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'New Arrivals',
                  style: Theme.of(context).textTheme.headline6,
                ),
                TextButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const DealsScreen()),
                    );
                  },
                  child: const Text('See More'),
                ),
              ],
            ),
          ),
          // Horizontally scrolling list of new items
          SizedBox(
            height: 180, // Adjust height as needed
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: newItems.length,
              itemBuilder: (context, index) {
                return NewItemWidget(newItem: newItems[index]);
              },
            ),
          ),
        ],
      ),
    );
  }
}

class NewItemWidget extends StatelessWidget {
  final NewItem newItem;

  const NewItemWidget({Key? key, required this.newItem}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 4.0),
      child: Card(
        elevation: 2.0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8.0),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Image
            ClipRRect(
              borderRadius:
                  const BorderRadius.vertical(top: Radius.circular(8.0)),
              child: Image.network(
                newItem.imageUrl,
                fit: BoxFit.cover,
                errorBuilder: (context, error, stackTrace) =>
                    const Icon(Icons.error, color: Colors.red),
                loadingBuilder: (context, child, loadingProgress) {
                  if (loadingProgress == null) {
                    return child;
                  } else {
                    return const Center(child: CircularProgressIndicator());
                  }
                },
              ),
            ),

            // Details
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    newItem.title,
                    style: Theme.of(context).textTheme.subtitle1,
                  ),
                  const SizedBox(height: 4.0),

                  // If the item is new and on sale, display the old price (struck through) and new price
                  if (newItem.isNew && newItem.isSale) ...[
                    Row(
                      children: [
                        // Old price (struck through)
                        Text(
                          '\$${newItem.oldPrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.grey,
                            decoration: TextDecoration.lineThrough,
                          ),
                        ),
                        const SizedBox(width: 4.0),
                        // New price (highlighted)
                        Text(
                          '\$${newItem.newPrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.red,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ] else if (newItem.isNew) ...[
                    // If the item is new but not on sale, display the new price only
                    Text(
                      '\$${newItem.newPrice.toStringAsFixed(2)}',
                      style: const TextStyle(
                        color: Colors.green,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
