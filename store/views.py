from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Product
from category.models import Category
from carts.models import CartItem, Cart
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:   # if category search keli aani nsli tr 404 yeil
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)  # http://127.0.0.1:8000/store/shirts/ -- kiti shirts dakhvayche aahe
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    else:   # category asel tr to product deil jo search kela
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)    # paginator kiti dakhvayche aahe web page vr products
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {'products' : paged_products, 'product_count' : product_count}
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug): # single product detail
    try:             # single product krt aahe mhnun get(category name, product name)
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product=single_product).exists() # CartItem mdhla cart chi id access krt aaho
    except Exception as e:                                                                   # if this query have any objects then True means we are not going to add to cart button
        raise e
    context = {"single_product" : single_product, "in_cart" : in_cart}
    return render(request, 'store/product_detail.html', context)

def search(request):
    if 'keyword' in request.GET :   # first checking this GET request having this 'keyword' or not
        keyword = request.GET['keyword'] # if that's true then we are storing this 'keyword' in keyword variable
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()                            # icontains means looking for whole descriptions
    context = {'products' : products, "product_count" : product_count}  # product count sangel kiti aahe tr Items madhe 
    return render(request, 'store/store.html', context)