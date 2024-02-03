from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from .forms import OrderForm
from .models import Order, Payment
import datetime
from django.http import HttpResponse
import json


def payments(request):
    body = json.loads(request.body)
    order = Order.objects.get(user=request.user, is_ordered=False, order_number = body['orderID'])

    # Store transaction details inside payment mode
    payment = Payment(
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount_paid = order.order_total,
        status = body['status'],
    )
    payment.save()
    order.payment = payment  # inside order model we have payment so this is the order.payment object
    order.is_ordered = True  # means this order is successfull
    order.save()
    return render(request, 'orders/payments.html')


def place_order(request, total=0, quantity=0,):
    current_user = request.user

    # IF THE CART COUNT IS LESS THAN OR EQUAL TO ZERO THEN REDIRECT BACK TO SHOP
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()  # cartitem cha product che count
    if cart_count <= 0:              # jr cart madhe ek pn product nsla tr tyala direct store vala pagevr nee
        return redirect('store')
    
    grand_total = 0
    tax         = 0
    for cart_item in cart_items:
        total    += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total)/100
    grand_total = total + tax
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing information inside order table
            data = Order()
            data.user = current_user
            data.first_name     = form.cleaned_data['first_name'] # attribute aahe --  dict dete -- clean krun dete -- 1000 words aahe tr to ek word sodhun deto
            data.last_name      = form.cleaned_data['last_name']
            data.phone          = form.cleaned_data['phone']
            data.email          = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country        = form.cleaned_data['country']
            data.state          = form.cleaned_data['state']
            data.city           = form.cleaned_data['city']
            data.order_note     = form.cleaned_data['order_note']
            data.order_total    = grand_total
            data.tax            = tax
            data.ip             = request.META.get('REMOTE_ADDR') # ADDR give u the user ip
            data.save()

            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d  = datetime.date(yr, dt, mt)
            current_date = d.strftime("%Y%m%d") #20240202
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order' : order,
                'cart_items' : cart_items,
                'total' : total,
                'tax' : tax,
                'grand_total' : grand_total,
            }
            return render(request, 'orders/payments.html', context)

    else:
        return redirect('checkout')



