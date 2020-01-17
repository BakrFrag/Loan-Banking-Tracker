from django.db import models

# Create your models here.
class Brrower(models.Model):
    name=models.CharField(max_length=256);
class Investor(models.Model):
    name=models.CharField(max_length=256);
    balance=models.IntegerField();
LOAN_CHOICES=(
    ("funded","Fundded"), # investor submit offer;
    ("complete","Completed") # brrower return mony back to investor
);
class Loan(models.Model):
    duration=models.CharField(default="6 Months",max_length=256);
    amount=models.IntegerField(default=5000.0);
    currency=models.CharField(default="$ Americian Dolar",max_length=256);
    status=models.CharField(choices=LOAN_CHOICES,max_length=256,null=True);
    brrower=models.OneToOneField(Brrower,on_delete=models.CASCADE);
    investor=models.OneToOneField(Investor,on_delete=models.CASCADE)