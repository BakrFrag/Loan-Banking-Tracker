from django.contrib import admin

# Register your models here.
from loan.models import Brrower , Loan , Investor;
admin.site.register([Loan,Brrower,Investor]);