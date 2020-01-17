from django.urls import path
from loan import views;
urlpatterns = [
    path("loan/list/",views.LoanListView.as_view(),name="loan_list"),
    path("loan/create/",views.LoanCreateView.as_view(),name="create_loan"),
    path("investor/list/",views.InvestorListView.as_view(),name="investor_list"),
    path("investor/create/",views.InvestorCreateView.as_view(),name="create_investor"),
    path("brrower/list/",views.BrowerListView.as_view(),name="brrower_list"),
    path("brrower/create/",views.BrrowerCreateView.as_view(),name="create_brrower"),
]
