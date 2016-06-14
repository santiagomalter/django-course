from django.shortcuts import render, HttpResponse
from models import Product
import requests

def home(request):
    return render(request, 'app/home.html', context = {})

def products(request):
    data = {}
    data['products'] = Product.objects.all()
    return render(request, 'app/products.html', context = data)

def ipn(request):
    response = request.POST

    response['cmd'] = '_notify-validate'

    request = requests.post('https://www.sandbox.paypal.com/cgi-bin/webscr', response)

    if request.text == "VERIFIED":
        print 'Transaction is verified by PayPal'

    return HttpResponse('', status_code=200)
