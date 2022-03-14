from pyexpat import model
from rest_framework import serializers
from .models import Magazine,FirstCategory,Service, Exhibition, User, Banner,Pro, Knowhow

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
class ProSerializer(serializers.ModelSerializer):
    name          = serializers.CharField(source='user.name')
    profile_image = serializers.URLField(source='user.profile_image')
    #service_name = serializers.CharField(source='service.service_name')
    
    class Meta:
        model = Pro
        fields = ( 'name','profile_image') #'service_name')


class TinyProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = ["pro_id", "pro_description","service"]



#Knowhow
class KnowhowSerializer(serializers.ModelSerializer):
    #users = TinyUserSerializer(many=True, read_only=True)
    pro     = ProSerializer( read_only=True)
    service = TinyServiceSerializer(read_only=True)
    class Meta:
        model = Knowhow
        fields = ( 'id','name','coverImageUrl','pro','service')

    
    


#knowhow-custom
# class KnowhowSerializer(serializers.ModelSerializer):
#     users = TinyUserSerializer(many=True, read_only=True)
#     pros = TinyProSerializer(many=True, read_only=True)

#     def create(self, validated_data):
#         users_data = validated_data.pop("users")
#         pros_data = validated_data.pop("pros")
#         knowhow = Knowhow.objects.create(**validated_data)
#         # for user_data in users_data:
#         #     User.objects.create(knowhow=knowhow, user=user_data)
#         for pro_data in pros_data:
#             Pro.objects.create(knowhow=knowhow, pros=pro_data)
#         return Knowhow

#     class Meta:
#         model = Knowhow
#         fields = ["id", "name", "coverImageUrl","created_at","users","pros"]

