import logging
from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm

logger = logging.getLogger(__name__)


def add_product(request):
    message = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            logger.info(f'Получили {name=}, {description=}, {price=}, {quantity=}.')
            product = Product(name=name, description=description, price=price, quantity=quantity)
            product.save()
            message = 'Товар сохранен'

    else:
        form = ProductForm()
        message='Заполните форму'
        return render(request, 'homeworkapp4/product_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
        return render(request, 'homeworkapp4/upload_image.html', {'form': form})
