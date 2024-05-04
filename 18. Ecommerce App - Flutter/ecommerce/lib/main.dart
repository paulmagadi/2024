import 'package:flutter/material.dart';
import 'package:curved_navigation_bar_with_label/curved_navigation_bar.dart';
import './screens/home.dart';

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
        title: const Text("Bellamore Online Shop"),
      ),
      body: _pages[_selectedIndex],
      bottomNavigationBar: CurvedNavigationBar(items: [
        CurvedNavigationBarItem(icon: const Icon(Icons.home), label: "Home"),
        CurvedNavigationBarItem(
            icon: const Icon(Icons.category), label: "Category"),
        CurvedNavigationBarItem(icon: const Icon(Icons.home), label: "Deals"),
        CurvedNavigationBarItem(
            icon: const Icon(Icons.shopping_cart), label: "Cart"),
        CurvedNavigationBarItem(
            icon: const Icon(Icons.person), label: "Account"),
      ]),
    );
  }
}
