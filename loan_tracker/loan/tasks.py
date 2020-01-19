from celery.task.schedules import crontab
from celery.decorators import periodic_task
from loan.models import (Loan,Brrower,Investor,Offer)

# @periodic_task(run_every=(crontab(minute='*')),
# name="brrower_money_back_to_investor",ignore_result=True,)
# def brrower_money_back_to_investor():
#     offers=Offer.objcts.all().filter(status="funded");
