from django.db import models

#                         <<<<<<<<<<<---------- CUSTOM USER MODEL ---------->>>>>>>>>>>

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):    # superadmin sathi
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError("User Must Have An Email Address") # email nahi takla tr
        
        if not username:
            raise ValueError("User Must Have An Username")      # username ni tr 
        
        user = self.model(
            email      = self.normalize_email(email), # jr capital madhe email takla tr to small letter madhe krel
            username   = username,
            first_name = first_name,
            last_name  = last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email      = self.normalize_email(email),
            username   = username,
            password   = password,
            first_name = first_name,
            last_name  = last_name,
        )

        user.is_admin      = True
        user.is_active     = True
        user.is_staff      = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):    # admin sathi class
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.IntegerField(null=True)

    # required :-
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'  # aapn login hou email fields ne
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email             # email address deil templates madhe admin chya
    
    def has_perm(self, perm, obj=None):
        return self.is_admin          # if user is admin so he have permission to do all changes
    
    def has_module_perms(self, add_label):
        return True
    
