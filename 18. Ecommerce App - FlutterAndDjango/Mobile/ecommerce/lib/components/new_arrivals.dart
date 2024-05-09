import 'package:flutter/material.dart';


import 'package:flutter/material.dart';
import '../screens/deals.dart';
// import 'new_item.dart'; // Make sure you have the new_item.dart file or create it

class NewArrivalsSection extends StatelessWidget {
  final List<NewItem> newItems;

  const NewArrivalsSection({Key? key, required this.newItems}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Title and "See More" button
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

class NewItem {
  final String imageUrl;
  final String title;
  final double oldPrice;
  final double newPrice;
  final bool isNew;

  NewItem({
    required this.imageUrl,
    required this.title,
    required this.oldPrice,
    required this.newPrice,
    required this.isNew,
  });
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
              borderRadius: const BorderRadius.vertical(top: Radius.circular(8.0)),
              child: Image.network(
                newItem.imageUrl,
                fit: BoxFit.cover,
                errorBuilder: (context, error, stackTrace) => const Icon(Icons.error, color: Colors.red),
                loadingBuilder: (context, child, loadingProgress) {
                  if (loadingProgress == null) {
                    return child;
                  } else {
                    return Center(child: CircularProgressIndicator());
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
                  if (newItem.isNew) ...[
                    // If the item is new, display old price (struck through) and new price
                    Row(
                      children: [
                        Text(
                          '\$${newItem.oldPrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.grey,
                            decoration: TextDecoration.lineThrough,
                          ),
                        ),
                        const SizedBox(width: 4.0),
                        Text(
                          '\$${newItem.newPrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.red,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ] else ...[
                    // If the item is not new, display the regular price only
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
