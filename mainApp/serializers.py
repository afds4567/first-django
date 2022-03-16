from pyexpat import model
from rest_framework import serializers
from .models import Magazine,FirstCategory, ProService, Review,Service, Exhibition, User, Banner,Pro, Knowhow
from django.db.models import Avg,Count

#Banner
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ( '__all__')


#Magazine
class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = ('id', 'title','linkUrl', 'imageUrl')


#최상단 카테고리
class FirstCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstCategory
        fields = ( '__all__')


#Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ( '__all__')


class TinyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('service_id','service_name','image_url')


#exhibition
class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ('__all__')


#메인페이지 Exhibition
class ExhibitionServiceSerializer(serializers.ModelSerializer):
    services = TinyServiceSerializer(many=True)

    def create(self, validated_data):
        services_data = validated_data.pop("services")
        exhibition = Exhibition.objects.create(**validated_data)
        for service_data in services_data:
            Service.objects.create(exhibition=exhibition, service=service_data)
        return Exhibition

    class Meta:
        model = Exhibition
        fields = ('id', 'name', 'services')


#User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( '__all__')


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "name", "profile_image")

#Pro
class OriginalProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = '__all__'


class ProSerializer(serializers.ModelSerializer):
    name          = serializers.CharField(source='user.name')
    profile_image = serializers.URLField(source='user.profile_image')
    
    class Meta:
        model = Pro
        fields = ( 'name','profile_image') 


class TinyProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = ["pro_id", "pro_description","service"]


class ProServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProService
        fields = '__all__'
        depth =1


#Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        #depth = 2


#Knowhow => 메인화면 노하우 소개
class KnowhowSerializer(serializers.ModelSerializer):
    #users = TinyUserSerializer(many=True, read_only=True)
    pro     = ProSerializer( read_only=True)
    service = TinyServiceSerializer(read_only=True)
    class Meta:
        model = Knowhow
        fields = ( 'id','name','coverImageUrl','pro','service')



#Rating 계산용 => 메인화면 인기 고수 소개 
class ProServiceReviewSerializer(serializers.ModelSerializer):
    pro = ProSerializer( read_only=True)
    service = TinyServiceSerializer(read_only=True)
    class Meta:
        model = ProService
        fields = ('pro','service','avg_rating','review_count')
        #ordering = ('-avg_rating',)

    avg_rating   = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    def get_avg_rating(self, ob):
        # reverse lookup on Reviews using item field
        return ob.reviews.all().aggregate(Avg('rating'))['rating__avg']
        
    def get_review_count(self, ob):
        # reverse lookup on Reviews using item field
        return ob.reviews.all().aggregate(Count('rating'))['rating__count']
        

    

