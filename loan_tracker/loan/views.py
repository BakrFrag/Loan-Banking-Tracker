from django.shortcuts import render
from rest_framework import generics;
# Create your views here.
from loan.serializers import (LoanListSerializer,LoanCreateSerializer,BrrowerSerializer,InvestorSerializer,OfferSerializer);
from loan.models import (Brrower,Loan,Investor,Offer);
class LoanListView(generics.ListAPIView):
      model=Loan;
      queryset=Loan.objects.all();
      serializer_class=LoanListSerializer;
class LoanCreateView(generics.CreateAPIView):
    model=Loan;
    serializer_class=LoanCreateSerializer;
class BrowerListView(generics.ListAPIView):
    model=Brrower;
    serializer_class=BrrowerSerializer;
    queryset=Brrower.objects.all();
class BrrowerCreateView(generics.CreateAPIView):
    model=Brrower;
    serializer_class=BrrowerSerializer;
class InvestorListView(generics.ListAPIView):
    model=Investor;
    queryset=Investor.objects.all();
    serializer_class=InvestorSerializer;
class InvestorCreateView(generics.CreateAPIView):
    model=Investor;
    serializer_class=InvestorSerializer;

class OfferListView(generics.ListAPIView):
    model=Offer;
    serializer_class=OfferSerializer;
    queryset=Offer.objects.all();
class OfferCreateView(generics.CreateAPIView):
    model=Offer;
    serializer_class=OfferSerializer;