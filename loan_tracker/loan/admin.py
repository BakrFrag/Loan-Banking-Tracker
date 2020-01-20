from django.contrib import admin

# Register your models here.
from loan.models import Brrower , Loan , Investor,Offer;
admin.site.register([Loan,Brrower,Investor,Offer]);