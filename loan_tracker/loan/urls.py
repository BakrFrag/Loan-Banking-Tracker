from django.urls import path
from loan import views;
urlpatterns = [
    # loan urls
    path("loan/list/",views.LoanListView.as_view(),name="loan_list"),
    path("loan/<int:pk>/",views.LoanApiView.as_view(),name="loan"),
    path("loan/create/",views.LoanCreateView.as_view(),name="create_loan"),
    # investor urls
    path("investor/list/",views.InvestorListView.as_view(),name="investor_list"),
    path("investor/<int:pk>/",views.InvestorApiView.as_view(),name="investor"),
    path("investor/create/",views.InvestorCreateView.as_view(),name="create_investor"),
    # brrower urls
    path("brrower/list/",views.BrowerListView.as_view(),name="brrower_list"),
    path("brrower/<int:pk>/",views.BrrowerApiView.as_view(),name="brrower"),
    path("brrower/create/",views.BrrowerCreateView.as_view(),name="create_brrower"),
    # offer list 
    path("offer/list/",views.OfferListView.as_view(),name="offer_list"),
    path("offer/<int:pk>/",views.OfferApiView.as_view(),
    name="offer"),
    path("offer/create/",views.OfferCreateView.as_view(),name="create_offer"),
]
