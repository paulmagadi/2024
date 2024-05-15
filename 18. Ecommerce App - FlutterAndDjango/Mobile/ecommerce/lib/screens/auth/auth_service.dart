// auth_service.dart
import 'package:shared_preferences/shared_preferences.dart';

class AuthService {
  static const String _authTokenKey = 'authToken';

  Future<void> saveAuthToken(String token) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setString(_authTokenKey, token);
  }

  Future<String?> getAuthToken() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    return prefs.getString(_authTokenKey);
  }

  Future<void> clearAuthToken() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.remove(_authTokenKey);
  }

  Future<bool> isAuthenticated() async {
    final token = await getAuthToken();
    return token != null;
  }
}
