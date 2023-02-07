from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Organization
# Register your models here.

class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("username", "email", "organization", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", "organization")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "organization", "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid']

admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
