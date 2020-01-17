from django.db import models

# Annual Interest Rate 5000*(15/100) =750
Annual_Interest_Rate=750;
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
    # field include total money (loan money + anaual interest rate)
    # total = 750+5000=5750
    # default will be 5000 but when offer be on this loan from investor will changed to 5570 - annaual rate added
    total=models.IntegerField(default=5000);
    brrower=models.OneToOneField(Brrower,on_delete=models.CASCADE);
    def save(self,*args,**kwargs):
        self.duration="6 Months";
        self.amount=5000.0;
        self.currency="$ Americian Dolar";
        super(Loan,self).save(*args,**kwargs);

    def __str__(self):
        return f"Loan With Brrower {self.brrower.name} And Investor {self.investor.name}";
class Offer(models.Model):
    loan=models.OneToOneField(Loan,on_delete=models.CASCADE);
    investor=models.OneToOneField(Investor,on_delete=models.CASCADE);
    def __str__(self):
        return f"offer on {self.loan}";