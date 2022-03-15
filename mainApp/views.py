from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import  MagazineSerializer,FirstCategorySerializer, ReviewSerializer,UserSerializer,ServiceSerializer\
    ,ExhibitionServiceSerializer,ExhibitionSerializer,BannerSerializer,ProSerializer, KnowhowSerializer\
       ,OriginalProSerializer,ProServiceSerializer,ProServiceReviewSerializer

from .models import Knowhow, Magazine, ProService,Service,FirstCategory,User,Exhibition, Banner, Pro\
    , Review

# Create your views here.


# class ReviewList(APIView):  # 목록 보여줌
#     def get(self, request):  # 리스트 보여줄 때
#         reviews = Review.objects.all()  # review의 모든 객체를
#         serializer = ReviewSerializer(reviews, many=True)  # 시리얼라이즈해서
#         return Response(serializer.data)  # 응답으로 시리얼라이즈 데이터를 반환한다.

#     def post(self, request):  # 새 글 작성시
#         serializer = ReviewSerializer(
#             data = request.data)  # 사용자에게 받은 입력 데이터를
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class ReviewDetail(APIView):
#     # pk에 해당하는 객
#     def get_object(self,pk):
#         try:
#             return Review.objects.get(pk=pk)
#         except Review.DoesNotExist:
#             raise Http404

#     # 특정 게시물 조회
#     def get(self,request,pk, format=None):
#         review = self.get_object(pk)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)

#     # 특정 게시물 수정
#     def put(self, request, pk, format=None):
#         review = self.get_object(pk)
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # 특정 게시물 삭제
#     def delete(self, request, pk, format=None):
#         review = self.get_object(pk)
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#Banner
class BannerList(APIView):

    def get(self, request):
        banners = Banner.objects.all()

        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = BannerSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# Category 
class FirstCategoryList(APIView):

    def get(self, request):
        categories = FirstCategory.objects.all()

        serializer = FirstCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = FirstCategorySerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class FirstCategoryDetail(APIView):

    def get_object(self,pk):
        try:
            return FirstCategory.objects.get(pk=pk)
        except FirstCategory.DoesNotExist:
            raise Http404


    #특정 게시물 조회
    def get(self,request,pk, format=None):
        services = self.get_object(pk)
        serializer = FirstCategorySerializer(services)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        firstcategories = self.get_object(pk)
        serializer = FirstCategorySerializer(firstcategories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


#User
class UserList(APIView):

    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = UserSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#Pro
class OriginalProList(APIView):

    def get(self, request):
        Pros = Pro.objects.all()

        serializer = OriginalProSerializer(Pros, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = OriginalProSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



class ProList(APIView):

    def get(self, request):
        Pros = Pro.objects.all()

        serializer = ProSerializer(Pros, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ProSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProServiceList(APIView):

    def get(self, request):
        Pros = ProService.objects.all()

        serializer = ProServiceSerializer(Pros, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ProServiceSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



#Magazine
class MagazineList(APIView):

    def get(self, request):
        magazines = Magazine.objects.all()

        serializer = MagazineSerializer(magazines, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = MagazineSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#Service
class ServiceList(APIView):


    def get(self, request):
        services = Service.objects.all()

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ServiceSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ServiceDetail(APIView):

    def get_object(self,pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404


    #특정 게시물 조회
    def get(self,request,pk, format=None):
        services = self.get_object(pk)
        serializer = ServiceSerializer(services)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        services = self.get_object(pk)
        serializer = ServiceSerializer(services, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

#Exhibition
class ExhibitionList(APIView):

    def get(self, request):
        exhibition = Exhibition.objects.all()

        serializer = ExhibitionSerializer(exhibition, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ExhibitionSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
# main화면 exhibition용 
class ExhibitionServiceList(APIView):

    def get(self, request):
        exhibitions = Exhibition.objects.all()

        serializer = ExhibitionServiceSerializer(exhibitions, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ExhibitionServiceSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



#Service
class KnowhowList(APIView):


    def get(self, request):
        knowhows = Knowhow.objects.all()

        serializer = KnowhowSerializer(knowhows, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = KnowhowSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#Review
class ReviewList(APIView):


    def get(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ReviewSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


#pop-pro전용
class ProServiceReviewList(APIView):
    

    def get(self, request):
        proservices = ProService.objects.all()
        serializer = ProServiceReviewSerializer(proservices, many=True)
        
        return Response(serializer.data)

    def post(self, request):  # 새 글 작성시
        serializer = ProServiceReviewSerializer(
            data = request.data)  # 사용자에게 받은 입력 데이터를
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        