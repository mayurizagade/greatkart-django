from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

# def home(request):
#     return HttpResponse("HomePage")

def home(request):
    products = Product.objects.all().filter(is_available=True)  # add kru products web page vr
    context = {'products' : products}
    return render(request, "home.html", context)