from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from bookStore.accounts.forms import AppUserCreationForm, AppUserChangeForm
from bookStore.accounts.models import UserProfile

# Register your models here.
UserModel = get_user_model()


class ProfileInline(admin.StackedInline):  # Or admin.TabularInline for compact display
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profiles'


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('pk', 'username', 'is_staff', 'is_superuser')
    search_fields = ('username',)
    ordering = ('pk',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
