from Client.models import Category, Product

def productCategory(request):
    category=Category.objects.all()
    return category

def storeProduct(request):
    view_count = request.POST.get('view_count', 0)
    product=Product(
        category=Category.objects.get(pk=request.POST['category']),
        title=request.POST['title'],
        slug=request.POST.get('slug',False),
        image=request.FILES.get('image',False),
        marked_price=request.POST.get('marked_price',0),
        selling_price=request.POST.get('selling_price',),
        description=request.POST.get('description',False),
        manufacture_date =request.POST.get('manufacture_date'),
        expiry_date =request.POST.get('expiry_date'),
        hex =request.POST.get('hex'),
        # view_count=request.POST.get('view_count'),
        view_count=view_count,
    )
    product.save()
    return "sucess" 

# pharmacist/service.py

def create_product(request):
    # Process the submitted form data and create a new product
    product = Product()
    product.title = request.POST['title']
    product.category = Category.objects.get(pk=request.POST['category'])
    product.slug = request.POST['slug']
    product.image = request.FILES.get('image', False)
    product.marked_price = request.POST['marked_price']
    product.selling_price = request.POST['selling_price']
    product.description = request.POST['description']
    product.manufacture_date = request.POST['manufacture_date']
    product.expiry_date = request.POST['expiry_date']
    product.hex = request.POST['hex']
    product.view_count = request.POST.get('view_count', 0)  # Assuming view_count is an optional field
    product.save()  # Save the new product to the database



def getproduct():
    product=Product.objects.values().all()
    return list(product)


def getproductId(id):
    product=Product.objects.get(id=id)
    return product

# def updateproduct(request,id):
#     print("updateproduct function called with id:", id)
#     product=Product.objects.get(id =id)
#     product.title=request.POST['title']
#     product.category =Category.objects.get(pk=request.POST['category'])
#     product.slug=request.POST['title']
#     product.image=request.FILES['image']
#     product.marked_price=request.POST['marked_price']
#     product.selling_price=request.POST['selling_price']
#     product.description=request.POST['description']
#     # product.warranty=request.POST['warranty']
#     # product.return_policy=request.POST['return_policy']
#     product.view_count=request.POST['view_count']
#     product.save()
#     return



def updateproduct(request, id):
    product = getproductId(id)  # Retrieve the existing product from the database
    product.title = request.POST['title']
    product.category = Category.objects.get(pk=request.POST['category'])
    product.slug = request.POST['slug']
    product.image = request.FILES.get('image', False)
    product.marked_price = request.POST['marked_price']
    product.selling_price = request.POST['selling_price']
    product.description = request.POST['description']
    product.manufacture_date = request.POST['manufacture_date']
    product.expiry_date = request.POST['expiry_date']
    product.hex = request.POST['hex']
    
    # Handle 'view_count' field if it exists in the request
    if 'view_count' in request.POST:
        product.view_count = request.POST['view_count']
    
    product.save()  # Save the updated product to the database



def deleteproduct(id):
    product=Product.objects.get(id=id)
    product.delete()
    return "success"

def getproductbyid(id):
    try:
        product = Product.objects.get(id=id)
        return product
    except Product.DoesNotExist:
        return None