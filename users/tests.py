from django.contrib.auth import get_user_model
from django.test import TestCase

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
