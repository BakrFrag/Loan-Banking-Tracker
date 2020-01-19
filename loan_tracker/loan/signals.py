from django.db.models.signals import post_save;
from loan.models import Offer;
from django.dispatch import receiver;
@receiver(post_save,sender=Offer)
def set_new_values(sender,created,instance,**kwargs):
        if created:
            investor=instance.investor;
            loan=instance.loan;
            investor.balance -=5003;
            investor.save();
            loan.status="funded";
            loan.total_money +=750;