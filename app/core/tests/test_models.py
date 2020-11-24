from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test if creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user_with_email(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user_with_email(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email will raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user_with_email(None, 'test123')

