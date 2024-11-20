from django.urls import path
from . import views



urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('product/<uuid:id>/', views.ProductPage.as_view(), name='product'),
    path('basket/', views.BasketPage.as_view(), name='basket'),
]