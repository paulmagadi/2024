import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';

class BannerCarousel extends StatelessWidget {
    final List<String> images;  // List of image paths

    const BannerCarousel({Key? key, required this.images}) : super(key: key);

    @override
    Widget build(BuildContext context) {
        return CarouselSlider(
            items: images.map((imagePath) {
                return Image.asset(imagePath, fit: BoxFit.contain);
            }).toList(),
            options: CarouselOptions(
                height: 200.0,
                autoPlay: true,
                autoPlayInterval: Duration(seconds: 5), 
                aspectRatio: 16/9,
                enlargeCenterPage: true,
            ),
        );
    }
}
