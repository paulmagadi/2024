import 'package:flutter/material.dart';
import 'package:curved_navigation_bar_with_label/curved_navigation_bar.dart';
import './screens/home.dart';
import './screens/category.dart';
import './screens/deals.dart';
import './screens/cart.dart';
import './screens/account.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Bellamore',
      theme: ThemeData(),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  final List<Widget> _pages = [
    const HomeScreen(),
    const CategoryScreen(),
    const DealsScreen(),
    const CartScreen(),
    const ProfileScreen(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
                    children: [
                        // Logo: Place an Image widget as the leading widget in AppBar
                        Image.asset(
                            'assets/images/sqlogo.jpg',  // Path to your logo image
                            height: 30,  // Adjust the height as desired
                        ),
                        // Spacer to push the search bar to the right
                        Spacer(),
                        // Search bar: Add a TextField as an action
                        Expanded(
                            child: TextField(
                                onSubmitted: (String query) {
                                    // Handle search query submission
                                    print('Search query: $query');
                                },
                                decoration: InputDecoration(
                                    hintText: 'Search...',
                                    hintStyle: TextStyle(color: Colors.white70),
                                    border: InputBorder.none,
                                    icon: Icon(Icons.search, color: Colors.white),
                                ),
                                style: TextStyle(color: Colors.white),
                            ),
                        ),
                    ],
                ),
      ),
      body: _pages[_selectedIndex],
      bottomNavigationBar: CurvedNavigationBar(
        items: [
          CurvedNavigationBarItem(icon: const Icon(Icons.home), label: "Home"),
          CurvedNavigationBarItem(
              icon: const Icon(Icons.category), label: "Category"),
          CurvedNavigationBarItem(icon: const Icon(Icons.home), label: "Deals"),
          CurvedNavigationBarItem(
              icon: const Icon(Icons.shopping_cart), label: "Cart"),
          CurvedNavigationBarItem(
              icon: const Icon(Icons.person), label: "Account"),
        ],
        onTap: (index) {
          // Update the state when an item is tapped
          setState(() {
            _selectedIndex = index;
          });
        },
      ),
    );
  }
}
