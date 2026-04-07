from django.urls import path
from api import views
urlpatterns = [
    path('companies/', views.companies_list),
    path('companies/<int:pk>/', views.company_detail),
]