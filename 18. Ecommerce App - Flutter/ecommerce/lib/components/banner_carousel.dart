import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

class BannerCarousel extends StatelessWidget {
  const BannerCarousel({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return CarouselSlider(
      items: [
        Image.asset('assets/images/banner/7.png', fit: BoxFit.contain),
        Image.asset('assets/images/banner/2.png', fit: BoxFit.contain),
        Image.asset('assets/images/banner/4.png', fit: BoxFit.contain),
        Image.asset('assets/images/banner/5.png', fit: BoxFit.contain),
        Image.asset('assets/images/banner/6.png', fit: BoxFit.contain),
        Image.asset('assets/images/banner/3.png', fit: BoxFit.contain),
      ],
      options: CarouselOptions(
        height: 160.0,
        autoPlay: true,
        autoPlayInterval: const Duration(seconds: 5),
        aspectRatio: 16 / 9,
        enlargeCenterPage: true,
        onPageChanged: (index, reason) {
          // Handle page change events if needed
          // print('Carousel page changed to index: $index');
        },
      ),
    );
  }
}
