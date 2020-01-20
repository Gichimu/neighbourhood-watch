from django.test import TestCase
from .models import Profile, Neighbourhood, Business
from django.contrib.auth.models import User

class profileModelTest(TestCase):

    def setUp(self):
        self.test_user = User(username = 'test_user', email = 'test@test.com')
        self.test_user.save()
        self.test_neighbourhood = Neighbourhood(name = 'Test', location = 'Nairobi', occupants = 0)
        self.test_neighbourhood.save()
        self.test_profile = Profile(avatar = 'https://ucarecdn.com/19e91691-fcec-449a-bd7d-e882c910d2e1/', bio = 'test bio', neighbourhood_id = self.test_neighbourhood.id, user_id = self.test_user.id)
        self.test_profile.save()
        self.test_business = Business(name = 'test business', email = 'test@test.com', neighbourhood_id = self.test_neighbourhood.id, profile_id = self.test_profile.id)

    def test_create_neighbourhood(self):
        self.test_neighbourhood.save_neighbourhood()
        obj = Neighbourhood.objects.get(name = 'Test')
        self.assertEqual(self.test_neighbourhood.id, obj.id)

    def test_create_profile(self):
        self.test_profile.save_profile()
        obj = Profile.objects.get(bio = 'test bio')
        self.assertEqual(self.test_profile.id, obj.id)

    def test_create_business(self):
        self.test_business.save_business()
        obj = Business.objects.get(name = 'test business')
        self.assertEqual(self.test_business.id, obj.id)

    def test_delete_neighbourhood(self):
        self.test_neighbourhood.save_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.test_neighbourhood.delete_neighbourhood()
        hoods1 = Neighbourhood.objects.all()
        self.assertEqual(len(hoods), (len(hoods1) - 1))

