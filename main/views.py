from django.shortcuts import render
from .models import ShopCard

# Create your views here.
def index(request):
   return render(request, 'main/pages/index.html')
def shop(request):
   post = ShopCard.objects.all()
   return render(request, 'shop/shop.html', context={'posts': post})
