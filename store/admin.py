from django.contrib import admin

# Register your models here.
from store.models import Customer
from store.models import Product
from store.models import Order
from store.models import OrderItem
from store.models import ShippingAddress

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)