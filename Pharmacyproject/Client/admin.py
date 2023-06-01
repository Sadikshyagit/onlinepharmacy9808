from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(
    [Admin, Customer, Category, Product, Cart, CartProduct, Order, ProductImage])