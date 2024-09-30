from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from homes.models import CustomUser,Listing


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff','date_joined','id')

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Create the user
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Return the user and both tokens
        return {
            'user': user,
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def to_representation(self, instance):
        # Customize the representation to include user details and tokens
        user_data = super().to_representation(instance['user'])
        user_data['access_token'] = instance['access_token']
        user_data['refresh_token'] = instance['refresh_token']
        return user_data
    
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



class HostSerlizer(serializers.ModelSerializer):
      class Meta:
        model = Listing
        fields = ['owner',]
