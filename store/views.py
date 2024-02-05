from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Product, ReviewRating
from .forms import ReviewForm
from category.models import Category
from carts.models import CartItem, Cart
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib import messages
from orders.models import OrderProduct


def store(request, category_slug=None):
    categories = None
    products   = None

    if category_slug  != None:   # if category search keli aani nsli tr 404 yeil
        categories     = get_object_or_404(Category, slug=category_slug)
        products       = Product.objects.filter(category=categories, is_available=True)
        paginator      = Paginator(products, 1)  # http://127.0.0.1:8000/store/shirts/ -- kiti shirts dakhvayche aahe
        page           = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count  = products.count()

    else:   # category asel tr to product deil jo search kela
        products       = Product.objects.all().filter(is_available=True).order_by('id')
        paginator      = Paginator(products, 3)    # paginator kiti dakhvayche aahe web page vr products
        page           = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count  = products.count()

    context = {'products' : paged_products, 'product_count' : product_count}
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug): # single product detail
    try:             # single product krt aahe mhnun get(category name, product name)
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart        = CartItem.objects.filter(cart__cart_id = _cart_id(request), product=single_product).exists() # CartItem mdhla cart chi id access krt aaho
    except Exception as e:                                                                   # if this query have any objects then True means we are not going to add to cart button
        raise e
    
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None
    
    # Get the reviews
    reviews =ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
        "single_product" : single_product, 
        "in_cart" : in_cart, 
        'orderproduct' : orderproduct,
        'reviews' : reviews,
        }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET :   # first checking this GET request having this 'keyword' or not
        keyword = request.GET['keyword'] # if that's true then we are storing this 'keyword' in keyword variable
        if keyword:
            products      = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()                            # icontains means looking for whole descriptions
    context = {'products' : products, "product_count" : product_count}  # product count sangel kiti aahe tr Items madhe 
    return render(request, 'store/store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER') # store the previous url means update kela review tr to tyat page vr neil
    if request.method == "POST":
        try:                                  # Account madhla user chi id, Product chi id
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form    = ReviewForm(request.POST, instance=reviews) # if we already have review then update that review
            form.save()
            messages.success(request, 'Thank You...! Your Review Has Been Updated')
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject    = form.cleaned_data['subject'] # models madhla subject through product_detail.html madhla subject
                data.rating     = form.cleaned_data['rating']  # models madhla rating through product_detail.html madhla rating
                data.review     = form.cleaned_data['review']  # models madhla review through product_detail.html madhla review
                data.ip         = request.META.get('REMOTE_ADDR') # store the ip address
                data.product_id = product_id
                data.user_id    = request.user.id
                data.save()
                messages.success(request, 'Thank You...! Your Review Has Been Submitted.')
                return redirect(url) # 54 line madhla url