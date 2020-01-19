from celery.task.schedules import crontab
from celery.decorators import periodic_task
from loan.models import (Loan,Brrower,Investor,Offer)
from datetime import datetime as dt;
from datetime import timezone;
@periodic_task(run_every=(crontab(minute='*')),
name="brrower_money_back_to_investor",ignore_result=True,)
def brrower_money_back_to_investor():
    offers=Offer.objcts.all().filter(status="funded");
    for i in offers:
        offer_time=i.created;
        now=dt.now(timezone.utz);
        diff = (now - offer_time).days;
        if diff > 0 and diff%30==0:
            loan=i.loan;
            investor=i.investor;
            # 6 months  >> 5750
            # 1000 1000 1000 1000 1000 750
            if loan.total_money > 1000:
                loan.total_money -= 1000;
                loan.save();
                investor.balance += 1000;
                investor.save();
            elif loan < 1000 :
                loan.total_money = 0;
                loan.status="completed";
                loan.save();
                investor.balance += 750;
                investor.save();
        
