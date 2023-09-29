from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Главная страница</h1>"
                        "<p>Здесь  данныме о моем первом Django-сайте</p>")

def about(request):
    return HttpResponse("<h1>О себе</h1>"
                        "<p>Здесь данные обо мне</p>")
