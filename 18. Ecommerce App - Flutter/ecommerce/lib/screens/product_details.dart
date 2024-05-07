import 'package:flutter/material.dart';

// Define a class to represent the product
class Product {
    final String imageUrl;
    final String title;
    final String description;
    final double price;

    Product({
        required this.imageUrl,
        required this.title,
        required this.description,
        required this.price,
    });
}

// Define the product details screen widget
class ProductDetailsScreen extends StatelessWidget {
    final Product product;  // The product to display details for

    const ProductDetailsScreen({Key? key, required this.product}) : super(key: key);

    @override
    Widget build(BuildContext context) {
        return Scaffold(
            appBar: AppBar(
                title: Text(product.title),
            ),
            body: SingleChildScrollView(
                child: Column(
                    children: [
                        // Product image
                        Image.asset(
                            product.imageUrl,
                            fit: BoxFit.cover,
                            width: double.infinity,
                        ),
                        
                        // Product details
                        Padding(
                            padding: const EdgeInsets.all(16.0),
                            child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                    // Product title
                                    Text(
                                        product.title,
                                        style: Theme.of(context).textTheme.headlineSmall,
                                    ),
                                    
                                    // Product price
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
                                    
                                    // Product description
                                    Text(
                                        product.description,
                                        style: Theme.of(context).textTheme.bodyLarge,
                                    ),
                                    
                                    // Buttons (e.g., add to cart, add to wishlist)
                                    Row(
                                        children: [
                                            ElevatedButton(
                                                onPressed: () {
                                                    // Handle add to cart
                                                    // print('Add to cart');
                                                },
                                                child: const Text('Add to Cart'),
                                            ),
                                            const SizedBox(width: 8.0),
                                            OutlinedButton(
                                                onPressed: () {
                                                    // Handle add to wishlist
                                                    // print('Add to Wishlist');
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
