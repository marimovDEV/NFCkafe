from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class BronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bron
        fields = ['id','name','phone_number','datetime','number_of_people','special_request']

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'category', 'name', 'description','price','image']

class ChefsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chefs
        fields = ['id','name','designation','image','facebook_url','instagram_url']
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'client_name', 'feedback']  # AdminProfile'da mavjud bo'lgan maydonlarni qo'shing

class IshVaqtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IshVaqti
        fields = ['id', 'day', 'start_time','end_time']  # AdminProfile'da mavjud bo'lgan maydonlarni qo'shing

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'address', 'phone','instagram']  # AdminProfile'da mavjud bo'lgan maydonlarni qo'shing

class TavsiyaTaomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TavsiyaTaom
        fields = ['id', 'menu_item', 'start_date','end_date','description']  # AdminProfile'da mavjud bo'lgan maydonlarni qo'shing

class AksiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aksiya
        fields = ['id', 'title', 'description','discount_percentage','start_date','end_date','active']  # AdminProfile'da mavjud bo'lgan maydonlarni qo'shing
