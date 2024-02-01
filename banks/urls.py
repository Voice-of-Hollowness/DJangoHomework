from django.urls import path
from .views import bank_list, bank_detail, add_banks

urlpatterns = [
    path('banks/', bank_list, name='bank_list'),
    path('banks/<int:bank_id>/', bank_detail, name='bank_detail'),
    path('banks/add/', add_banks, name='add_banks'),
]
