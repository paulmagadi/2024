import './product_model.dart';
import '../components/products.dart';
import '../components/new_arrivals.dart';
import '../components/deals.dart';
import '../components/featured.dart';

// Define conversion functions
AllProduct convertProductToAllProduct(Product product) {
  return AllProduct(
    imageUrl: product.image,
    title: product.name,
    price: product.price,
    salePrice: product.salePrice,
    isSale: product.isSale,
  );
}

Deal convertProductToDeal(Product product) {
  return Deal(
    imageUrl: product.image,
    title: product.name,
    oldPrice: product.price,
    newPrice: product.salePrice,
  );
}

FeaturedProduct convertProductToFeaturedProduct(Product product) {
  return FeaturedProduct(
    imageUrl: product.image,
    title: product.name,
    price: product.price,
  );
}

NewItem convertProductToNewProduct(Product product) {
  return NewItem(
    imageUrl: product.image,
    title: product.name,
    oldPrice: product.price,
    newPrice: product.salePrice,
    isSale: product.isSale,
    isNew: product.isNew,
    description: product.description,
  );
}


Product convertNewItemToProduct(NewItem newItem) {
    return Product(
        name: newItem.title,
        image: newItem.imageUrl,
        price: newItem.oldPrice,
        salePrice: newItem.newPrice,
        isSale: newItem.isSale,
        isNew: newItem.isNew,
        description: newItem.description,
        inStock: product.inStock
      stockQuantity: 
      discount: 
      percentageDiscount: 
      isNew: 
      isFeatured: 
      isListed: 
      createdAt: 
    );
}