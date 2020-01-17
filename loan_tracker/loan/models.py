from django.db import models

# Create your models here.
class Brrower(models.Model):
    name=models.CharField(max_length="256");
class Investor(models.Model):
    name=models.CharField](max_length="256");
    balance=models.IntegerField();
class Loan(models.Model):
    duration=models.CharField(default="6 Months",max_length="256");
    amount=models.IntegerField(default=5000.0);
    currency=models.CharField(default="$ Americian Dolar",max_length="256");
    brrower=models.OneToOneField(Brrower,on_delete=Models.CASCADE);
    investor=models.OneToOneField(Investor,on_delete=models.CASCADE)