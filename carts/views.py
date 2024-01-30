from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from store.models import Product, Variation
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


def _cart_id(request):      # database madhe save kraych aahe cart_id
    cart = request.session.session_key
    if not cart:
        cart = request.session.create() # session nsel tr create kr
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # get product
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


    is_cart_item_exists = CartItem.objects.filter(product=product).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product)
        ex_var_list = []
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(item.id)

        if product_variation in ex_var_list:
            # increase the cart item quantity
            index = ex_var_list.index(product_variation)
            item_id = id[index]
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()

        else:
            item = CartItem.objects.create(product=product, quantity=1)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
                item.save()

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
        tax           = 0
        grand_total   = 0
        cart          = Cart.objects.get(cart_id = _cart_id(request))
        cart_items    = CartItem.objects.filter(cart=cart, is_active=True)
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

    return render(request, 'store/cart.html', context) # store madhe cart.html aahe to access kr

def remove_cart(request, product_id, cart_item_id):  # removre cart vr click kele tr
    cart      = Cart.objects.get(cart_id=_cart_id(request))      # cart
    product   = get_object_or_404(Product, id=product_id)        # product
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id) # cart_item
        if cart_item.quantity > 1:   # cart_item quantity 1 peksha jast asel tr
            cart_item.quantity -= 1  # if aapn "-" vr click kele tr -1 zal pahije
            cart_item.save()         # tyala save kr
        else:
            cart_item.delete()       # 1 peksha kmi asel tr delete kr
    except:
        pass
    return redirect('cart')      # aani cart means home page vr direct neee

def remove_cart_item(request, product_id, cart_item_id):
    cart      = Cart.objects.get(cart_id=_cart_id(request))
    product   = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')