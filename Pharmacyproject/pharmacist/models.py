
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pharamcist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pharmacy_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_no= models.CharField(max_length=200, null=True, blank=True)
    license_number = models.CharField(max_length=200, null=True, blank=True)
    company_pic= models.ImageField(upload_to="products")
    joined_on = models.DateTimeField(auto_now_add=True)
    

    def str(self):
        return self.full_name