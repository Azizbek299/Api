from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('', home, name='home'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('boglanish/', BoglanishApi.as_view(), name='boglanish'),
    path('phone-number/', PhoneApiView.as_view(), name='phone-number'),
    path('boglanish/<int:pk>/', BoglanishDetail.as_view(), name='boglanish-detail'),
    path('phone-number/<int:pk>/', PhoneDetail, name='phone-detail'),
    path('use/', UserList.as_view()),
    path('use/<int:pk>/', UserDetail.as_view()),

    path('simple/', SimpleCreateListApiView.as_view()),
    path('simple/<int:id>/', SimpleUdateView.as_view()),

]
