from django.shortcuts import render, HttpResponse
from models import Product
import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'app/home.html', context = {})

def products(request):
    data = {}
    data['products'] = Product.objects.all()
    return render(request, 'app/products.html', context = data)

@csrf_exempt
def ipn(request):
    response = request.POST.dict()

    print response

    response['cmd'] = '_notify-validate'

    request = requests.post('https://www.sandbox.paypal.com/cgi-bin/webscr', response)

    print request.text

    if request.text == "VERIFIED":
        print 'Transaction is verified by PayPal'

    return HttpResponse('ok', status=200)
