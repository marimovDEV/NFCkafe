
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated


class BronViewSet(viewsets.ModelViewSet):
    queryset = Bron.objects.all()
    serializer_class = BronSerializer


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# class HomeVideoViewSet(viewsets.ModelViewSet):
#     queryset = HomeVideo.objects.filter(is_active=True)
#     serializer_class = HomeVideoSerializer
    
class ChefsViewSet(viewsets.ModelViewSet):
    queryset = Chefs.objects.all()
    serializer_class = ChefsSerializer
    # permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]
    
class IshVaqtiViewSet(viewsets.ModelViewSet):
    queryset = IshVaqti.objects.all()
    serializer_class = IshVaqtiSerializer
    
class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class TavsiyaTaomViewSet(viewsets.ModelViewSet):
    queryset = TavsiyaTaom.objects.all()
    serializer_class = TavsiyaTaomSerializer

class AksiyaViewSet(viewsets.ModelViewSet):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer
