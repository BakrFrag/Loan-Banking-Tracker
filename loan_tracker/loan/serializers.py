from loan.models import Brrower, Investor , Loan,Offer ;
from rest_framework import serializers;



        
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

# loan list/retrieve serializer Get Request
class LoanListSerializer(serializers.ModelSerializer):
    brrower=BrrowerSerializer()
    class Meta:
        model=Loan;
        fields='__all__';
"""
add validation on offer serializer to ensure that 
investor balance have more than 5003 (loan amount + fee)
"""

class OfferSerializer(serializers.ModelSerializer):
    loan=LoanListSerializer();
    investor=InvestorSerializer();
    class Meta:
        model=Offer;
        fields="__all__";
    def validate(self,data):
        investor=data['investor'];
        loan=data['loan'];
        if investor.balance >= 5003:
            return data;
        raise serializers.ValidationError("Balance Of Investor Not Enought Money")
