from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError('Invalid email or password.')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('Email and password are required.')

        return attrs



class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_joined')




User = get_user_model()  # If using a custom user model, this ensures compatibility

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name','last_name', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        data = super().to_representation(instance)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data



    


#ListingAmenity
# class ListingAmenitySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ListingAmenity
#         fields = '__all__'



#ListingImage
class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = '__all__'





#Listing
class ListingSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.first_name')
    owner = CustomUserSerializer() 

    class Meta:
        model = Listing
        fields = ['id','title', 'description', 'address', 'city', 'state', 'country', 'price_per_night', 'max_guests', 'bedrooms', 'bathrooms', 'created_at', 'updated_at', 'is_available','mainImage_url','category','image', 'owner']

#handles posting of listings
class PostListing(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

#Amenity
class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

#profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



#Booking
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

#Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

# Message
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields="__all__"

#Wishlist
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        fields="__all__"

# Location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields="__all__"