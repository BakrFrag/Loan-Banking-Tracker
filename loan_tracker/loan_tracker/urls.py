from django.contrib import admin
from django.urls import path,include;
# coreapi documentation
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('loan.urls')),
    
    path("core-docs/",include_docs_urls(title="Loan Tracker"))
]
