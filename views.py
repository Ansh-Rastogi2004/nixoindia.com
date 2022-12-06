from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages


class ProductView(View):
 def get(self, request):
  Recta = Product.objects.filter(category='RE')
  Atlanta = Product.objects.filter(category='AT')
  Squaro = Product.objects.filter(category='SQ')
  return render(request, 'app/home.html', {'Recta': Recta, 'Atlanta': Atlanta, 'Squaro': Squaro})


# def product_detail(request):
# return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html',
  {'product': product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def products(request):
 return render(request, 'app/products.html')

class CustomerregistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form': form})

 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations! Successfully Registered.')
   form.save()
  return render(request, 'app/customerregistration.html', {'form': form})

def checkout(request):
 return render(request, 'app/checkout.html')