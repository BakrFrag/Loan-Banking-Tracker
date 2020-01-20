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
        response=client.post(
        reverse("create_loan"),
        {"brrower":"random_name"},
        format="json");
        # no brrower random_name so status code 400
        self.assertEqual(response.status_code,400);
"""
testcase to get list of all brrower
"""
class TestListBrrower(TestCase):
    def test_listbrrower(self):
        client=APIClient();
        response=client.get(reverse("brrower_list"),format="json");
        self.assertEqual(response.status_code,200);
"""
test case create brrower
"""
class TestCreateBrrower(TestCase):
    def test_createbrrower(self):
        client=APIClient();
        response=client.post(reverse("create_brrower"),
        {"name":"random_brrower"},format="json");
        self.assertEqual(response.status_code,201);
"""
testcase to list all investors
"""
class TestListInvestor(TestCase):
    def test_listinvestor(self):
        client=APIClient();
        response=client.get(reverse("investor_list"));
        self.assertEqual(response.status_code,200);
"""
test create investor 
"""
class TestCreateInvestor(TestCase):
    def test_createinvestor(self):
        client=APIClient();
        response=client.post(reverse("create_investor"),
        {"name":"test_investor","balance":7000},
        format="json");
        self.assertEqual(response.status_code,201);
