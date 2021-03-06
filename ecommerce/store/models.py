from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Customer(models.Model):
    user=models.OneToOneField(User ,blank=True ,null=True, on_delete=CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    image=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name
        
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_item(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total

class Orderitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property 
    def get_total(self): 
        total=self.product.price*self.quantity
        return total

