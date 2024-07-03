from django.test import TestCase
from .models import Profile, Project, Skill, Contact, User

class ModelTests(TestCase):
    def test_create_profile(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        profile = Profile.objects.create(user=user, bio='Test bio')
        self.assertEqual(profile.bio, 'Test bio')