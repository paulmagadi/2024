import 'package:flutter/material.dart';
import '../screens/deals.dart';
import '../screens/product_details.dart';
import '../models/product_model.dart';
// import '../models/model_converters.dart';

class NewItem {
  final String name;
  final String description;
  final double price;
  final String image;
  final bool isSale;
  final double salePrice;
  final bool inStock;
  final int stockQuantity;
  final double discount;
  final int percentageDiscount;
  final bool isNew;
  final bool isFeatured;
  final bool isListed;
  final DateTime createdAt;

  NewItem({
    required this.name,
    required this.description,
    required this.price,
    required this.image,
    required this.isSale,
    required this.salePrice,
    required this.inStock,
    required this.stockQuantity,
    required this.discount,
    required this.percentageDiscount,
    required this.isNew,
    required this.isFeatured,
    required this.isListed,
    required this.createdAt,
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
                // Section title
                Text(
                  'New Arrivals',
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

    Product convertNewItemToProduct(NewItem newItem) {
    return Product(
        name: newItem.title,
        image: newItem.imageUrl,
        price: newItem.oldPrice,
        salePrice: newItem.newPrice,
        isSale: newItem.isSale,
        isNew: newItem.isNew,
        description: newItem.description,
        inStock: newItem.inStock
    );
}

    const NewItemWidget({Key? key, required this.newItem}) : super(key: key);

    @override
    Widget build(BuildContext context) {
        return GestureDetector(
            onTap: () {
                // Convert NewItem to Product using conversion function
                Product product = convertNewItemToProduct(newItem);
                
                // Navigate to the ProductDetailsScreen
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => ProductDetailsScreen(product: product),
                    ),
                );
            },
            child: Card(
                elevation: 2.0,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8.0),
                ),
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                        // Display product image and details...
                    ],
                ),
            ),
        );
    }
}
