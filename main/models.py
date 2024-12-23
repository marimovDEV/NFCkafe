from django.db import models
from django.utils.timezone import now



class Bron(models.Model):
    name = models.CharField(verbose_name='Mijoz ismi',max_length=255)
    phone_number = models.CharField(verbose_name='Mijoz telefor raqami',max_length=13)
    datetime = models.DateTimeField(verbose_name='Bron kuni')
    number_of_people = models.PositiveIntegerField(verbose_name='Qancha odam kelishi')
    special_request = models.TextField(verbose_name='Qoshimcha takliflari mijozlarni',blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.datetime}"

    class Meta:
        verbose_name = "Bron qilingan stol"
        verbose_name_plural = "Bron qilingan stollar" 

class MenuCategory(models.Model):
    name = models.CharField(verbose_name='Kategorya nomi',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"  

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, verbose_name='Kategoriya',on_delete=models.CASCADE, related_name="items")
    name = models.CharField(verbose_name='Mahsulot nomi',max_length=100)
    description = models.TextField(verbose_name='Qoshimcha malumot',blank=True, null=True)
    price = models.DecimalField(verbose_name='Narxi',max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name='Mahsulot rasmi',upload_to="menu_items/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"  

class Chefs(models.Model):
    name = models.CharField(verbose_name='Oshpaz ismi',max_length=100)
    designation = models.CharField(verbose_name='Darajasi',max_length=100)
    image = models.ImageField(verbose_name='Oshpazning rasmi',upload_to="team/", blank=True, null=True)
    facebook_url = models.URLField(verbose_name='Facebook',blank=True, null=True)
    instagram_url = models.URLField(verbose_name='Instagram',blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Povar malumotlari"
        verbose_name_plural = "Povar malumotlari"  

class Comment(models.Model):
    client_name = models.CharField(verbose_name='Mijoz ismi',max_length=100)
    feedback = models.TextField(verbose_name='Izoh')


    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = "Mijoz izohi"
        verbose_name_plural = "Mijozlar izohlari"  

class IshVaqti(models.Model):
    day = models.CharField(verbose_name='Kun',max_length=50)
    start_time = models.TimeField(verbose_name='Boshlash vaqti')
    end_time = models.TimeField(verbose_name='Tugash vaqti')

    def __str__(self):
        return f"{self.day}: {self.start_time} - {self.end_time}"

    class Meta:
        verbose_name = "Ish Vaqti"
        verbose_name_plural = "Ish Vaqti"  
        
class ContactInfo(models.Model):
    address = models.CharField(verbose_name='Manzil',max_length=255)
    phone = models.CharField(verbose_name='Telefon raqam',max_length=20)
    instagram = models.EmailField(verbose_name='Instagram')

    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = "Kontakt malumot"
        verbose_name_plural = "Kontakt malumotlari"   




class TavsiyaTaom(models.Model):
    menu_item = models.ForeignKey('MenuItem', verbose_name='Tavsiya qilinadigan taom',on_delete=models.CASCADE, related_name="featured_items")
    start_date = models.DateField(verbose_name='Boshlash vaqti')
    end_date = models.DateField(verbose_name='Tugash vaqti')
    description = models.TextField(verbose_name='tavsifi',blank=True, null=True)

    def __str__(self):
        return f"Featured: {self.menu_item.name} ({self.start_date} - {self.end_date})"

    class Meta:
        verbose_name = "Tavsiya qilingan Taom"
        verbose_name_plural = "Tavsiya qilingan Taomlar"


class Aksiya(models.Model):
    title = models.CharField(verbose_name='sarlavha',max_length=255)
    description = models.TextField(verbose_name='Tavsifi')
    discount_percentage = models.DecimalField(verbose_name='Foiz',max_digits=5, decimal_places=2)  # Example: 10.00 for 10% discount
    start_date = models.DateTimeField(verbose_name='Boshlash vaqti',default=now)
    end_date = models.DateTimeField(verbose_name='tugash vaqti')
    active = models.BooleanField(verbose_name='Aqtiv yoki NeAqtiv',default=True)

    def __str__(self):
        return f"{self.title} - {self.discount_percentage}% off"

    class Meta:
        verbose_name = "Aksiya"
        verbose_name_plural = "Aksiya"