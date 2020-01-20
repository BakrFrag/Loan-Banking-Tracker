from django.contrib import admin
from django.urls import path,include;

# swagger view
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Loan Tracker')
# coreapi documentation
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('loan.urls')),
    path("swagger-docs/",schema_view),
    path("core-docs/",include_docs_urls(title="Loan Tracker"))
]
