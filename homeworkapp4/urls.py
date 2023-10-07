from django.urls import path
from .views import add_product, upload_image


urlpatterns = [
        path('product_add/', add_product, name='add_product'),
        path('upload/', upload_image, name='upload_image'),
        ]