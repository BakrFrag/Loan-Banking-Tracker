from django.db import models
from django.dispatch import receiver;
from django.db.models.signals import post_save;
# Annual Interest Rate 5000*(15/100) =750
Annual_Interest_Rate=750;
LOAN_CHOICES=(

    # investor submit offer
    ("funded","Fundded"), 
    # brrower return mony back to investor
    ("complete","Completed") 
);

class Brrower(models.Model):
    name=models.CharField(max_length=256,unique=True);
    def __str__(self):
        return self.name;
class Investor(models.Model):
    name=models.CharField(max_length=256,unique=True);
    balance=models.IntegerField();
    def __str__(self):
        return self.name;

"""
total_money field will hold the total money brrower have to 
give back to investor 
when loan created the field will be 5000 (loan ammount)
when offer come to this loan the total_money will be 
5750 (amount + annual_rate)
"""
class Loan(models.Model):
    duration=models.CharField(default="6 Months",max_length=256);
    amount=models.IntegerField(default=5000.0);
    annual_rate = models.FloatField(default=0.15);
    currency=models.CharField(default="$ Americian Dolar",max_length=256);
    status=models.CharField(choices=LOAN_CHOICES,max_length=256,null=True);
    total_money=models.IntegerField(default=5000);
    brrower=models.OneToOneField(Brrower,on_delete=models.CASCADE);
    def save(self,*args,**kwargs):
        self.duration="6 Months";
        self.amount=5000.0;
        self.currency="$ Americian Dolar";
        self.annual_rate=0.15;
        super(Loan,self).save(*args,**kwargs);

    def __str__(self):
        return f"Loan With Brrower {self.brrower.name} "
class Offer(models.Model):
    loan=models.OneToOneField(Loan,on_delete=models.CASCADE);
    investor=models.OneToOneField(Investor,on_delete=models.CASCADE);
    created=models.DateTimeField(auto_now_add=True);
    


# def set_new_values(sender,created,instance,**kwargs):
#     if created:
#         investor=instance.investor;
#         loan=instance.loan;
#         investor.balance -= 5003;
#         investor.save();
#         loan.status = "funded";
#         loan.total_money += 750;
#         loan.save();
# post_save.connect(set_new_values,sender=Offer)