from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.models import (Country, City, User, Location, Courier, PromoCode, Order, Category, Venue, Event, Promotion,
                         PromotionEvent, Session, Like, Basket)


@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    list_display = ('custom_image', "username", "email", "first_name", "last_name", "is_staff")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'image')}),
        (
            _("Permissions"),
            {
                'fields': (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def custom_image(self, obj: User):
        return format_html(
            f'<a href="{obj.pk}">'
            f'<img src="{obj.image.url}" width="35" height="35" style="object-fil: cover;"></a>'
        )

    custom_image.short_description = "Image"


@admin.register(Country)
class Admin(admin.ModelAdmin):
    pass


@admin.register(City)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Location)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Courier)
class Admin(admin.ModelAdmin):
    pass


@admin.register(PromoCode)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Order)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Category)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Venue)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Event)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Promotion)
class Admin(admin.ModelAdmin):
    pass


@admin.register(PromotionEvent)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Session)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Like)
class Admin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class Admin(admin.ModelAdmin):
    pass
