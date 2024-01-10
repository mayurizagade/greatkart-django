from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available') # this fields on the front page of admin(Product)
    prepopulated_fields = {'slug' : ('product_name',)} # autopopulated the field means product_name madhe je kahi lihinar te slug madhe type hoil

admin.site.register(Product, ProductAdmin)