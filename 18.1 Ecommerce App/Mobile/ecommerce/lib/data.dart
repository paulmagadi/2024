import 'dart:convert';
import 'package:http/http.dart' as http;

class Product {
  final String name;
  final String description;
  final double price;

  Product({
    required this.name,
    required this.description,
    required this.price,
  });

  // Factory constructor to parse JSON data into a Product instance
  factory Product.fromJson(Map<String, dynamic> json) {
    return Product(
      name: json['name'],
      description: json['description'],
      price: json['price'].toDouble(),
    );
  }
}

// Function to fetch products from the backend
Future<List<Product>> fetchProducts() async {
  final response = await http.get(Uri.parse('http://10.0.2.2:8000/api/products/'));

  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    return data.map((product) => Product.fromJson(product)).toList();
  } else {
    throw Exception('Failed to load products');
  }
}
