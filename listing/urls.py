from django.urls import path
from .views import (
    stock_detail_view,
    stock_list_view,
    save_order,
)


urlpatterns = [
    path('', stock_list_view, name='show_all_stocks'),
    path('saveorder/', save_order, name='saveorder'),
    path('details/<int:id>/', stock_detail_view, name='stock_detail'),
]
