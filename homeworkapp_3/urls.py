from django.urls import path
from homeworkapp_3 import views
from .views import clients_orders, order_full, clients_orders_day

urlpatterns = [
            path('', views.index, name='index'),
            path('about/', views.about, name='about'),
            path('clients/', views.get_clients, name='clients'),
            path('clients_order/<int:client_id>/', clients_orders, name='clients_orders'),
            path('order_full/<int:order_id>/', order_full, name='order_full'),
            path('clients_orders_day/<int:client_id>/', clients_orders_day, name='clients_orders_day'),
]


