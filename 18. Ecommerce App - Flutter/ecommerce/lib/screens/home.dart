import 'package:flutter/material.dart';
import '../components/category_menu.dart';
import '../components/banner_carousel.dart';


class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Horizontal menu for categories
          const Padding(
            padding: EdgeInsets.symmetric(vertical: 8.0),
            child: CategoryMenu(),
          ),

          // Banner section
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
            child: Container(
              height: 200.0,
              decoration: BoxDecoration(
                image: const DecorationImage(
                  image: AssetImage('assets/images/banner/1.png'),
                  fit: BoxFit.contain,
                ),
                borderRadius: BorderRadius.circular(4.0),
              ),
            ),
          ),

          // Add the BannerCarousel component
          const Padding(
            padding: EdgeInsets.symmetric(vertical: 1.0),
            child: BannerCarousel(),
          ),

          // Add other sections such as featured products, promotions, etc.
        ],
      ),
    );
  }
}
