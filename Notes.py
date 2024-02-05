#                         <<<<<<<<<<<---------- CUSTOM USER MODEL ---------->>>>>>>>>>>

# GIT :- Activate env :- source env/Scripts/activate

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

# Google :- github.com -- create account in GIT :- password :- Mayuriz@123
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

# --------------------------------------------------

# GROUPING CART ITEM VARIATIONS :- cart madhe different color che shirts add kele tr veg vegde add zale pahije ekach yachat nahi

# CARTS APP:- 
# views.py :- add_cart madhe aapn existing_variation, current_variation, item_id define kru

# --------------------------------------------------

# CART INCREMENT / DECREMENT / REMOVE WITH VARIATIONS :-
# CARTS APP:- 
# views.py :- remove_cart, remove_cart_item madhe cart_item_id parameter dil
# urls.py  :- remove_cart, remove_cart_item madhe cart_item_id uls define kela

# --------------------------------------------------

# PUSH CODE TO GITHUB :-
# GIT :- git status                                     --- status dakhvte
#        git add -A                                     --- staging area madhe takte data
#        git commit -m "store and carts functionality"  --- local repository madhe takte data
#        git push origin main                           --- main ne push krte

# =====================================================================================================

# 12) REGISTRATION, LOGIN, WITH TOKEN BASED VARIFICATION & MESSAGE ALERT :-
# SETUP URLS AND DEGIN :-

# GIT :- atom .
# ACCOUNT APP   :- create file urls.py
#               :- create register, login, logout url in that file
# greatkart app :- urls.py :- include accounts urls in that
# views.py      :- define register, login, logout
# templates     :- create accounts folder
#               :- create register.html & login.html
# navbar.html   :- register and login ch navbar aal pahije mhnun --- <a href="{% url 'login' %}"> & <a href="{% url 'register' %}">
# forms.py      :- create new file in accounts app 'forms.py'
#               :- create Modelform in that file
# register.html :- {{ form.as_p }} --- as_p means as paragraph

# --------------------------------------------------

# IMPLEMENTING MODELFORM AND EDITING __INIT__ :-
# ACCOUNTS APP :-
# forms.py     :- in class Registrationform create method password and confirm password
#              :- define __init__ for 'placeholder' and 'form-control'
#              :- placeholder :- text displayed in an input field 
#              :- form-control :- form-control is a CSS class commonly used in frameworks like Bootstrap to style
#                                 form elements such as input fields, select boxes, and textareas.
# register.html :- {{ form.password }} & {{ form.confirm_password }}

# --------------------------------------------------

# MAKING VIEW AND EDITING MODELFORM CLEAN METHOD TO CHECK PASSOWRD :-
# ACCOUNTS APP:- 
# views.py    :- register function 
#                 --- when we use django from we have to use cleaned_data to fetch the value from the request
#                 --- user.phone_number = phone_number --- updating the phone_number attribute of the user object with the value stored in the variable phone_number.
# forms.py    :- define clean function for password authentications
# register.html :- {{ form.email.errors }} -- if password chukicha takla tr error dee
                #  {{ form.non_field_errors }} 

# ----------------------------------------------------------

# DJANGO MESSAGE ALERT 
# ACCOUNTS APP  :-
# settings.py   :- from django.contrib.messages import constants as messages
#                  MESSAGE_TAGS = {messages.ERROR : 'danger',}
# templates     :- include -- create new file 'alerts.html'
# alerts.html   :- write code for messages
# register.html :- {% include 'includes/alerts.html' %}
# views.py      :- messages.success(request, "Registration Sucessful...!")
#                  return redirect('register')
# static folder :- js -- scripts.js -- setTimeout(function(){$('#message').fadeOut('slow')}, 4000) 
#                                   -- register zalyavr kitived successful vala msg dakhvaych aahe, 4000 means 4 sec

# -------------------------------------------------------------

# LOGIN FUNCTIONALITY  
# ACCOUNTS APP:- 

# views.py    :- define login and logout
# login.html  :- write code on login.html
# navbar.html :- {% if user.id is None %} --- else login, register, logout all url -- endif

# ===========================================================================================================

# 13) USER ACCOUNT ACTIVATION AND ACTIVATION LINK EXPIRY 

# A] ENCODE USER PRIMARY KEY & SEND TOKEN BASED ACTIVATION LINK :-

# ACCOUNTS APP :-
# views.py     :- create User Activation methods
# templates    :- accounts -- create new file account_verification_email.html
# account_verification_email.html :- autoescape off and endautoescape new concepts coming in this html page
# Greatkart    :- settings.py :-  EMAIL_HOST = 'smtp.gmail.com'
#                                 EMAIL_PORT = 587
#                                 EMAIL_HOST_USER = 'mayurizagade18@gmail.com'
#                                 EMAIL_HOST_PASSWORD = 'zspv iinl sswi fhay'
#                                 EMAIL_USE_TLS = True

# EMAIL_HOST_PASSWORD KSA CREATE KELA ?
# mayurizagade@gmail.com cha google vr geli --- Security -- 2 Step Verification on kel
#                                           --- App Password sgdyat khali asto tyavr click kele 
#                                           --- tithe name dil app la aani dummy passowrd aala 'zspv iinl sswi fhay'

# ----------------------------------------------------------------

# B] DECODE USER PRIMARY KEY & ACTIVATE THE USER | EXPIRE LINK :-

# ACCOUNTS APP :-
# urls.py      :- make url for activate
# views.py     :- define activate
# login.html   :- {% if request.GET.command == 'verification' %} etc 
# Web          :- new account register kr to create hoil mg tula mail yeil gmailvr(mayurizagade18@gmail.com) aani 
#                 tu tya mail vr click kele tr to jo account tu create kela to activate hoil aani nntr tu login 
#                 kru sksil tr Ecommerce website open hoil

# ----------------------------------------------------------------

# C] DASHBOARD 
# Dashboard means Tracking the Order vala Board means kuthe order aahe address kay etc aste te
# ACCOUNT APP :-
# urls.py     :- create url of dashboard
# views.py    :- define dashboard
# navbar.html :- <a href="{% url 'dashboard' %}">Dashboard</a> <span class="dark-transp"> | </span>
# templates   :- accounts -- create file 'dashboard.html'
# dashboard.html :- copy code from greatkart.html(rathankumar) --- {% include 'includes/alerts.html' %} 
#                   aani logout vr click kelyavr logout zal pahije so {% url 'logout' %} 

# ===========================================================================================================

# 14) FORGOT PASSWORD WITH SECUREVALIDATION LINKS 

# A] FORGOT PASSOWRD 
# ACCOUNT APP:-
# urls.py    :- create url of forgotPassword
# views.py   :- define forgotPassword
# html       :- templates -- accounts -- create file 'forgotPassword.html'
# forgotPassword.html :- {% include 'includes/alerts.html' %}
#                        <form action="{% url 'forgotPassword' %}" method="POST">
#                          {% csrf_token %}

# email dilyavr mail vr msg yeil tithun reset kru password tr html page create krav lagel
# html :- templates  :- accounts -- create file 'reset_password_email.html'
# reset_password_email.html :- http://{{domain}}{% url 'resetpassword_validate' uidb64=uid token=token %}
# urls.py    :- resetpassword_validate cha url
# views.py   :- define resetpassword_validate

# ----------------------------------------------------------------

# B] RESET PASSWORD
# ACCOUNT APP :-
# url.py      :- resetPassword
# views.py    :- define resetPassword
# html        :- templates -- accounts -- create new file "resetPassword.html"

# ----------------------------------------------------------------

# C] PUSH VODE TO GITHUB
# GIT :- git status
#        git add -A
#        git commit -m "django authentication"
#        git push origin main

# ===========================================================================================================

# 15) CART CHECKOUT, AUTOMATICALLY ASSIGN THE CART ITEMS TO LOGGED-IN USER

# A] CHECKOUT PAGE DESIGN 
# CARTS APP :-
# urls.py   :- create checkout url
# views.py  :- define checkout function
# html      :- templates/store/checkout.html -- new html file created checkout.html
# checkout.html :- cart.html cha purn page ethe copy kraycha ahe

# ----------------------------------------------------------------

# B] ASSIGN THE USER TO CART ITEM
# CARTS APP :- 
# models.py :- user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
# views.py  :- ACCOUNT APP -- In login we are assiging user to cart item

# ----------------------------------------------------------------

# C] UPDATE CART COUNTER AND CART VIEW FOR LOGGED IN USER 
# CARTS APP :- 
# context_processor :- if request.user.is_authenticated: etccc
# views.py          :- cart -- if request.user.is_authenticated:

# ----------------------------------------------------------------

# D] VARIATION GROUPING FOR LOGGEDIN USERS PART1
# -- agr aapn logout asel aani product add kela to login kelyavr add hot aahe pn login krun aapn product 
#    add kela tr toch same product grouping nhi krt aahe tr ha issue ethe solve kela
# CARTS APP :
# views.py  :- if current_user.is_authenticated: aani else madhe same copy paste

# ----------------------------------------------------------------

# E] VARIATION GROUPING FOR LOGGEDIN USERS PART2
# ACCOUNTS APP :-
# views.py :- login madhe codes lihile cart madhe add zale pahije mhnun
#            -- GETTING THE PRODUCT VARIATION BY CART ID
#            -- GET THE CART ITEMS FROM THE USERS TO ACCESS HIS PRODUCT VARIATIONS
#            -- GET COMMON PRODUCT VARIATION INSIDE LIST

# ----------------------------------------------------------------

# F] FIX REMOVE AND DECREMENT BUTTON  
# CARTS APP :
# views.py  :- remove_cart madhe codes lihile -- if request.user.is_authenticated: -- aapm "-" vr click kele tr -1 zal paihje
#           :- remove_cart_item madhe same tsch -- remove vr click kele tr item cart madhun remove zala pahije  

# ----------------------------------------------------------------

# G] DYNAMICALLY REDIRECT THE USER TO NEXT PAGE
# if aapn logout asel aani aapn kuthe click kele tr tyane aaplyala login kelyavr tyach page vr nel pahije
# GIT :- pip install requests
#        py manage.py runserver
# ACCOUNT APP :
# views.py    :- login madhe --- params = dict(x.split("=")for x in query.split("&"))
# CARTS APP :-
# views.py :- checkout madhe -- if request.user.is_authenticated: try and except block

# ===========================================================================================================

# 16) ORDER AND ORDER NUMBER GENERATION 
# A] ORDER FLOW EXPLAINED 
#    Purn order flow explained kela ki aadhi order gheu mg to place order madhe jail tyat naw, gav,ptta aste
#    nntr order decrease or increase krte, email send hote, contact number, size, color etc
#    We have to create new app(orders), models, views, html etc for orders
#    We create 3 models Payment, Orders, Order Product

# GIT :- git status
#        git add -A
#        git commit -m "handled cart and checkout page for the logged in users"
#        git push origin main

# ----------------------------------------------------------------

# B] ORDER ORDERPRODUCT PAYMENT MODELS 
# GIT         :- py manage.py startapp orders -- APP CREATED
# settings.py :- register that app in installed app 'orders'

# ORDERS APP :
# models.py  :- create Payment, Order, OrderProduct models
# admin.py   :- register Payment, Order, OrderProduct
# GIT        :- makemigrations and migrate

# ----------------------------------------------------------------

# C] PLACE ORDER VIEW GENERATE ORDER NUMBER PART 1
# Greatkart urls :- include orders url 

# ORDERS APP :
# urls.py   :- In orders app create urls.py file
#              create url of place_order
# views.py  :- create place_order function
# forms.py  :- create forms.py file in orders app
#              create class OrderForm (forms)

# ----------------------------------------------------------------

# D] PLACE ORDER VIEW GENERATE ORDER NUMBER PART 2

# ORDER APP : 
# views.py  :- place_order madhe order number generate kel
# checkout.html :- <form action="{% url 'place_order' %}" method="POST">
# WEB       :- Nav, email etc takl aani place order kel tr aapla order admin madhe register hoil

# ----------------------------------------------------------------

# E] REVIEW ORDER PAGE SETUP 
# ORDER APP :
# urls.py :- create urls of payments
# view.py :- create payments function
# templates :- create order folder
#              in that folder create payments.html file
# payments.html :- copy cart.html code 
#                  Billing Address, Payments Method, Review etc

# ----------------------------------------------------------------

# F] REVIEW ORDER PAYMENT PAGE 
# ORDER APP :
# models.py :- define full_name, full_address
# payment.html :- <p class="card-text mb-0">{{order.full_name}}</p> etccc table vgere add kela
#                  mhnje billing madhe sgd disl pahije 

# ===========================================================================================================

# 17) PAYMENT GATEWAY INTEGRATIONS AND PLACE ORDER 

# A] CREATE PAYPAL BUSINES ACCOUNT
# mayurizagade18@gmail.com --- Pass@123
# yat sandbox account bnv means dummy account
# We want 2 account :- Personal :- greatkart.personalproject@gmail.com --- Pass@123
#                      Business :- greatkart.businessp2@gmail.com      --- Pass@123

# ----------------------------------------------------------------

# B] PAYPAL GATEWAY INTEGRATIONS 
# Paypal login krun personal and business account bnv
# payment.html :- PAYPAL BUTTON WILL LOAD pasun paypal ch details
# base.html :-  scipts add kele paypal che etc
# aapn payment kru tr paypal chi mail and password taka lagel nntr payment hoil
# Personal :- greatkart.personalproject@gmail.com --- Pass@123
# https://www.sandbox.paypal.com/myaccount/summary -- yat open kru tr transaction desil kiti paise baki aahe te pn

# ----------------------------------------------------------------

# C] SEND TRANSACTION DETAILS TO VIEW FINAL
# ORDER APP :
# views.html :- payments madhe code lihile admin madhe gele pahije order
# payment.html :- code for transaction details

# ===========================================================================================================

# 18) AFTER ORDER FUNCTIONALITIES 

# A] MOVE CART ITEMS TO ORDERPRODUCT TABLE 
# ORDER APP :
# views.py :- cart_items = CartItem.objects.filter(user=request.user) pasunch
# admin.py :- create class OrderProductInline for tabularinline 
#             table aala pahije admin madhe je pn product order kele tyacha
# WEB admin madhe OrderProduct vr click kelyavr table disel

# ----------------------------------------------------------------

# B] SET VARIATIONS TO ORDER PRODUCT
# ORDER APP :
# WEB admin -- OrderProduct madhe jo table aahe tyat variations la set kraych aahe
# views.py :- cart_item = CartItem.objects.get(id=item.id) etc
# variations admin page chya orderproduct madhe vr selected zale

# ----------------------------------------------------------------

# C] REDUCE QUANTITY OF SOLD PRODUCTS AND CLEAR CART
# ORDER APP :
# views.py :- product.stock -= item.quantity  ---- 100-2 = 98 Jeans rahil stock madhe
#             clear cart --- CartItem.objects.filter(user=request.user).delete()
#             ekda order zal ki cart clear zala pahije -- home page vr neil mg to

# ----------------------------------------------------------------

# D] SEND ORDERD RECIEVED EMAIL 
# views.py                  :- mail_subject = 'Thank You For Your Order...!' pasunchh
# html                      :- templates/orders/order_recieved_email.html 
# order_recieved_email.html :- {% autoescape off %} codes {% endautoescape %}

# jevva tu order krsil tr gmail vr msg, order number yeil -- for buyers
# web admin madhe to ordder number takla tr order diste konta aahe tr -- for developers

# ----------------------------------------------------------------

# E] REDIRECT USER TO ORDER COMPLETE PAGE 
# ORDER APP :
# urls.py             :- create order_complete url
# views.py            :- define order_complete function
# html                :- templates/orders/order_complete.html
# order_complete.html :- {% extends 'base.html' %} etc --- copy from rathnk sir html
# payments.html :-  window.location.href = redirect_url + '?order_number='+data.order_number+'&payment_id='+data.transID;
#                   ha url aahe jo search bar vr disel with order_number
# views.py      :- data = {
#                'order_number' : order.order_number,  # order_number -- pyaments.html madhe order_number
#                'transID'      : payment.payment_id,  #                 dila aahe to mg web search bar vr disel

# ----------------------------------------------------------------

# F] ORDER COMPLETION INVOICE 
# PAYMENT SUCCESSFULL vala page
# ORDER APP :
# views.py  :- function order_complete madhe try and except block create kela
#              tyat total, product, id etc sgdch dil je payment successfull zalyavr disayla pahije html page through
# order_complete.html :- line 33 pasun purn {{order.full_name}} ase vale vael add kele payment valya pagevr disayla

# ----------------------------------------------------------------

# G] GIT PUSH 
# GIT :- git status
#        git add -A
#        git commit -m "product order and payments"
#        git push origin main

# ===========================================================================================================

# 19) REVIEW AND RATING SYSYTEM 

# A] REVIEW AND RATING MODEL 
# STORE APP:
# models.py :- create new model ReviewRating
# admin.py  :- register ReviewRating
# Git       :- makemigrations and migrate then runserver

# ----------------------------------------------------------------

# B] MAKING RATING STARS PART1
# STORE APP:
# forms.py :- in store app create new fie 'forms.py'
#             class ReviewForm created
# product_detail.html :- Review val section
# greatkart :- static/css/custom.css
# base.html :- <link href="{% static 'css/custom.css' %}" rel="stylesheet" type="text/css"/>

# ----------------------------------------------------------------

# C] RATING MAKING STARS CSS PART2
# GREATKART:
# custom.css : codes lihile stars asayla hve click kelyavr yellow color aala pahije etc

# ----------------------------------------------------------------

# D] STORE THE REVIEW
# STORE APP :
# urls.py :- submit_review
# views.py :- define submit_review function
# product_detail.html :- {% if user.is_authenticated %} asel tr review deu skto jr user login nsel tr tyala login page vr pathv

# ===========================================================================================================

# 20) TWO FACTORS CHECK FOR SUBMITTING REVIEW

# A] CHECK IF USER PURCHAED PRODUCT BEFORE SUBMIT REVIEW
# STORE APP :
# views.py  :- product_detail madhe jr product purches kela trch review deta yeil
#               {% if orderproduct %} pasun 

# ----------------------------------------------------------------

# B] DISPLAY RATING STARS 
# STORE APP:
# views.py :- product_detail madhe review single product che deta aale pahije ae dile
# product_detail.html :- {% for review in reviews %} pasun purn review bddl
# custom.css :- .rating-star i{color : #ffb503 !important;} --- rating yellow color chi disli pahije
# http://127.0.0.1:8000/store/category/jeans/atx-jeans/

# ===========================================================================================================

# 21) RATING AND REVIEW AVERAGE CALCULATION

# A] RATING AVERAGE CALCULATION
# STORE APP :
# models.py :- define averageReview
# product_detail.html :- {{single_product.averageReview}}

# ----------------------------------------------------------------

# B] RATING AVERAGE STAR AND REVIEW COUNTER
# product_detail.html :- Customer REviews madhe                
#                        <i class="fa fa-star{% if single_product.averageReview < 0.5 %}-o{% elif single_product.averageReview >= 0.5 and single_product.averageReview < 1 %}-half-o {% endif %}" aria-hidden="true"></i>
#                        aani sgdyat vrti pn star disle pahije mhnun line 27 la pn copy paste kel

# STORE APP :
# models.py :- define countReview function for counting the review
# product_detail.html :- <span>{{single_product.countReview}} reviews</span> jithe review count dakhvaycha aahe tithe

# ----------------------------------------------------------------

# C] ANONYMOUS USER ERROR FIX
# STORE APP :
# views.py :- product_detail madhe jr login asel tr review deta yeil aani product gheta yeil
#             if request.user.is_authenticated: etc
#             else: orderproduct = None

# ----------------------------------------------------------------

# D] PUSH CODE TO GITHUB
# GIT :- git status
#        git add -A
#        git commit -m "product order and payments"
#        git push origin main

# ===========================================================================================================

# 22) REVIEW AND RATING SYSYTEM 

# A] 