from rest_framework_simplejwt.views import TokenObtainPairView
from .tokens import CustomTokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, UserLoginSerializer,UserSerializer,HostSerlizer
from rest_framework.decorators import APIView
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny,IsAuthenticated
from homes.models import CustomUser,Profile
from rest_framework import status,viewsets
from dotenv import load_dotenv
import os
from rest_framework.exceptions import NotFound
from homes.serializers import ProfileSerializer
from homes.models import Listing
from homes.filter import ListingFilter
from django_filters.rest_framework import DjangoFilterBackend






load_dotenv()
User = get_user_model()



class UserViewset(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


#handles Login
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        response = {
            'refresh_token': str(refresh),
            'access_token': access_token,
            'user': {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        }
        return Response(response)


#handles logout
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#handles login with google
class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        try:
            # Verify the token with Google
            idinfo = id_token.verify_oauth2_token(token, requests.Request(),"596990711165-q3h6s4u8un2nmt1ppobcmemql7kgshhk.apps.googleusercontent.com")

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
                'access_token': access_token,
                'refresh_token': str(refresh),
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



class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = HostSerlizer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ListingFilter
