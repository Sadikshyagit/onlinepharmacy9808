from Client.models import Category, Product


def productCategory(request):
    category=Category.objects.all()
    return category

def storeProduct(request):
    product=Product(
        category    =Category.objects.get(pk=request.POST['category']),
        title=request.POST.get('title',False),
        slug=request.POST.get('slug',False),
        image=request.FILES.get('image',False),
        marked_price=request.POST.get('marked_price',False),
        selling_price=request.POST.get('selling_price',False),
        description=request.POST.get('description',False),
        manufacture_date =request.POST.get('manufacture_date',False),
        expiry_date =request.POST.get('expiry_date',False),
        hex =request.POST.get('hex',False),
        view_count=request.POST.get('view_count',False),
  
    )
    print(product)
    product.save()
    return "success"


def getproduct():
    product=Product.objects.values().all()
    return list(product)


def getproductId(id):
    product=Product.objects.get(id=id)
    return product

def updateproduct(request,id):
    product=Product.objects.get(id =id)
    product.title=request.POST['title']
    product.category    =Category.objects.get(pk=request.POST['category'])
    product.slug=request.POST['title']
    product.image=request.FILES['image']
    product.marked_price=request.POST['marked_price']
    product.selling_price=request.POST['selling_price']
    product.description=request.POST['description']
    # product.warranty=request.POST['warranty']
    # product.return_policy=request.POST['return_policy']
    product.view_count=request.POST['view_count']
    product.save()
    return


def deleteproduct(id):
    product=Product.objects.get(id=id)
    product.delete()
    return "success"