from django.shortcuts import render
from rest_framework import generics;
from rest_framework.exceptions import APIException;
# Create your views here.
from loan.serializers import (LoanListSerializer,
LoanCreateSerializer,BrrowerSerializer,InvestorSerializer,OfferSerializer);
from loan.models import (Brrower,Loan,Investor,Offer);

"""
List All Loans Or Custimize Loan By Status Either 
funded or completed
GET REQUEST
"""
class LoanListView(generics.ListAPIView):
      model=Loan;
      serializer_class=LoanListSerializer;
      def get_queryset(self):
            status=self.request.GET.get('status',None);
            if status is not None:
                return Loan.objects.filter(status=status);
            return Loan.objects.all();

"""
create loan instance of loan model 
POST REQUEST
"""

class LoanCreateView(generics.CreateAPIView):
    model=Loan;
    serializer_class=LoanCreateSerializer;

"""
get one loan object by PK
GET REQUEST
"""
class LoanApiView(generics.RetrieveAPIView):
    model=Loan;
    serializer_class=LoanListSerializer;
    queryset=Loan.objects.all();
    lookup_field="pk";

"""
List All Brrowers Or Custimize Brrower List 
By Thier Names
GET REQUEST
"""
class BrowerListView(generics.ListAPIView):
    model=Brrower;
    serializer_class=BrrowerSerializer;
    def get_queryset(self):
        name=self.request.GET.get('name',None)
        if name is not None:
            return Brrower.objects.filter(name=name);
        return Brrower.objects.all();
"""
Create Brrower 
POST REQUEST
"""
class BrrowerCreateView(generics.CreateAPIView):
    model=Brrower;
    serializer_class=BrrowerSerializer;

"""
brrower get single object
GET REQUEST
"""
class BrrowerApiView(generics.RetrieveAPIView):
    model=Brrower;
    queryset=Brrower.objects.all();
    serializer_class=BrrowerSerializer;
    lookup_field="pk";
"""
List All Investors Or Just Custimize Them By Name
GET REQUEST
"""    
class InvestorListView(generics.ListAPIView):
    model=Investor;
    queryset=Investor.objects.all();
    serializer_class=InvestorSerializer;
    def get_queryset(self):
        name=self.request.GET.get('name',None)
        if name is not None:
            return Investor.objects.filter(name=name);
        return Investor.objects.all();
        
"""
Create Investor
POSTREQUEST
"""
class InvestorCreateView(generics.CreateAPIView):
    model=Investor;
    serializer_class=InvestorSerializer;

"""
investor get single object by PK
GET Request
"""
class InvestorApiView(generics.RetrieveAPIView):
    model=Investor;
    queryset=Investor.objects.all();
    serializer_class=InvestorSerializer;
    lookup_field="pk";

"""
List All Offers
GET REQUEST
"""
class OfferListView(generics.ListAPIView):
    model=Offer;
    serializer_class=OfferSerializer;
    queryset=Offer.objects.all();

"""
Create Offer
Validation Add By First Check
Money Mount = (Loan Amount + Fee ) = 5000 + 3 = 5003 
If Investor.Balance >= 5003
Will Create Loan and decrease investor balance by 5003
and change value of loan.total_money to be 5750
(loan ammount + annual rate)
Else APIException Will Riased
POST REQUEST
"""
class OfferCreateView(generics.CreateAPIView):
    model=Offer;
    serializer_class=OfferSerializer;
"""
get single offer object
GET REQUEST
"""
class OfferApiView(generics.RetrieveAPIView):
    model=Offer;
    queryset=Offer.objects.all();
    lookup_field="pk";
    serializer_class=OfferSerializer;