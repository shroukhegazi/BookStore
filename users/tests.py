from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve # new
from .forms import CustomUserCreationForm # new
from .views import SignupPageView # new

class CustomUserTests(TestCase):
    def test_create_user(self):
        User= get_user_model()
        user=User.objects.create_user(username='admin',email='admin@ad.com',password='12345')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email,'admin@ad.com')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_active)

        
    def test_create_user(self):
        User= get_user_model()
        super_user=User.objects.create_superuser(username='admin11',email='admin11@ad.com',password='12345')
        self.assertEqual(super_user.username, 'admin11')
        self.assertEqual(super_user.email,'admin11@ad.com')
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_active)

class SignupPageTests(TestCase): # new
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')
    def test_signup_form(self): # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    def test_signup_view(self): # new
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
)