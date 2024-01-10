from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug          = models.SlugField(max_length=100, unique=True) # slug sarkh aal pahije
    descriptions  = models.TextField(max_length=255, blank=True)
    cat_image     = models.ImageField(upload_to='photos/categories', blank=True)    # we use image so we have to install pillow

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def get_url(self): # get url of perticular category
        return reverse('products_by_category', args=[self.slug]) # means category slug