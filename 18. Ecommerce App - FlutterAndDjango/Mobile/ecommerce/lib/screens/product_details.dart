import 'package:flutter/material.dart';
import '../models/data.dart';  // Import the Product model class

class ProductDetailsScreen extends StatelessWidget {
  final Product product;

  const ProductDetailsScreen({Key? key, required this.product}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(product.name),
      ),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Display the product image
            Image.asset(
              product.image,
              fit: BoxFit.cover,
              width: double.infinity,
            ),
            // Product details
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Display the product title
                  Text(
                    product.name,
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  // Display the product price
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 8.0),
                    child: Text(
                      '\$${product.price.toStringAsFixed(2)}',
                      style: const TextStyle(
                        color: Colors.green,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                  // Display the product description
                  Text(
                    product.description,
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  // Add buttons (e.g., add to cart, wishlist) if needed
                  Row(
                    children: [
                      ElevatedButton(
                        onPressed: () {
                          // Handle add to cart
                        },
                        child: const Text('Add to Cart'),
                      ),
                      const SizedBox(width: 8.0),
                      OutlinedButton(
                        onPressed: () {
                          // Handle add to wishlist
                        },
                        child: const Text('Add to Wishlist'),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
