from django.shortcuts import render
import datetime
from .forms import SubscriberForm
from products.models import Product
from products.models import ProductImage

def landing(request):
    name="myname"
    currentday= datetime.datetime.now()
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data= form.cleaned_data
        print (data["name"])

        new_form =form.save()

    return render(request, "landing/landing.html", locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True,is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, "landing/home.html", locals())