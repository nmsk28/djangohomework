from django.urls import path
from . import views
from .views import my_index
from .views import my_about

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('', my_index, name='index'),
    path('about', my_about, name='about'),
]