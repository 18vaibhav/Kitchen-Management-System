from django.contrib import admin
from .models import *

admin.site.register(Customer)
# admin.site.register(Product)

# admin.site.register(Order)
# admin.site.register(Orderitem)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price','image']


class OrderItemInline(admin.TabularInline):
    model = Orderitem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer','date_ordered','complete','transaction_id']
    # list_filter = ['paid', 'created', 'updated']

    inlines = [OrderItemInline]