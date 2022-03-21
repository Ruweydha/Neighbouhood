from django.test import TestCase
from .models import Neighbourhood, Businesses
from django.contrib.auth.models import User

# Create your tests here.
class NeighbourhoodTestClass(TestCase):  # Neighbourhood class test
    def setUp(self):

        # create a user
        self.user = User(username = 'ruweydha')
        self.user.save()
        self.hood = Neighbourhood(name="South b",location='Nairobi',Admin= self.user )

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighbourhood))

    def test_save_method(self):
        self.hood.create_neigbourhood()
        hood = Neighbourhood.find_neighbourhood(self.hood.id)
        self.assertIsNotNone(hood)

    def test_update_method(self):
        self.hood.name = 'South c'
        self.hood.save()
        hood = Neighbourhood.find_neighbourhood(self.hood.id)
        self.assertEqual(self.hood.name, hood.name)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'ruweydha')
        self.user.save()

        self.hood = Neighbourhood(name="South b",location='Nairobi',Admin= self.user )
        self.hood.create_neigbourhood()

        self.business = Businesses( name="test biz", user=self.user, neighbourhood=self.hood, email="rue@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Businesses))

    def test_save_method(self):
        self.business.create_business()
        business = Businesses.find_business(self.business.id)
        self.assertIsNotNone(business)

    def test_delete_method(self):
        self.business.create_business()
        self.business.delete()
        business = Businesses.objects.filter(id=self.business.id).exists()
        self.assertFalse(business)

