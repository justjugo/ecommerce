from django.shortcuts import render
from products.models import  Product
# Create your views here.

def index(request):
        products=Product.objects.all()
        fruits=Product.objects.filter(category__name="Fruits")
        vegetables=Product.objects.filter(category__name="Vegetables")
        return render(request,'app/index.html',{'products':products,'fruits':fruits ,'vegetables':vegetables });


def about(request):
       
        return render(request,'app/about.html',{})  

def contact(request):
        return render (request,'app/contact.html',{})

