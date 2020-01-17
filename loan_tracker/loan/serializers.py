from loan.models import Brrower, Investor , Loan ;
from rest_framework import serializers;

# loan list/retrieve serializer Get Request
class LoanListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan;
        fields='__all__';
        
# loan create serializer Post Request
class LoanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan;
        fields=("brrower",);
           
       
# brrower serializer
class BrrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brrower;
        fields="__all__";
# investor serializer
class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Investor;
        fields="__all__";
class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer;
        fields="__all__";