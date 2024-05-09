import 'dart:convert';
import 'package:http/http.dart' as http;
import 'product_model.dart';

Future<List<Product>> fetchProducts() async {
  final response =
      await http.get(Uri.parse('http://10.0.2.2:8000/api/products/'));

  if (response.statusCode == 200) {
    List<dynamic> data = jsonDecode(response.body);
    return data.map((product) => Product.fromJson(product)).toList();
  } else {
    throw Exception('Failed to load products');
  }
}
