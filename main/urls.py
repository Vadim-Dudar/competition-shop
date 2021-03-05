from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name = 'index' ),
  path('main/shop', views.shop, name = 'shop' ),
]