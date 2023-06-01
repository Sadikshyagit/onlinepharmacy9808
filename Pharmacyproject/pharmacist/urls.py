from . import views
from .views import *
from django.urls import path

app_name = "Pharmacist"
urlpatterns = [
path("registrer",PharmacistRegistrationView.as_view(), name="pharmacist.registration"),
path("", PharmacistLoginView.as_view(), name="pharmacist.login"),
path('add/',views.product_create, name= 'product.create'),
path('list',views.product_list, name= 'product.list'),
path('store',views.product_store, name= 'product.store'),
]