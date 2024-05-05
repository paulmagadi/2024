import 'package:flutter/material.dart';

// import 'package:ecommerce/constants/constants.dart';
// Import any additional necessary packages

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Horizontal menu for categories
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 8.0),
            child: SingleChildScrollView(
              scrollDirection:
                  Axis.horizontal, // Set scroll direction to horizontal
              child: Row(
                children: [
                  // Create a list of category items (e.g., buttons or cards)
                  CategoryItem(
                    icon: Icons.category, // Use appropriate icons or images
                    title: 'Shoes',
                    onPressed: () {
                      // Handle category selection (e.g., navigate to the category screen)
                      print('Category 1 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'T-Shits',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Dress',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Shirts',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Kids Shoes',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Women shoes',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Men shoes',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Sandals',
                    onPressed: () {
                      print('Category 2 selected');
                    },
                  ),

                  // Add more CategoryItem widgets for other categories
                ],
              ),
            ),
          ),
          // Add other sections such as featured products, promotions, etc.
        ],
      ),
    );
  }
}

// Define a custom widget for each category item
class CategoryItem extends StatelessWidget {
  final IconData icon;
  final String title;
  final VoidCallback onPressed;

  const CategoryItem({
    required this.icon,
    required this.title,
    required this.onPressed,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 8.0),
      child: ElevatedButton(
        onPressed: onPressed,
        style: ElevatedButton.styleFrom(
          padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
          // primary: Colors.white,
          // onPrimary: Colors.black,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8.0),
          ),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              size: 24.0,
            ),
            SizedBox(height: 4.0),
            Text(title),
          ],
        ),
      ),
    );
  }
}
