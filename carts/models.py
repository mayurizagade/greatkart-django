from django.db import models
from store.models import Product, Variation

class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id  # return cart_id as object
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True) # may product have same variations so in that perticular situations we have to use manytomany filed
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product     # return product as object
    
    def sub_total(self):
        return self.product.price * self.quantity  
    # --> self means CartItem     | self means CartItem
    # --> product means model     | quantity means CartItem cha andercha quantity
    # --> price means Product model cha andercha price