
from django.contrib import admin
from .models import (
    Bron, 
    MenuCategory, 
    MenuItem, 
    Chefs, 
    Comment, 
    IshVaqti, 
    ContactInfo, 
    TavsiyaTaom, 
    Aksiya
)



@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'price')

@admin.register(Bron)
class BronAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'datetime', 'number_of_people', 'special_request')
    search_fields = ('name', 'email')
    list_filter = ('datetime', 'number_of_people')

@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'feedback')
    search_fields = ('client_name',)

@admin.register(IshVaqti)
class IshVaqtiAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time')
    list_filter = ('day',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'instagram')
    search_fields = ('address', 'phone', 'instagram')

@admin.register(TavsiyaTaom)
class TavsiyaTaomAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'start_date', 'end_date')
    search_fields = ('menu_item__name',)
    list_filter = ('start_date', 'end_date')

@admin.register(Aksiya)
class AksiyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage', 'start_date', 'end_date', 'active')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date', 'active')