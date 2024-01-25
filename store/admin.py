from django.contrib import admin
from .models import Product, Variation

class ProductAdmin(admin.ModelAdmin):
    list_display        = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available') # this fields on the front page of admin(Product)
    prepopulated_fields = {'slug' : ('product_name',)} # autopopulated the field means product_name madhe je kahi lihinar te slug madhe type hoil

class VariationAdmin(admin.ModelAdmin):
    list_display  = ('product', 'variation_category', 'variation_value', 'is_active') # this filed on the front page of the admin(Variations)
    list_editable = ('is_active',)      # is_active editable zala pahije mhnun means product clickable kru
    list_filter   = ('product', 'variation_category', 'variation_value') # right side la FILTER box yeil -- tyat kay kay dakhvyache aahe te sgd
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)