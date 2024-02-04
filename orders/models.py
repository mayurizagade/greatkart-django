from django.db import models
from accounts.models import Account
from store.models import Product, Variation

# A]     <<<<<<<<<<<<<<=========================== PAYMENT ===========================>>>>>>>>>>>>>> 

class Payment(models.Model):
    user           = models.ForeignKey(Account, on_delete=models.CASCADE) # we need Account detail in Payment
    payment_id     = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid    = models.CharField(max_length=100)
    status         = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id
    

# B]     <<<<<<<<<<<<<<=========================== ORDER ===========================>>>>>>>>>>>>>> 
    
class Order(models.Model):
    STATUS = (
        ("New", "New"),
        ("Accepted", "Accepted"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )
    
    user           = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True) # we need account detail
    payment        = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True) # and payment detail
    order_number   = models.CharField(max_length=50)
    first_name     = models.CharField(max_length=50)
    last_name      = models.CharField(max_length=50)
    phone          = models.CharField(max_length=15)
    email          = models.EmailField(max_length=50)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    country        = models.CharField(max_length=50)
    state          = models.CharField(max_length=50)
    city           = models.CharField(max_length=50)
    order_note     = models.CharField(max_length=100, blank=True)
    order_total    = models.FloatField()
    tax            = models.FloatField()
    status         = models.CharField(max_length=10, choices=STATUS, default="New")
    ip             = models.CharField(max_length=20, blank=True)
    is_ordered     = models.BooleanField(default=False)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def full_name(self):    # we are concanitate first_name and last_name
        return f"{self.first_name} {self.last_name}"  # Mayuri Zagade
    
    def full_address(self): # we are concanitate address_1 and address_2
        return f"{self.address_line_1} {self.address_line_2}"

    def __str__(self):
        return self.first_name


# B]     <<<<<<<<<<<<<<========================= ORDER PRODUCT =========================>>>>>>>>>>>>>> 

class OrderProduct(models.Model):
    order         = models.ForeignKey(Order, on_delete=models.CASCADE)         # i want order detail
    payment       = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True) # i want payment detail
    user          = models.ForeignKey(Account, on_delete=models.CASCADE)        # i want user detail
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)        # i want product detail
    variations    = models.ManyToManyField(Variation, blank=True)               # i want variations detail
    quantity      = models.IntegerField()
    product_price = models.FloatField()
    ordered       = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name