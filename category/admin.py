from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)} # autopopulated the field means category_name madhe je kahi lihinar te slug madhe type hoil
    list_display = ('category_name', 'slug') # this fields on the front page of admin(category)
    
admin.site.register(Category, CategoryAdmin)