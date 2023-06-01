from django.shortcuts import render

from django.shortcuts import redirect, render
from Client.models import Product
from pharmacist import service
from django.views.generic import CreateView,FormView
from pharmacist.forms import PharmacistRegistrationForm,PharmacistLoginForm
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate



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
            return self.success_url
def product_list(request):
    product = Product.objects.all()
    data = {
        'product':product,
    }
    return render(request,'pharmacist/list.html',data)
   

def product_create(request):
    data={
        
        'category':service.productCategory(request)
    }
    return render(request,'pharmacist/form.html',data)


#view for the list view 
def product_store(request):
    service.storeProduct(request)
    return redirect('vendor.list')

#view for the edit the registration from
def product_edit(request,id):
    vendor=service.getproductId(id)
    
    data = {
        'title'  : 'vendor',
        'vendor':vendor,
        'category':service.productCategory(request)
        
    }
    return render(request,'vendor/form.html',data)


#view for the update vendor registration from
def product_update(request,id):
    service.updateproduct(request, id)
    return redirect('vendor.list')


#view for the delete registration from
def product_delete(request,id):
    service.deleteproduct(id)
    return redirect('vendor.list')