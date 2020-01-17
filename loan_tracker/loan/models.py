from django.db import models

LOAN_CHOICES=(

    ("funded","Fundded"), # investor submit offer;
    ("complete","Completed") # brrower return mony back to investor
);
# Create your models here.
class Brrower(models.Model):
    name=models.CharField(max_length=256);
    def __str__(self):
        return self.name;
class Investor(models.Model):
    name=models.CharField(max_length=256);
    balance=models.IntegerField();
    def __str__(self):
        return self.name;
class Loan(models.Model):
    duration=models.CharField(default="6 Months",max_length=256);
    amount=models.IntegerField(default=5000.0);
    currency=models.CharField(default="$ Americian Dolar",max_length=256);
    status=models.CharField(choices=LOAN_CHOICES,max_length=256,null=True);
    brrower=models.OneToOneField(Brrower,on_delete=models.CASCADE);
    def __str__(self):
        return f"Loan With Brrower {self.brrower.name} And Investor {self.investor.name}";
class Offer(models.Model):
    loan=models.OneToOneField(Loan,on_delete=models.CASCADE);
    investor=models.OneToOneField(Investor,on_delete=models.CASCADE);
    def __str__(self):
        return f"offer on {self.loan}";