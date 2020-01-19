from django.contrib import admin
from django.urls import path,include;
# swagger view
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Loan Tracker')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('loan.urls')),
    path("swagger-docs",schema_view)
]
