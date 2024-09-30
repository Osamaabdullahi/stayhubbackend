# users/urls.py
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import CustomTokenObtainPairView,UserRegisterView, UserLoginView,GoogleLoginView,LogoutView,UserViewset,ListingViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'listings', ListingViewSet)



urlpatterns = [

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include(router.urls)),


    path('api/register/', UserRegisterView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing tokens

    path('auth/google/', GoogleLoginView.as_view(), name='google-login'),


]
