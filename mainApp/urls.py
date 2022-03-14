from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MagazineList,FirstCategoryList,ServiceList,ServiceDetail,\
    UserList,ExhibitionServiceList,ExhibitionList,BannerList,FirstCategoryDetail\
        ,ProList,KnowhowList

urlpatterns=[
    path('banner/',BannerList.as_view()),
    #path('review/<char:name>/', ReviewDetail.as_view()),
    path('category/', FirstCategoryList.as_view()),
    path('category/<int:pk>/', FirstCategoryDetail.as_view()),
    path('magazine/', MagazineList.as_view()),
    path('service/', ServiceList.as_view()),
    path('service/<int:pk>/', ServiceDetail.as_view()),
    path('exhibitionservice/', ExhibitionServiceList.as_view()),
    path('exhibition/', ExhibitionList.as_view()),
    path('user/', UserList.as_view()),
    path('pro/', ProList.as_view()),
    
    path('knowhow/', KnowhowList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)




