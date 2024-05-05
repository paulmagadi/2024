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
                    },
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'T-Shits',
                    onPressed: () {},
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Dress',
                    onPressed: () {},
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Shirts',
                    onPressed: () {},
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Kids Shoes',
                    onPressed: () {},
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Women shoes',
                    onPressed: () {},
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Men shoes',
                    onPressed: () {},
                  ),
                  CategoryItem(
                    icon: Icons.category,
                    title: 'Sandals',
                    onPressed: () {},
                  ),

                  // more CategoryItem widgets
                ],
              ),
            ),
          ),

          // Banner section
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Container(
              height: 200.0,
              decoration: BoxDecoration(
                image: const DecorationImage(
                  image: AssetImage('assets/images/banner1.png'),
                  fit: BoxFit.contain,
                ),
                borderRadius: BorderRadius.circular(4.0),
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
