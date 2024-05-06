import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

class BannerCarousel extends StatefulWidget {
  const BannerCarousel({Key? key}) : super(key: key);

  @override
  _BannerCarouselState createState() => _BannerCarouselState();
}

class _BannerCarouselState extends State<BannerCarousel> {
  final List<String> items = [
    'assets/images/banner/7.png',
    'assets/images/banner/2.png',
    'assets/images/banner/4.png',
    'assets/images/banner/5.png',
    'assets/images/banner/6.png',
    'assets/images/banner/3.png',
  ];
  final CarouselController _controller = CarouselController();
  int _current = 0;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        CarouselSlider(
          items: items.map((item) {
            return Image.asset(
              item,
              fit: BoxFit.contain,
              width: double.infinity,
            );
          }).toList(),
          carouselController: _controller,
          options: CarouselOptions(
            height: 170.0,
            autoPlay: true,
            autoPlayInterval: const Duration(seconds: 10),
            aspectRatio: 16 / 9,
            enlargeCenterPage: true,
            onPageChanged: (index, reason) {
              setState(() {
                _current = index;
              });
            },
          ),
        ),
        // Dots (indicators) at the bottom of the carousel
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: items.asMap().entries.map((entry) {
            return GestureDetector(
              onTap: () => _controller.animateToPage(entry.key),
              child: Container(
                width: 12.0,
                height: 12.0,
                margin: const EdgeInsets.symmetric(
                  vertical: 4.0,
                  horizontal: 4.0,
                ),
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: (Theme.of(context).brightness == Brightness.dark
                          ? Colors.white
                          : const Color.fromARGB(255, 250, 75, 0))
                      .withOpacity(_current == entry.key ? 0.9 : 0.4),
                ),
              ),
            );
          }).toList(),
        ),
      ],
    );
  }
}
