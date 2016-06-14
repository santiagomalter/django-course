from django.shortcuts import render, HttpResponse
from models import Product, Order
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
    """
    {u'payer_status': u'verified', u'payment_type': u'instant', u'first_name': u'test', u'last_name': u'buyer', u'payer_email': u'santiago.malter-buyer@gmail.com', u'notify_version': u'3.8', u'verify_sign': u'AWHOXWDJQ5vZGrZYnTL9kMA9c5cLAsuVU5wWgN.q6bG7.pYJjAs6HGsA', u'mc_gross': u'5.00', u'address_country': u'Belgium', u'payment_status': u'Completed', u'mc_fee': u'0.52', u'ipn_track_id': u'5f338b1312001', u'address_zip': u'4800', u'item_name': u'Product One', u'txn_id': u'5CL243856K976511B', u'business': u'santiago.malter-facilitator@gmail.com', u'payment_gross': u'', u'payment_fee': u'', u'protection_eligibility': u'Eligible', u'address_street': u'Rue du Cornet 6', u'payment_date': u'07:37:28 Jun 14, 2016 PDT', u'address_country_code': u'BE', u'quantity': u'1', u'custom': u'', u'transaction_subject': u'', u'receiver_email': u'santiago.malter-facilitator@gmail.com', u'mc_currency': u'EUR', u'test_ipn': u'1', u'item_number': u'', u'shipping': u'0.00', u'address_status': u'unconfirmed', u'residence_country': u'BE', u'receiver_id': u'PK2YS5QZ3YQ9W', u'payer_id': u'BQKDCTPL2GDL8', u'txn_type': u'web_accept', u'address_state': u'', u'tax': u'0.00', u'handling_amount': u'0.00', u'address_name': u'test buyer', u'address_city': u'Verviers', u'charset': u'windows-1252'}
    """
    response = request.POST.dict()

    # Append parameter to ask validation from PayPal
    response['cmd'] = '_notify-validate'

    # Repost for validation
    request = requests.post('https://www.sandbox.paypal.com/cgi-bin/webscr', response)

    # Check validity
    if request.text == "VERIFIED":
        print 'Transaction is verified by PayPal'

        # Create order in Database
        Order.objects.create(product=Product.objects.get(pk=response['item_number'], status="paid"))

    return HttpResponse('ok', status=200)
