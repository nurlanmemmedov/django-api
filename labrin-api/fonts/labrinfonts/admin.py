from django.contrib import admin
from .models import Font
from .models import FontFamily
from .models import Category
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import RegisterForm, UserAdminChangeForm
from .models import User
from django.contrib import admin

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = RegisterForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ['admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ['full_name',]}),
        ('Permissions', {'fields': ['admin',]}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','full_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Font)
admin.site.register(FontFamily)
admin.site.register(Category)
admin.site.register(User, UserAdmin)
