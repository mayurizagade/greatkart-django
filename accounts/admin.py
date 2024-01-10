from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 
                    'first_name',
                    'last_name',
                    'username',
                    'last_login',
                    'date_joined',
                    'is_active')    # kay kay display kraych aahe admin panel madhe
    list_display_links = ('email', 'first_name', 'last_name')   # optional -- email etc vr click krta aal pahije
    readonly_fields = ('last_login', 'date_joined')     # ha read only rahil
    ordering = ('-date_joined',)                        # descending order madhe date joined dakhvel
    filter_horizontal = () 
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)