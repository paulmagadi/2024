import 'package:flutter/material.dart';
import '../models/product_model.dart'; 

class ProductDetailsScreen extends StatelessWidget {
    final Product product; // The selected product

    const ProductDetailsScreen({Key? key, required this.product}) : super(key: key);

    @override
    Widget build(BuildContext context) {
        return Scaffold(
            appBar: AppBar(
                title: Text(product.name),
            ),
            body: SingleChildScrollView(
                child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                        // Display product image
                        Image.network(
                            product.image,
                            fit: BoxFit.cover,
                            errorBuilder: (context, error, stackTrace) => const Icon(Icons.error, color: Colors.red),
                        ),

                        // Display product title
                        Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: Text(
                                product.name,
                                style: Theme.of(context).textTheme.headlineSmall,
                            ),
                        ),

                        // Display old price and new price (if applicable)
                        if (product.isSale) ...[
                            Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Row(
                                    children: [
                                        // Old price (struck through)
                                        Text(
                                            '\$${product.price.toStringAsFixed(2)}',
                                            style: const TextStyle(
                                                color: Colors.grey,
                                                decoration: TextDecoration.lineThrough,
                                            ),
                                        ),
                                        const SizedBox(width: 8.0),
                                        // New price (highlighted)
                                        Text(
                                            '\$${product.salePrice.toStringAsFixed(2)}',
                                            style: const TextStyle(
                                                color: Colors.red,
                                                fontWeight: FontWeight.bold,
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ] else ...[
                            // Display only the new price if no sale
                            Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Text(
                                    '\$${product.price.toStringAsFixed(2)}',
                                    style: const TextStyle(
                                        color: Colors.green,
                                        fontWeight: FontWeight.bold,
                                    ),
                                ),
                            ),
                        ],

                        // Display product description or other details
                        Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: Text(
                                product.description,
                                // product.description ?? 'No description available.',
                                style: Theme.of(context).textTheme.bodyMedium,
                            ),
                        ),

                        // Add more product details or related products if needed...
                    ],
                ),
            ),
        );
    }
}
