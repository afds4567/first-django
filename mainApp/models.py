from pyexpat import model
from re import T
from django.db import models

# Create your models here.

class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    image_url = models.URLField()

    class Meta:
        db_table = "banners"
    
    


class FirstCategory(models.Model):
    first_category_id   = models.AutoField(primary_key=True)
    first_category_name = models.CharField(max_length=10)
    first_category_url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "first_categories"
    
    def __str__(self):
        return self.first_category_name

class SecondCategory(models.Model):
    second_cateogry_id   = models.AutoField(primary_key=True)
    first_category       = models.ForeignKey(FirstCategory, on_delete=models.CASCADE)
    second_category_name = models.CharField(max_length=10)

    class Meta:
        db_table = "second_categories"

    def __str__(self):
        return self.second_category_name

class Service(models.Model):
    service_id      = models.AutoField(primary_key=True)
    #pro             = models.ForeignKey('Pro',null=True,on_delete=models.CASCADE)    
    second_category = models.ForeignKey(SecondCategory,on_delete=models.CASCADE)
    exhibition      = models.ForeignKey('Exhibition', related_name='services',null=True, on_delete=models.CASCADE)
    service_name    = models.CharField(max_length=20)
    image_url       = models.URLField()
    request_count   = models.IntegerField()
    
    class Meta:
        db_table = "services"
        ordering = ['-request_count']


class Review(models.Model):
    review_id       = models.AutoField(primary_key=True)
    writer          = models.ForeignKey('User', on_delete=models.CASCADE)
    proservice      = models.ForeignKey('ProService',on_delete=models.CASCADE,related_name='reviews')
    content         = models.CharField(max_length=200,default="Good")
    rating          = models.DecimalField(max_digits=2, decimal_places=1)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reviews"


class User(models.Model):
    user_id       = models.AutoField(primary_key=True,unique=True)
    name          = models.CharField(max_length=45)
    gender        = models.CharField(max_length=2,default='남자')
    email         = models.EmailField(max_length=60, unique=True)
    password      = models.CharField(max_length=100)
    phone_number  = models.CharField(max_length=11, unique=True, null=True)
    profile_image = models.URLField(max_length=2000, null=True)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name
    

class Pro(models.Model):
    pro_id          = models.AutoField(primary_key=True,unique=True)
    user            = models.OneToOneField('User', on_delete=models.CASCADE)
    #service        = models.ForeignKey('Service',on_delete=models.CASCADE)
    address         = models.ForeignKey('Address',on_delete=models.CASCADE, null=True)
    company_name    = models.CharField(max_length=100, null=True)
    is_safe_payment = models.BooleanField( default=False)
    pro_description = models.CharField(max_length=200,default="소개글이 없습니다")
    hired_count     = models.IntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pro"

    def __str__(self):
        return self.company_name

#여러 서비스 제공하는 고수 서비스 중 각각에 대한 정보  
class ProService(models.Model):
    proservice_id  = models.AutoField(primary_key=True)
    pro            = models.ForeignKey(Pro, on_delete=models.CASCADE)
    service        = models.ForeignKey(Service, on_delete=models.CASCADE)
    is_main        = models.BooleanField(default=False)
    status         = models.CharField(default="inprogress",max_length=20)
    price          = models.IntegerField(default=10000, null=True)
    item_img       = models.URLField(null=True)
    item_name      = models.CharField(max_length=100, null=True)
    class Meta:
        unique_together = ('pro','service')

    #rating        = models.FloatField(default=0)
    #review_count


class Address(models.Model):
    address_id    = models.AutoField(primary_key=True)
    address_category_1  = models.CharField(max_length=5)
    address_category_2 = models.CharField(max_length=5)

    class Meta:
        db_table = "addresses"

    def __str__(self):
        return self.address


class Magazine(models.Model):
    title    = models.CharField(max_length=100)
    linkUrl  = models.URLField()
    imageUrl = models.URLField()

    class Meta:
        db_table = "magazines"

    def __str__(self):
        return self.title


class Exhibition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "exhibitions"

    def __str__(self):
        return self.name


class Knowhow(models.Model):
    id             = models.AutoField(primary_key=True)
    name           = models.CharField(max_length=100)
    service        = models.OneToOneField(Service, related_name='services', on_delete=models.CASCADE,null=True)
    pro            = models.OneToOneField(Pro, related_name='pros', on_delete=models.CASCADE,null=True)
    coverImageUrl  = models.URLField()
    created_at     = models.DateTimeField(auto_now_add=True)
