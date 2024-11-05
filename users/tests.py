from django.test import TestCase
from django.contrib.auth.models import User
class LoginTestCase(TestCase):
    def setUp(self):
        # Create a test user to login with
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
    def test_login(self):
        # Test if the user can log in with valid credentials
        login = self.client.login(username='testuser', password='testpassword123')
        self.assertTrue(login)  # Assert that login is successful
    def test_login_invalid_password(self):
        # Test if the user cannot log in with an invalid password
        login = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(login)  # Assert that login fails with wrong credentials
