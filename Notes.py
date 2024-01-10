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
# Password:
# Password (again):
# py manage.py runserver -- open in google and see admin panel madhe email aal

# PASSWORD dist aahe admin panel madhe :-
# admin.py madhe changes kele accounts valya

# ADD IMAGES from Admin:-
# settings.py -- MEDIA_URL = 'media/'
#                MEDIA_ROOT = BASE_DIR /'media'
# urls.py -- from django.conf.urls.static import static
#            from django.conf import settings
#  after urlpatterns[] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Download img from sir video(or anywhere)
# Go to admin panel and add category with images

# I WANT SLUG :- means category madhe lihile tr slug madhe pn lihun aal pahije
# models madhe slugfileds tak slug mdhe
# makemigrations and migrate
# admin.py :- category vala -- class create kr

# -------------------------------------------------------------------------------

#   PRODUCT MANAGER :- store
# create store app in GIT :- py manage.py startapp store
# register that app in settings
# create Product model in models.py of store
# register that model in admin.py of store
# In GIT :- makemigations and migrate and runserver
# Google :- open --- http://127.0.0.1:8000/admin/
#                    Add Products
#                    

# NOW WE HAVE TO ADD ON OUR WEBSITE :-
# Open --- http://127.0.0.1:8000/
# greatkart -- Project cha views madhe aapn Purn products add kru
# home.html changes --- for loop lavla product.name,price,image deu means web vr disel images,price
# store app madhe urls.py create kru
# store app madhe views create kru
# new template create kru store(folder)
# in that folder create store.html
# http://127.0.0.1:8000/store/shoes/ -- jo product search kru to product deil

# ----------------------------------------------------------------------------------------

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


# I WANT PRODUCT DETAIL IN WEB PAGE :-

# STORE APP --->

# urls.py :- create product_slug url 
# views.py :- define product_detail function
# HTML :- templates -- store -- create product_detail.html 
# models.py :- def get_url function for getting all url -- means aapn product madhe shirts,
#              earning etc vr click kele tr tyacha related aale pahije
# home.html :- {{product.get_url}} tak jo define kela means url taklyavr product bddl yeil 

# When I click on store we have to go on home page :-
# navbar.html :- <a href="{% url 'home' %}" class="brand-wrap"> -- brand vr click kele tr home vr nele pahije
#                <a href="{% url 'store' %}" class="btn btn-outline-primary">Store</a>
#                   store vr click kele tr home vr nele pahije
# home.html :- <a href="{% url 'store' %}" class="btn btn-outline-primary float-right">See all</a>
#               See all vr click kele tr home vr nele pahije
# store.html :- <a href="{{ product.get_url }}"> -- product vr click kelyabrobr detail disle pahije
#               <a href="{{ product.get_url }}" class="title">{{product.product_name}}</a>

# I WANT TO CHANGE BANNER :-
# select image whatever u want, then add to static/images/banners/cover
# home.html :- <img src="{% static 'images/banners/cover.jpg' %}" class="img-fluid rounded">

# ----------------------------------------------------------------------------------------

# 6) SETUP GIT AND START CART FUNCTIONALITY :-

# Google :- github.com -- create account in GIT 
#                      -- + click on this sign top on right side -- create New Repository -- give name & create
# Open GITHUB :- git init 
# ADD TO CART BUTON :- 
