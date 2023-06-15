from django.shortcuts import render
from django.shortcuts import redirect, render
from Client.models import Product, Category
from pharmacist import service
from django.views.generic import CreateView,FormView
from pharmacist.forms import PharmacistRegistrationForm,PharmacistLoginForm
from .models import *
from pharmacist.service import create_product
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
from django.urls import reverse


class PharmacistLoginView(FormView):
    template_name = "Pharmacistlogin.html"
    form_class = PharmacistLoginForm
    success_url = reverse_lazy("Pharmacist:product.list")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Pharamcist.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url


class PharmacistRegistrationView(CreateView):
    template_name = "Pharmacyregistration.html"
    form_class = PharmacistRegistrationForm
    success_url = reverse_lazy("Pharmacist:product.list")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return reverse("Pharmacist:pharmacist.login")
        
def product_list(request):
    product = Product.objects.all()
    data = {
        'product':product,
    }
    return render(request,'pharmacist/list.html',data)
   

# def product_create(request):
#     data={
        
#         'category':service.productCategory(request)
#     }
#     return render(request,'pharmacist/add.html',data)

def product_create(request):
    if request.method == 'POST':
        create_product(request)
        return redirect('Pharmacist:product.list')
    else:
        category = Category.objects.all()
        context = {'category': category}
        return render(request, 'pharmacist/add.html', context)

#view for the list view 
def product_store(request):
    service.storeProduct(request)
    return redirect('Pharmacist:product.list')

# #view for the edit the registration from
# def product_edit(request,id):
#     vendor=service.getproductId(id)
#     data = {
#         'title'  : 'vendor',
#         'vendor':vendor,
#         'category':service.productCategory(request)  
#     }
#     return render(request,'vendor/form.html',data) category

def product_edit(request, id):
    if request.method == 'POST':
        service.updateproduct(request, id)
        return redirect('Pharmacist:product.list')
    else:
        product = service.getproductId(id)
        category = Category.objects.all()
        context = {'product': product, 'category': category}
        return render(request, 'pharmacist/form.html', context)


def product_update(request, id):
    if request.method == 'POST':
        service.updateproduct(request, id)
        return redirect('Pharmacist:product.list')
    else:
        product = Product.objects.get(id=id)(id)
        categories = service.getallcategories()
        return render(request, 'form.html', {'product': product, 'category': categories})


#view for the delete registration from
def product_delete(request,id):
    service.deleteproduct(id)
    return redirect('Pharmacist:product.list')

from Client.models import Order

def admin_orders(request):
    orders = Order.objects.all()
    return render(request, 'pharmacist/orders.html', {'orders': orders})

def pharmacist_logout(request):
    logout(request)
    return redirect('Pharmacist:pharmacist.login')

from django.shortcuts import render
from django.views.generic import TemplateView
from Client.models import Product

class OutOfStockView(TemplateView):
    template_name = 'pharmacist/out_of_stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve out-of-stock products
        out_of_stock_products = Product.objects.filter(hex=0)
        context['out_of_stock_products'] = out_of_stock_products
        return context

