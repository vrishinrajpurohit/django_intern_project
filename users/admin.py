from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel
from .forms import CustomHostUserChangeForm,CustomHostUserCreationForm

# # Register your models here.
#
class CustomHostUserAdmin(UserAdmin):
    add_form = CustomHostUserCreationForm
    form = CustomHostUserChangeForm
    model=CustomUserModel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'Profile', 'Address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','last_name','email','password1', 'password2', 'Profile','Address'),
        }),
    )
    list_display = ["username","email","first_name","Address","Profile"]
#
admin.site.register(CustomUserModel,CustomHostUserAdmin)
