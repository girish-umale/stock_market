from django.urls import path
from .views import (
    stock_detail_view,
    stock_list_view,
    save_order,
)

app_name = 'stocks_url'

urlpatterns = [
    path('', stock_list_view, name='show_all_stocks'),
    path('save/', save_order, name='save_order_details'),
    path('details/<int:id>/', stock_detail_view, name='stock_detail'),
]
