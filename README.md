# Project Name
Loan Tracker
# Project Description
Handle Loan Requests By Brrowers And Offers From Investors
Also Keep Track Of How Mony Get Back To Investors Monthly
# How It Works & Logic Of Project
> this section explain the logic used to build this project

> Loan Will Return As 
> 1000 1000 1000 1000 1000 750
1. Once Loan Created Offer Can Be Applay To Loan 

2. Before Offer Applay On Loan It Will 
Check If Investor Balance Greater Than Or Equal 5003 (Loan Ammout + Fee )

4. If Investor Balance Less Than 5003 (loan ammount + fee )
 
   Validation Error Will Riase 

5. Once Offer Applied On Loan 

Post Save Signal On Database Wil Do 

1. Investor Balance Will Decreased By 5003 (Loan Amount + Fee)

2. Loan Status Will Changed To Funded

3. Loan Total Money Will Changed To Be 

    5750 (loan amount + annual intetest rate )

As Money Will Be Returned Monthly To Investor 

Periodic Task Excute Every Day To Check 

1. If Difference Between This Day And Offer Day Is Months

2. Then It Check If Total Money Is Greater Than 1000

3. Loan Total Money Will Decreased By 1000 And Investor Balance Will Increase By 1000

4. If The Loan Total Money Less Than 1000

   This Mean It Is Last Mony 
So The Loan Total Money Will Be 0

   And Incrase Invetsor Balance By 750 (last charge)

5. And Loan Status Will Be Completed
 


# Project Api EndPoints Urls 
1. > Loan Model Urls

. Create Loan
```
127.0.0.1:8000/loan/create/
```
. List All Loans AS Last Created Shown First
```
127.0.0.1:8000/loan/list/
```
. you can custimize loans list by status

. get all loans with status funded

```
127.0.0.1:8000/loan/list/?status=funded
```
. get all loans with status completed


```
127.0.0.1:8000/loan/list/?status=completed
```
. get specfic loan by loan id

```
127.0.0.1:8000/loan/<int:pk>
```
>  Brrower Model Urls

. get list of all brrower

```
127.0.0.1:8000/brrower/list/
```
. custimize list by brrower name

```
127.0.0.1:8000/brrower/list/?name=b1
```
. create brrower
```
127.0.0.1:8000/brrower/create/
```
. get specif brrower by pk
```
127.0.0.1:8000/brrower/<int:pk>/
```
> Investor Urls

. list all investor
```
127.0.0.1:8000/investor/list/
```
. custimize investor by name
```
127.0.0.1:8000/investor/list/?name=inv1
```
. get single investor object by pk
```
127.0.0.1:8000/investor/<int:pk>/
```
. create investor 
```
127.0.0.1:8000/investor/create/
```
>  Offer Url

. list all offers
```
127.0.0.1:8000/offer/list/
```
. create offer
```
127.0.0.1:8000/offer/create/
```
. get single offer object
```
127.0.0.1:8000/offer/<int:pk>/
```
> Documentation Url

. documentation by swagger
```
127.0.0.1:8000/swagger-docs
```
# PreRequests
> Some Software Are Required To Be In Your Machine 

1. [Python3](https://www.python.org/)
. Programming Language Used
2. [Python3 Pip](https://pypi.org/project/pip/)
. Python Package Manager
3. [Redis Server](https://redis.io/)
. Used As Meeage Broker With Celery Library
4. [Git](https://git-scm.com/)
. Used To Clone Project From Github

# How To Run 
1. install pipenv package manager 
```
sudo pip3 install pipenv
```
2. clone project from github
```
git clone [url]
```
3. cd into project folder
```
cd Loan-Tracker
``` 
4. active virtualenv
```
pipenv shell 
```

5. install requested libraries
```
pipenv install -r requirements.txt
```
. if some thing gi wrong run 
```
pipenv install django djangorestframework celery celery[redis] coreapi
```
6.
``` 
cd loan_tracker
```
6. run development server
```
python manage.py runserver
```
7. if you mant to check tests
```
python manage.py test
```
8. periodic tasks will be excute every day in background

8. vist local host in your browser 
and play with urls 

# Python Libraries

1. [Django Framework](https://www.djangoproject.com/)

> Python Web Framework 

2. [Django Rest Framework](https://www.django-rest-framework.org/)

> Used To Build Api End Points 

3. [Rest Framework Swagger](https://django-rest-swagger.readthedocs.io/)

> Used To Build Documentation For Project

4. [Celery Library](https://docs.celeryproject.org/)

> Used To Perform Periodic Tasks 
6. [Coreapi](https://www.coreapi.org/)
> Used To Build Documentation

# Important Notes
> All These URL Tested And Works Fine
and Behave As Expected

> All Tests On test.py Works Fine

> Comments Tell You More Please Read It 

> This Project Developed On Ubuntu 18.2 Please If You use Different OS Some Issues May Happen

> This Project Developed In DEVELOPMENT MODE and settings of it not Suitable For Production Enviroment

