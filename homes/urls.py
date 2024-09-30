from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ListingImageViewSet, ListingViewSet, AmenityViewSet, BookingViewSet, ReviewViewSet, MessageViewSet, WishlistViewSet, LocationViewSet,ProfileViewSet

from . import views
from .views import GoogleLoginView,RegisterUserAPIView,LogoutView,CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'listing-images', ListingImageViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'wishlists', WishlistViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'profile', ProfileViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path("",views.api_root,name="root"),
    path('auth/google/', GoogleLoginView.as_view(), name='google-login'),
    path('auth/register/', RegisterUserAPIView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("addlisting/",views.AddListings.as_view(),name="addListing"),

]






