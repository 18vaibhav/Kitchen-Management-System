from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.http import JsonResponse
from .forms import ProductForm
import json
from django.urls import reverse_lazy
from . utils import cookiecart
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def store(request):
    if request.user.is_authenticated: 
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartitem=order.get_cart_item
    else:
        cookiedata=cookiecart(request)
        cartitem=cookiedata['cartitem']
        
    products=Product.objects.all()
    context={'products':products,'cartitem':cartitem}
    return render(request , 'store/store.html' , context)

def cart(request):
    if request.user.is_authenticated: 
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartitem=order.get_cart_item
    else:
        cookiedata=cookiecart(request)
        cartitem=cookiedata['cartitem']
        order=cookiedata['order']
        items=cookiedata['items']
    context={'items':items ,'order':order,'cartitem':cartitem}
    return render(request , 'store/cart.html' , context)

def checkout(request):
    if request.user.is_authenticated: 
        customer=request.user.customer
        order, created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartitem=order.get_cart_item
    else:
        cookiedata=cookiecart(request)
        cartitem=cookiedata['cartitem']
        order=cookiedata['order']
        items=cookiedata['items']
    context={'items':items ,'order':order,'cartitem':cartitem}
    return render(request , 'store/checkout.html' , context)

def updateitem(request):
    data  =  json.loads(request.body)
    productid=data['productid']
    action=data['action']
    print(productid)
    customer=request.user.customer
    product=Product.objects.get(id=productid )
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderitem,created=Orderitem.objects.get_or_create(order=order,product=product)
    if(action=='Add'):
        orderitem.quantity=(orderitem.quantity+1)
    elif(action=='remove'):
        orderitem.quantity=(orderitem.quantity-1)
    
    orderitem.save()
    if(orderitem.quantity<=0):
        orderitem.delete()
    return JsonResponse('item is added',safe=False)


def product_create(request):
    context = {}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            price = form.cleaned_data.get("price")
            image = form.cleaned_data.get("image")
            obj = Product.objects.create(
                name = name,
                price = price,
                image = image
            )
            obj.save()
            return redirect('store')
    else:
        form = ProductForm()

    context['form'] = form
    return render(request, "store/add_product.html",context)

# def delete_product(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
 
#     # fetch the object related to passed id
#     obj = get_object_or_404(Product, id = id)
 
 
#     if request.method =="POST":
#         # delete object
#         obj.delete()
#         # after deleting redirect to
#         # home page
#         return redirect("store")
 
#     return render(request, "delete_product.html", context)

class ProductDeleteView(DeleteView):
    model = Product
    def get_queryset(self):
        return super().get_queryset()
    # fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('store')
    template_name = 'store/delete_product.html'