import 'dart:convert';
import 'package:http/http.dart' as http;

class Product {
  final String name;
  final String description;
  final num price;  // Use 'num' type to handle both integers and doubles
  final String image;

  Product({
    required this.name,
    required this.description,
    required this.price,
    required this.image,
  });

  // Factory constructor to parse JSON data into a Product instance
  factory Product.fromJson(Map<String, dynamic> json) {
    // Check if 'price' key exists and is not null
    final priceValue = json['price'];
    if (priceValue != null) {
      // Try to convert the value to a double or integer
      final price = priceValue is num
          ? priceValue
          : double.tryParse(priceValue.toString());
      if (price != null) {
        return Product(
          name: json['name'] as String,
          description: json['description'] as String,
          price: price,
          image: json['image'] as String,
        );
      }
    }
    
    // If 'price' is not valid, throw an exception
    throw const FormatException('Invalid price format');
  }
}


// Function to fetch products from the backend
Future<List<Product>> fetchProducts() async {
  final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/products/'));

  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    return data.map((product) => Product.fromJson(product)).toList();
  } else {
    throw Exception('Failed to load products');
  }
}
