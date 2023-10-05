from django.http import HttpResponse
import logging
import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from homeworkapp_3.models import Client, Product, Order


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    logger.info('Index page accessed')
    return HttpResponse("About us")

#
# def get_clients(request):
#     clients = Client.objects.all()
#     context = {
#         'clients': clients
#     }
#     return render(request, 'homeworkapp_3/client_list.html', context=context)
#
# def clients_orders(request, client_id):
#     client = Client.objects.get(pk=client_id)
#     orders = Order.objects.filter(customer=client_id)
#     context ={
#         'client': client,
#         'orders': orders
#     }
#     return render(request, 'homeworkapp_3/clients_orders.html', context=context)

def clients_orders_day(request, client_id):
    #COUNT_DAYS = 7
    #COUNT_DAYS = 30
    COUNT_DAYS = 365
    start = datetime.date.today() - datetime.timedelta(days=COUNT_DAYS)
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(customer=client_id, date_ordered__gte=start)
    context ={
        'count_days': COUNT_DAYS,
        'client': client,
        'orders': orders
    }
    return render(request, 'homeworkapp_3/client_order.html', context=context)


# def order_full(request, order_id):
#     order = get_object_or_404(Order, pk=order_id)
#     context = {
#         'order': order
#     }
#     return render(request, 'homeworkapp_3/order_full.html', context=context)
