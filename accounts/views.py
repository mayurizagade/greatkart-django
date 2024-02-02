from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from carts.models import Cart, CartItem
from carts.views import _cart_id
import requests

# VERIFICATION EMAIL 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name   = form.cleaned_data['first_name'] # when we use django from we have to use cleaned_data to fetch the value from the request
            last_name    = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email        = form.cleaned_data['email']
            password     = form.cleaned_data['password']
            username     = email.split("@")[0]

            # We are creating users 
            user         = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number # Accounts class madhe aap phone_number method dili nahi tr user sobt ethe method dili --- updating the phone_number attribute of the user object with the value stored in the variable phone_number.
            user.save()

            # <<<--- USER ACTIVATION --->>> 
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message      = render_to_string('accounts/account_verification_email.html', {
                'user'   : user,                                        # username
                'domain' : current_site,                                # domain aahe
                'uid'    : urlsafe_base64_encode(force_bytes(user.pk)), # encoding user id with base64_encode so nobody can see the primary key
                'token'  : default_token_generator.make_token(user),    # create token for perticular user and check token
                })
            to_email   = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            # messages.success(request, "Thank You For Registering With Us, We Have Sent You A Verfiaction Email To Your Email Address[mayurizagade18@gmail.com]. Please Verify it...!")
            return redirect('/accounts/login/?command=verification&email='+email) # verification sathi command
    else:
        form = RegistrationForm()
    context = { 'form' : form,}
    return render(request, "accounts/register.html", context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email'] # ha email login.html madhla name=email vala email aahe
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:   # if we have user
            try:    # cartitem madhe kahi add kele tr logout kelyavr te gel nahi pahije
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    # <<-- GETTING THE PRODUCT VARIATION BY CART ID -->> 
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))  # productvariation madhe variation list takt aaho
                                                # list madhe convert kele bcoz to already queryset madhe aahe
                        
                    # <<-- GET THE CART ITEMS FROM THE USERS TO ACCESS HIS PRODUCT VARIATIONS -->>
                    cart_item = CartItem.objects.filter(user=user)  # product exsits krte tr add kr tyala tyachatch
                    ex_var_list = []  # we getting existing variations list from the database
                    id = []           # id of that perticular item
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)

                    # <<-- GET COMMON PRODUCT VARIATION INSIDE LIST -->>
                    # product_variation = [1, 2, 3, 4, 6]
                    # ex_var_list = [4, 6, 3, 5]  -- hya don madhe 4,6 commomn aahe tr he dogh ekatch aale pahije
                    
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index   = ex_var_list.index(pr)
                            item_id = id[index]                        # id madhe aapn index takla 
                            item    = CartItem.objects.get(id=item_id) # getting cartitem id
                            item.quantity += 1                         # increasing quantity "+" vr click kele tr
                            item.user = user                           # assign current user to cart item
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:  
                                item.user = user
                                item.save()  # assiging user to cart item
            except:
                pass
            auth.login(request, user)
            messages.success(request, 'You Are Now Logged In')
            url = request.META.get("HTTP_REFERER") # Previous url vr neun fekel
            try:
                query = requests.utils.urlparse(url).query
                # print('query -->', query)    # query --> next=/cart/checkout/
                # next=/cart/checkout/   --- next is key and cart/checkout is value
                params = dict(x.split("=")for x in query.split("&")) # x.split is spliting "=" value and convert in dict
                # print("params -->", params)   # params --> {'next': '/cart/checkout/'}
                if "next" in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect("dashboard")
            
        else:
            messages.error(request, "Invalid Login Credentials...!") # credentials chukle tr error de
            return redirect('login')                                 # aani punha login page vr pathv
    return render(request, "accounts/login.html")

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You Are Looged Out....!")
    return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()  # give u primary key of user
        user = Account._default_manager.get(pk=uid)   # return user object
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):  # user asel tr 
        user.is_active = True  # user asel tr activate hoil 
        user.save()
        messages.success(request, 'Congratulations Your Account Is Activated....!')
        return redirect('login')
        # -- aadhi mayurizagade18 vr mail yeil mla aani me jr tya link vr click kele tr jo account create kela to accout activate hoil aani msg yeil congrats etc aani login page vr pathvel
    else:
        messages.error(request, 'Invalid Activation Link...!') 
        return redirect('register') # if account nsel tr Invalid Activation msg yeil aani register krayla lavel

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email) # email address exact same to same aahe kay check krel

            # <<<--- RESET PASSWORD EMAIL --->>>
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message      = render_to_string("accounts/reset_password_email.html",{
                "user"   : user,
                "domain" : current_site,
                "uid"    : urlsafe_base64_encode(force_bytes(user.pk)),
                'token'  : default_token_generator.make_token(user),
            })
            to_email     = email
            send_email   = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Password Reset Email Has Been Sent To Your Email Address.')
            return redirect('login')
        
        else:
            messages.error(request, 'Account Does Not Exsit..!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid  # save the uid in the session
        messages.success(request, 'Please Reset Your Password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This Link is Has Been Expired')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
           uid = request.session.get('uid') 
           user = Account.objects.get(pk=uid)
           user.set_password(password) # set_password is inbuilt function of django
           user.save()
           messages.success(request, 'Password Reset Successful...!')
           return redirect('login')  # jsa password reset zala tsach login page vr pathv
        else:
            messages.error(request, 'Password Does Not Match!')
            return redirect('resetPassword')
        
    else:  # if msg post nsel tr this template will load
        return render(request, 'accounts/resetPassword.html')