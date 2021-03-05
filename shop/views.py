from django.shortcuts import render
from .models import ShopCard
from django.conf import settings

# Create your views here.
def index(request):
   post = ShopCard.objects.all()[:3]
   return render(request, 'main/pages/index.html', context={'posts': post})
def shop(request):
   post = ShopCard.objects.all()
   return render(request, 'shop/shop.html', context={'posts': post})
def cart_produckt(request):
   post = ShopCard.objects.all()
   return render(request, 'shop/cart_produckt.html', context={'posts': post})