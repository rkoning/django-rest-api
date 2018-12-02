from django.test import TestCase
from .models import Account, Campaign, Advertisement
from rest_framework import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
# Create your tests here.

class AccountTestCase(TestCase):
    """Test suite for account model"""
    def setUp(self):
        """Define test client"""
        self.account_id = 1
        self.account = Account(account_id = 1)

    def test_model_can_create_an_account(self):
        """Test the account model can create an account"""
        old = Account.objects.count()
        self.account.save()
        self.assertNotEqual(old, Account.objects.count())

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.account_data = {'account_id': 1, 'account_descriptive_name' : 'test', 'customer_descriptive_name' : 'test'}
        self.response = self.client.post(
            reverse('create'),
            self.account_data,
            format = "json"
        )

    def test_api_can_create_an_account(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
