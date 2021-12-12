from django.contrib import admin
from .models import *


admin.site.register(
    [Admin, Customer, Category, Product, Cart, CartProduct, ProductImage])


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'payment_completed')
    search_fields = ('cart', 'id',)
