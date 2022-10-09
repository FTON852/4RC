from django.urls import path

from .views import balance, balance_nft, get_nft, transactions_history

urlpatterns = [
    path('balance/<str:public_key>/', balance, name='balance'),
    path('balance_nft/<str:public_key>/', balance_nft, name='balance_nft'),
    path('get_nft/<int:id>/', get_nft, name='balance'),
    path('transactions_history/<str:public_key>/', transactions_history, name='transactions_history'),
]
