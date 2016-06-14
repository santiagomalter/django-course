from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^products$', views.products, name="products"),

    # For Paypal
    url(r'^ipn$', views.ipn, name="ipn"),
]
