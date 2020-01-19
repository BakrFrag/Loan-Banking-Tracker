from django.test import TestCase
from rest_framework.test import APIClient;
from django.urls import reverse;
# Create your tests here.
"""
test case to list loans GET REQUEST with status code 200
"""
class TestListLoan(TestCase):
    def test_loanlist(self):
        client=APIClient();
        response=client.get(reverse("loan_list"),format='json');
        self.assertEqual(response.status_code,200);
"""
test case to test create loan with status code 400
"""
class TestCreateLoan(TestCase):
    def test_createloan(self):
        client=APIClient();
        response=client.post(reverse("create_loan",kwargs={name:"test_brrower"}),format="json");
         self.assertEqual(response.status_code,400);

