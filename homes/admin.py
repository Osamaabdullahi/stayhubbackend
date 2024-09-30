
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Profile,Listing, ListingImage, Amenity,Booking,Review,Message,Wishlist,Language




class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'city_or_state', 'is_superhost']
    filter_horizontal = ['languages']  # To select multiple languages easily

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Listing)
admin.site.register(ListingImage)
admin.site.register(Amenity)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Message)
admin.site.register(Wishlist)


