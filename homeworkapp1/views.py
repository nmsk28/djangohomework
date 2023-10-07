from django.http import HttpResponse
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def my_index(request):
    context = {"main":"Главная страница",
               "text": "Здесь  данныме о моем первом Django-сайте"}
    return render(request, "homeworkapp1/index.html", context)

def my_about(request):
    context = {"about": "О себе",
                "text": "Здесь данные обо мне"}
    return render(request, "homeworkapp1/about.html", context)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Главная страница</h1>"
                        "<p>Здесь  данныме о моем первом Django-сайте</p>")

def about(request):
    return HttpResponse("<h1>О себе</h1>"
                        "<p>Здесь данные обо мне</p>")
