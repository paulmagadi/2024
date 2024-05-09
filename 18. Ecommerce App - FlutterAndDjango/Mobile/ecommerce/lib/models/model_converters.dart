// model_converters.dart

import './product_model.dart';


// Conversion function from NewItem to Product
Product convertNewItemToProduct(NewItem newItem) {
    return Product(
        name: newItem.title,
        image: newItem.imageUrl,
        price: newItem.oldPrice,
        salePrice: newItem.newPrice,
        isSale: newItem.isSale,
        isNew: newItem.isNew,
        // Add any additional properties as necessary
    );
}

// Add more conversion functions as needed...
