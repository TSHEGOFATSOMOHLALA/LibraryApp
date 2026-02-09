from django.contrib import admin
from .models import  Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'created_date')
    list_filter = ('category', 'in_stock')
    search_fields =('name','description')

admin.site.register(Product, ProductAdmin)