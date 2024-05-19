from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'user_type')}),
        ("Important Dates", {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions",)

admin.site.register(CustomUser, CustomUserAdmin)
