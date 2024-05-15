import 'package:flutter/material.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: SingleChildScrollView(
        child: Column(
          children: [
            //card
            Card(
              elevation: 4.0,
              margin: EdgeInsets.all(24.0),
              child: Padding(
                padding: EdgeInsets.all(16.0),
                // The entire card is a row
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    //Create two columns.
                    // First column
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        //Create a row for each item
                        Row(
                          //The row wil have 3 children(icon, space and texts)
                          children: [
                            Icon(Icons.phone, color: Colors.green),
                            SizedBox(
                                width: 8), // Add spacing between icon and text
                            // The texts will be in a column with children. 2
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Tell',
                                    style:
                                        TextStyle(fontWeight: FontWeight.bold)),
                                Text('+2547000000',
                                    style: TextStyle(color: Colors.grey)),
                              ],
                            ),
                          ],
                        ),
                        SizedBox(height: 16), // Add spacing between rows
//REPEATE THE ABOVE FOR ALL THE ROWS
                        // Email information
                        Row(
                          children: [
                            Icon(Icons.email, color: Colors.green),
                            SizedBox(width: 8),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Email',
                                    style:
                                        TextStyle(fontWeight: FontWeight.bold)),
                                Text('sqcodes@gmail.com',
                                    style: TextStyle(color: Colors.grey)),
                              ],
                            ),
                          ],
                        ),
                        SizedBox(height: 16), // Add spacing between rows

                        // Website information
                        Row(
                          children: [
                            Icon(Icons.web, color: Colors.green),
                            SizedBox(width: 8),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Website',
                                    style:
                                        TextStyle(fontWeight: FontWeight.bold)),
                                GestureDetector(
                                  onTap: () {
                                    // Handle website tap
                                    // You can use url_launcher package to launch the URL
                                  },
                                  child: const Text(
                                    'sqcodes.com',
                                    style: TextStyle(color: Colors.grey),
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                        const SizedBox(height: 16), // Add spacing between rows

                        // Address information
                        const Row(
                          children: [
                            Icon(Icons.location_on, color: Colors.green),
                            SizedBox(width: 8),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Address',
                                    style:
                                        TextStyle(fontWeight: FontWeight.bold)),
                                Text('Nairobi, Kenya',
                                    style: TextStyle(color: Colors.grey)),
                              ],
                            ),
                          ],
                        ),
                      ],
                    ),
                    Column(
                      children: <Widget>[
                        // Container with a circular border and a CircleAvatar as child
                        Container(
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            border: Border.all(
                              color: Colors.green, // Border color
                              width: 4, // Border width
                            ),
                          ),
                          child: const CircleAvatar(
                            radius: 55,
                            backgroundImage: AssetImage('images/paul.jpg'),
                          ),
                        ),
                        const SizedBox(height: 20),
                        const Text(
                          'Paul Magadi',
                          style: TextStyle(
                            fontSize: 20.0,
                            fontWeight: FontWeight.bold,
                            color: Colors.black,
                          ),
                        ),
                        const SizedBox(height: 10),
                        const Text(
                          'Software Developer',
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: 16.0,
                            color: Colors.black,
                          ),
                        ),
                        // const SizedBox(height: 20),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
