import './product_model.dart';
import '../components/products.dart';
import '../components/deals.dart';
// import '../components/featured.dart';

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

// FeaturedProduct convertProductToFeaturedProduct(Product product) {
//   return FeaturedProduct(
//     imageUrl: product.image,
//     title: product.name,
//     price: product.price,
//   );
// }
