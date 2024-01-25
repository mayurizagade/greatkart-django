#                         <<<<<<<<<<<---------- CUSTOM USER MODEL ---------->>>>>>>>>>>

# I want Email in admin
# delete old migrations files 0001 etc
# delete old database 'db.sqlite3'
# create app for custom user model
# register in settings.py
# create models
# register in admin.py
# AUTH_USER_MODEL = 'accounts.Account' # we need to tell user that we are going to use custom user
                #  'appname.modelname'

# makemigrations and migarte
# createsuperuser
# $ winpty python manage.py createsuperuser
# Email: admin@gmail.com
# Username: admin
# First name: Mayuri
# Last name: Zagade
# Password: Python@123
# Password (again): Python@123
# py manage.py runserver -- open in google and see admin panel madhe email aal

# --------------------------------------------------

# PASSWORD dist aahe admin panel madhe :-
# admin.py madhe changes kele accounts valya

# --------------------------------------------------

# ADD IMAGES from Admin:-
# settings.py -- MEDIA_URL = 'media/'
#                MEDIA_ROOT = BASE_DIR /'media'
# urls.py -- from django.conf.urls.static import static
#            from django.conf import settings
#  after urlpatterns[] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# --------------------------------------------------

# Download img from sir video(or anywhere)
# Go to admin panel and add category with images

# --------------------------------------------------

# I WANT SLUG :- means category madhe lihile tr slug madhe pn lihun aal pahije
# models madhe slugfileds tak slug mdhe
# makemigrations and migrate
# admin.py :- category vala -- class create kr

# =============================================================================================================

#   PRODUCT MANAGER :- store
# create store app in GIT :- py manage.py startapp store
# register that app in settings
# create Product model in models.py of store
# register that model in admin.py of store
# In GIT :- makemigations and migrate and runserver
# Google :- open --- http://127.0.0.1:8000/admin/
#                    Add Products
#                    
# --------------------------------------------------

# NOW WE HAVE TO ADD ON OUR WEBSITE :-
# Open --- http://127.0.0.1:8000/
# greatkart -- Project cha views madhe aapn Purn products add kru
# home.html changes --- for loop lavla product.name,price,image deu means web vr disel images,price
# store app madhe urls.py create kru
# store app madhe views create kru
# new template create kru store(folder)
# in that folder create store.html
# http://127.0.0.1:8000/store/shoes/ -- jo product search kru to product deil

# =============================================================================================================

# 5) CONTENT PROCESSESOR AND PRODUCT DETAIL :-

# CATEGORY APP --->

# category app :- create context_processsor.py file 
#                 define menu_links function
# settings.py :- register in TEMPLATES 
#                'category.context_processors.menu_links'
#                 'project_name.file_name.fuction_name'
# navbar.html :- for loop lavla links vala aani category.category_name dil mhnje web cha 
#                navbar madhe je aapn shirts,earings vgere dil aahe te yeil
#                <div class="dropdown-menu"> # all products aale pahije web pages chya navbar vr
#                   <a class="dropdown-item" href="{% url 'store' %}">All Products</a>
#               {% for category in links %}
#                <a class="dropdown-item" href="{{ category.get_url }}">{{ category.category_name }} </a>
#               {% endfor %}
# models.py :- def get_url function for getting all url -- means aapn category madhe shirts,
#              earning etc vr click kele tr tyacha related aale pahije

# WEB PAGE VR SIDE LA CATEGORY AALE PAHIJE :-
# store.html :- <ul class="list-menu">
#               <li><a href="{% url 'store' %}">All Products</a></li> # all products aale pahije
#               {% for category in links %}          yane category names yeil je aapn store kele
#               <li><a href="{{category.get_url}}">{{category.category_name}}</a></li>
#               {% endfor %}   category vr click kelyavr tyacha related aale pahije

# --------------------------------------------------

# I WANT PRODUCT DETAIL IN WEB PAGE :-

# STORE APP --->

# urls.py :- create product_slug url 
# views.py :- define product_detail function
# HTML :- templates -- store -- create product_detail.html 
# models.py :- def get_url function for getting all url -- means aapn product madhe shirts,
#              earning etc vr click kele tr tyacha related aale pahije
# home.html :- {{product.get_url}} tak jo define kela means url taklyavr product bddl yeil 

# --------------------------------------------------

# When I click on store we have to go on home page :-
# navbar.html :- <a href="{% url 'home' %}" class="brand-wrap"> -- brand vr click kele tr home vr nele pahije
#                <a href="{% url 'store' %}" class="btn btn-outline-primary">Store</a>
#                   store vr click kele tr home vr nele pahije
# home.html :- <a href="{% url 'store' %}" class="btn btn-outline-primary float-right">See all</a>
#               See all vr click kele tr home vr nele pahije
# store.html :- <a href="{{ product.get_url }}"> -- product vr click kelyabrobr detail disle pahije
#               <a href="{{ product.get_url }}" class="title">{{product.product_name}}</a>

# --------------------------------------------------

# I WANT TO CHANGE BANNER :-
# select image whatever u want, then add to static/images/banners/cover
# home.html :- <img src="{% static 'images/banners/cover.jpg' %}" class="img-fluid rounded">

# =============================================================================================================

# 6) SETUP GIT AND START CART FUNCTIONALITY :-

# Google :- github.com -- create account in GIT 
#                      -- + click on this sign top on right side -- create New Repository -- give name & create
# Open GITHUB :- git init --> first we have to initialize git repository
#                git add .
#                git commit -m "first" --> "first is msg"
#                git remote add origin https://github.com/mayurizagade/greatkart-django.git
#                git branch -M main
#                git push -u origin main
#                create app :-  py manage.py startapp carts
# settings.py :- register in installed app

# ** CARTS APP ** :-
# create urls.py in app 
# urls.py :- in project urls include app urls
# views.py :- define cart view
# html :- in template/store folder create cart.html file
# GIT :- py manage.py runserver
# Google :- http://127.0.0.1:8000/cart/
# models.py :- Create Cart & CartItem model
# GIT :- py manage.py makemigrations
#        py manage.py migrate 
#        py manage.py runserver
# admin.py :- register Cart, CartItem 
# Google :- admin page :-  http://127.0.0.1:8000/admin/carts/cartitem/

# =============================================================================================================

# 7) ADD TO CART USING SESSION KEYS, INCREMENT/DECREMENT/REMOVE CART ITEMS :-

# ADD TO CART BUTTON :- 

# ** CARTS APP ** :-
# views.py     :- define _cart_id, add_cart, 
# urls.py      :- add_cart
# product.html :- {% url 'add_cart' single_product.id %}
# Google       :- http://127.0.0.1:8000/cart/add_cart/6/

# --------------------------------------------------

# GET TOTAL QUANTITY CART ITEMS :-
# views.py :- defie cart

# --------------------------------------------------

# IMPLEMENT DATA INTO CART PAGE :-
# models.py :- def sub_total(self):
#              return self.product.price * self.quantity  
                # --> self means CartItem | self means CartItem
                # --> product means model | quantity means CartItem cha andercha quantity
                # --> price means Product model cha andercha price

# cart.html :- {% for cart_item in cart_items %} from <tr> to </tr> {% endfor %}
#              <div class="aside"><img src="{{cart_item.product.images.url}}" class="img-sm"></div> -- images
#              <input type="text" class="form-control"  value="{{ cart_item.quantity }}"> <!--quantity-->
#              <a href="{% url 'add_cart' cart_item.product.id %}" class="btn btn-light" type="button" id="button-minus"> <i class="fa fa-plus"></i> </a>
#              <var class="price">{{ cart_item.sub_total }}</var> <!--total price-->
#              <small class="text-muted">{{ cart_item.product.price }} </small> <!--product price-->
#               <dt>Total price:</dt>
#               <dd class="text-right">{{ total }}</dd>

# --------------------------------------------------

# CACULATE TAX GRAND TOTAL :-
# views.py :- tax = (2 * total)/100          # tax kiti lavaycha aahe te
#             grand_total = total + tax      # total paise + tax = all total
#             then add in context dictionary
# cart.html :- <div class="price-wrap"> 
#                <var class="price">₹ {{ cart_item.sub_total }}</var> <!--total price-->
#                <small class="text-muted">₹ {{ cart_item.product.price }} </small> <!--product price-->
#            </div> <!-- price-wrap .// --> 

# --------------------------------------------------

# CART DECREMENT AND REMOVE :-
# views.py :- define remove_cart      -- for single cart -1
#             define remove_cart_item -- for all cart remove
# urls.py :- create urls for 2 -- remove_cart, remove_cart_item
# cart.html :- <a href="{% url 'remove_cart_item' cart_item.product_id %}" class="btn btn-danger"> Remove</a>
#              <a href="{% url 'remove_cart' cart_item.product.id %}" class="btn btn-light" type="button" id="button-plus"> <i class="fa fa-minus"></i> </a>

# =============================================================================================================

# 8) FIXING CART BUGS & CONTEXT PROCESSOR FOR CART ITEM COUNTER :-

# CHECK FOR EMPTY CART :-
# cart.html :- {% if not cart_items %}
#              <h2 class="text-center">Your Shopping Cart Is Empty</h2>  <!--message-->
#              <br>
#              <div class="text-center">
#                 <a href="{% url 'store' %}"class="btn btn-primary">Continue Shopping</a>
#              </div>
#             {% else %}
#              {% endif %}

# --------------------------------------------------

# FIX ADD TO CART LINKS FOR HOMEPAGE :-
# store.html :- <a href="{% url 'add_cart' product.id %}" class="btn btn-block btn-primary">Add to cart </a>
# cart.html :-  <a href="{{ cart_item.product.get_url }}" class="title text-dark">{{cart_item.product.product_name}}</a> <!--images-->

# --------------------------------------------------

# CONTINUE SHOPPING VR CLICK KELE TR AALE PAHIJE :-
# cart.html :- <a href="{% url 'store' %}" class="btn btn-light btn-block">Continue Shopping</a>

# --------------------------------------------------

# CHECK IF THE PRODUCT ADDED TO CART :- 
# product_detail.html :- {% else %}
#                        {% if in_cart %}
#      Added Cart val :- <a href="#" class="btn  btn-success"> <span class="text">Added to Cart</span> <i class="fas fa-check"></i>  </a>
#      View Cart Val :-  <a href="{% url 'cart' %}" class="btn  btn-outline-primary"> <span class="text">View Cart</span> <i class="fas fa-eye"></i>  </a>
#                     {% else %}
#                     <a href="{% url 'add_cart' single_product.id %}" class="btn  btn-primary"> <span class="text">Add to cart</span> <i class="fas fa-shopping-cart"></i>  </a>
#                      {% endif %}

# --------------------------------------------------

# COUNTER FOR CART ICON IN NAVBAR :- bucket vali sign -- means aapn cart madhe je kahi add kele te cart madhe count disla pahije
# CART APP :- create context_processor file in app
#             define counter function
# settings.py :- register that file -- 'carts.context_processor.counter'
# navbar.html :- <a href="{% url 'cart' %}" class="widget-header pl-3 ml-3">
#                <div class="icon icon-sm rounded-circle border"><i class="fa fa-shopping-cart"></i></div>
#                <span class="badge badge-pill badge-danger notify">{{ cart_count }}</span>
#            </a>

# =============================================================================================================

# 9) PAGINATION & SEARCH 

# VIEW DETAILS BUTTON :-
# store.html :- <a href="{{ product.get_url }}" class="btn btn-block btn-primary"> View Details </a>

# --------------------------------------------------

# PAGINATOR PART 1 :- 
# Paginator means kiti product dakhvayche aahe store madhe
# STORE APP :- views.py :- store madhe else madhe paginator variable ghetle

# --------------------------------------------------

# PAGINATOR PART 2:-
# STORE APP :- views.py :- store madhe if madhe paginator variable ghetl
# store.html :-     <nav class="mt-4" aria-label="Page navigation sample">
    #     {% if products.has_other_pages %}
    #   <ul class="pagination">
    #     {% if products.has_previous %}                 <!-- PREVIOUS PAGE -->
    #     <li class="page-item"><a class="page-link" href="?page={{products.previous_page_number}}">Previous</a></li>
    #     {% else %}
    #     <li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>
    #     {% endif %}

    #     {% for i in products.paginator.page_range %}   <!-- PAGE NUMBER/RANGE -->
    #     {% if products.number == i %}
    #     <li class="page-item active"><a class="page-link" href="#">{{i}}</a></li>
    #     {% else %}
    #     <li class="page-item"><a class="page-link" href="?page={{i}}">{{i}}</a></li>
    #     {% endif %}
    #     {% endfor %}

    #     {% if products.has_next %}                   <!-- NEXT PAGE -->
    #     <li class="page-item"><a class="page-link" href="?page={{products.next_page_number}}">Next</a></li>
    #     {% else %}
    #     <li class="page-item disabled"><a class="page-link" href="#">Next</a></li>
    #     {% endif %}
    #   </ul>
    #   {% endif %}
    # </nav>

# http://127.0.0.1:8000/store/ --- previous and next val work krel

# --------------------------------------------------

# PRODUCT WARNING AND EMPTY CART ISSUE :-
# CARTS APP :- views.py :- from django.core.exceptions import ObjectDoesNotExist

# --------------------------------------------------

# SEARCH FUNCTION :-
# STORE APP :- 
# urls.py :- create search url
# views.py :- define search function
# navbar.html :- <a href="{% url 'store' %}" class="btn btn-outline-primary">Store</a>
        # <div class="col-lg  col-md-6 col-sm-12 col">
        #     <form action="{% url 'search' %}" class="search" method="GET">
        #         <div class="input-group w-100">
        #             <input type="text" class="form-control" style="width:60%;" placeholder="Search" name="keyword">

# store.html :- <section class="section-pagetop bg">
#     <div class="container">
#         {% if 'search' in request.path %}  <!-- Jr aapn Web vr Search kel means search valya path vr aalo-->
#         <h2 class="title-page">Search Result</h2>   <!-- tr search result as lihun de -->
#         {% else %}
#         <h2 class="title-page">Our Store</h2>       <!-- nahi tr our store lih -->
#         {% endif %}
#     </div> <!-- container //  -->
#     </section>

# Q is an object used to encapsulate a collection of keyword arguments

# =============================================================================================================

# 10) STARTING PRODUCT VARIATIONS AND VARIATION MANAGER 

# PRODUCT VARIATION PREPARATIONS :-
# product.html :- Size and Color 

# --------------------------------------------------

# SIZE AND COLOUR CART MADHE ADD ZAL PAHIJE :-
# CARTS APP:- 
# views.py :- in add_cart :- color = request.POST['color']  # product.html madhla color -- web vr color select krnya sthi
#                             size = request.POST['size']   # product.html mdhla size   -- web vr size select krnya sathi
# -----------------------------------

# PRODUCT VARIATION MODEL :-

# STORE APP :-
# models.py :- create class Variation
# admin.py  :- register Variation class
# GIT       :- makemigrations and migrate & runserver
# Google    :- http://127.0.0.1:8000/admin/store/variation/ --- color and size ethun deu aapn

# --------------------------------------------------

# PRODUCT VARIABLE FETCH DYNAMIC COLOR & VARIATION MANAGER & POST REQUEST :-

# STORE APP    :-
# models.py    :- create class VariationManager for color and size
# product.html :- size and color

# --------------------------------------------------

# GET THE INSTANCE OF VARIATION PART 1

# CARTS APP :- 
# views.py :- key and value takle 
#             key   = item                # if color is black then color is stored inside the key
#             value = request.POST[key]   # and black is stored inside the value

# models.py :- add variations in CartItem class
#              variations = models.ManyToManyField(Variation, blank=True) # may product have same variations so in that perticular situations we have to use manytomany filed
# admin.py  :- create class CartAdmin, CartItemAdmin for display whatever u want
# GIT       :- makemigrations and migarte and runserver

# =====================================================================================================

# 11) ADDNING THE VARIATIONS IN CART AND GROUPING CART ITEM VARITIONS 

# ADD VARIATION IN CART ITEM :-
# CARTS APP :- 
# views.py :- if len(product_variation) > 0:
#               cart_item.variations.clear()
#               for item in product_variation:
#                   cart_item.variations.add(item)  # cart madhe color and size aal pahije

# product.html :- {% if single_product.stock <= 0 %}
#                 <h3 class="text-danger">Out of Stock</h3>
#                 {% else %}
#                 <button type="submit" class="btn  btn-primary"> <span class="text">Add to cart</span> <i class="fas fa-shopping-cart"></i>  </button>
#               {% endif %}

# cart.html :- <p class="text-muted small">
#              {% if cart_item.variations.all %}   <!-- cart che purn variations aale pahije -->
#               {% for item in cart_item.variations.all %}
#                 {{ item.variation_category | capfirst }} : {{ item.variation_value | capfirst }} <br>
#               {% endfor %}     <!-- Color : White                 Size : Large -->
#              {% endif %}
#             </p>

# GROUPING CART ITEM VARIATIONS :- cart madhe different color che shirts add kele tr veg vegde add zale pahije ekach yachat nahi

# CARTS APP:- 
# views.py :- add_cart madhe aapn existing_variation, current_variation, item_id define kru

# CART INCREMENT / DECREMENT / REMOVE WITH VARIATIONS :-
# CARTS APP:- 
# views.py :- remove_cart, remove_cart_item madhe cart_item_id parameter dil
# urls.py  :- remove_cart, remove_cart_item madhe cart_item_id uls define kela

# PUSH CODE TO GITHUB :-