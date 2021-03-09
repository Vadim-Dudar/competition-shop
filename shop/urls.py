from django.urls import path
from . import views

from .models import ShopCard

from django.conf import settings
from django.conf.urls.static import static

posts = ShopCard.objects.all()
urlpatterns = [
  path('', views.index, name = 'index' ),
  path('shop', views.shop, name = 'shop' ),
  path('cart', views.cart_produckt, name = 'cart_produckt'),
  path('<str:slug>', views.cart_produckt, name = '555' )
]
  
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)