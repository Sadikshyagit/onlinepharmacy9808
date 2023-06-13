from . import views
from .views import *
from django.urls import path
from django.contrib.auth.views import LogoutView

app_name = "Pharmacist"
urlpatterns = [
path("registrer",PharmacistRegistrationView.as_view(), name="pharmacist.registration"),
path("", PharmacistLoginView.as_view(), name="pharmacist.login"),
path('add/',views.product_create, name= 'product.create'),
path('list',views.product_list, name= 'product.list'),
path('store',views.product_store, name= 'product.store'),
path('delete/<int:id>',views.product_delete, name= 'product.delete'),
# path('update/<int:id>/', views.product_update, name='product.update')
path("update/<int:id>/", views.product_edit, name="product.update"),
path('orders/', views.admin_orders, name='admin_orders'),
path("logout/", LogoutView.as_view(next_page="Pharmacist:pharmacist.login"), name="pharmacist.logout"),
path('out_of_stock/', views.out_of_stock, name='out_of_stock'),

]