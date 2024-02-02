from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from store.models import Product, Variation
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def _cart_id(request):      # database madhe save kraych aahe cart_id
    cart = request.session.session_key
    if not cart:
        cart = request.session.create() # session nsel tr create kr
    return cart


def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)  # get product

    # -- IF THE USER IS AUTHETICATED --
    if current_user.is_authenticated:
        product_variation = []          # --- WE ARE GETTING PRODUCT VARIATION ---
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass

        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists() # we are checking cartitem exists or not
        if is_cart_item_exists:  # if yes cartitem is exists
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            ex_var_list = []  # we getting existing variations list from the database
            id = []           # id of that perticular item
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)

            if product_variation in ex_var_list:    # we are checking the product variation that we are adding is exists or not
                # increase the cart item quantity   # if it's exists then increasing the cart_item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]  # we are getting the item_id
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            # if product not exists in cart then create new product and quantity will be 1
            else:
                item = CartItem.objects.create(product=product, quantity=1, user=current_user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                # cart_item.quantity += 1  # cart_item.quantity = cart_item.quantity + 1 -- means increament hot rahil click kele tr
                item.save()
        else :   # else cart_item exist nsel krt tr new create kr
            cart_item    = CartItem.objects.create(
                product  = product,
                quantity = 1,
                user     = current_user,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        # return HttpResponse(cart_item.quantity) # quantity dakhvel web pagevr
        # exit()
        return redirect('cart')

    # -- IF THE USER IS NOT AUTHENTICATED --
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass

        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))  # get the cart using the cart_id present in the session
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists() # we are checking cartitem exists or not
        if is_cart_item_exists:  # if yes cartitem is exists
            cart_item = CartItem.objects.filter(product=product, cart=cart)
            ex_var_list = []  # we getting existing variations list from the database
            id = []           # id of that perticular item
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            print(ex_var_list)

            if product_variation in ex_var_list:    # we are checking the product variation that we are adding is exists or not
                # increase the cart item quantity   # if it's exists then increasing the cart_item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]  # we are getting the item_id
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            # if product not exists in cart then create new product and quantity will be 1
            else:
                item = CartItem.objects.create(product=product, quantity=1, cart=cart)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                # cart_item.quantity += 1  # cart_item.quantity = cart_item.quantity + 1 -- means increament hot rahil click kele tr
                item.save()
        else :   # else cart_item exist nsel krt tr new create kr
            cart_item    = CartItem.objects.create(
                product  = product,
                quantity = 1,
                cart     = cart,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        # return HttpResponse(cart_item.quantity) # quantity dakhvel web pagevr
        # exit()
        return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax            = 0
        grand_total    = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user = request.user, is_active=True) # for login user
        else:
            cart           = Cart.objects.get(cart_id = _cart_id(request)) # for not logged in user
            cart_items     = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total     += (cart_item.product.price * cart_item.quantity)  # price * quantity
            quantity  += cart_item.quantity                              # quantity + quantity
        tax = (2 * total)/100         # tax kiti lavaycha aahe te
        grand_total    = total + tax   # total paise + tax = all total
    except ObjectDoesNotExist :
        pass  # just ignore

    context = {'total'       : total, 
               'quantity'    : quantity, 
               'cart_items'  : cart_items, 
               'tax'         : tax, 
               'grand_total' : grand_total}

    return render(request, 'store/cart.html', context) # store madhe cart.html aahe to access kr

def remove_cart(request, product_id, cart_item_id):  # removre cart vr click kele tr
    product   = get_object_or_404(Product, id=product_id)        # product
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)

        else:   # agr aapn logged in nahi rahilo tr
            cart      = Cart.objects.get(cart_id=_cart_id(request))                       # cart 
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id) # cart_item

        if cart_item.quantity > 1:   # cart_item quantity 1 peksha jast asel tr
            cart_item.quantity -= 1  # if aapn "-" vr click kele tr -1 zal pahije
            cart_item.save()         # tyala save kr
        else:
            cart_item.delete()       # 1 peksha kmi asel tr delete kr
    except:
        pass
    return redirect('cart')          # aani cart means home page vr direct neee

def remove_cart_item(request, product_id, cart_item_id):
    product   = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:  # logged in asel tr item cart madhe add kr
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)

    else:   # looged in nsel tr id get kr aani item cart madhe add kr
        cart      = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax           = 0
        grand_total   = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user = request.user, is_active=True) # for login user
        else:
            cart           = Cart.objects.get(cart_id = _cart_id(request))            # for not logged in user
            cart_items     = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total    += (cart_item.product.price * cart_item.quantity)  # price * quantity
            quantity += cart_item.quantity                              # quantity + quantity
        tax = (2 * total)/100         # tax kiti lavaycha aahe te
        grand_total   = total + tax   # total paise + tax = all total
    except ObjectDoesNotExist :
        pass  # just ignore

    context = {'total'       : total, 
               'quantity'    : quantity, 
               'cart_items'  : cart_items, 
               'tax'         : tax, 
               'grand_total' : grand_total}

    return render(request, 'store/checkout.html', context) # store madhe cart.html aahe to access kr

