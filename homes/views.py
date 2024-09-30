from rest_framework import viewsets
from .models import  ListingImage, Listing, Amenity, Booking, Review, Message, Wishlist, Location,CustomUser,Profile
from .serializers import  ListingImageSerializer, ListingSerializer, AmenitySerializer, BookingSerializer,ReviewSerializer, MessageSerializer, WishlistSerializer, LocationSerializer,UserSerializer,ProfileSerializer,PostListing
from rest_framework.decorators import api_view,APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny,IsAuthenticated
from djoser.views import UserViewSet
from rest_framework import status
import os
from dotenv import load_dotenv
from .filter import ListingImageFilter,ListingAmenityFilter,ReviewsFilter,ProfileFilter,ListingFilter,MessageFilter
from rest_framework import generics

# users/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .token import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer





# Load the .env file
load_dotenv()

User = get_user_model()



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)

            # Return the response with user details and tokens
            return Response({
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'access': access,
                'refresh': str(refresh),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        try:
            # Verify the token with Google
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.getenv("CLIENT_ID"))

            # Get the user's Google info
            google_id = idinfo['sub']
            email = idinfo['email']
            first_name = idinfo.get('given_name', '')
            last_name = idinfo.get('family_name', '')
            
            # Check if the user already exists or create one
            user, created = CustomUser.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'is_active': True,
                    'is_staff': False,
                }
            )

            # Generate JWT tokens for the authenticated user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                'access': access_token,
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
            }, status=200)
        except ValueError:
            # Invalid token
            return Response({"error": "Invalid token"}, status=400)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=205)
        except Exception as e:
            return Response(status=400)



def api_documentation_view(request):
    return render(request, 'api_documentation.html')

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # 'listing_amenities': reverse('listingamenity-list', request=request, format=format),
        'listing_images': reverse('listingimage-list', request=request, format=format),
        'listings': reverse('listing-list', request=request, format=format),
        'amenities': reverse('amenity-list', request=request, format=format),
        'bookings': reverse('booking-list', request=request, format=format),
        'reviews': reverse('review-list', request=request, format=format),
        'messages': reverse('message-list', request=request, format=format),
        'wishlists': reverse('wishlist-list', request=request, format=format),
        'locations': reverse('location-list', request=request, format=format),
    })

# ListingAmenity ViewSet
# class ListingAmenityViewSet(viewsets.ModelViewSet):
#     queryset = ListingAmenity.objects.all()
#     serializer_class = ListingAmenitySerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = ListingAmenityFilter

# ListingImage ViewSet
class ListingImageViewSet(viewsets.ModelViewSet):
    queryset = ListingImage.objects.all()
    serializer_class = ListingImageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ListingImageFilter

# Listing ViewSet
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ListingFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 

#view for posting listings
class AddListings(generics.ListCreateAPIView):
    serializer_class=PostListing
    queryset=Listing.objects.all()


# Amenity ViewSet
class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = ListingAmenityFilter  

# Booking ViewSet
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_class = ReviewsFilter  

# Message ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter  


#profile viewset
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfileFilter

# Wishlist ViewSet
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

# Location ViewSet
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer




