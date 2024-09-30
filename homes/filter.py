import django_filters
from .models import ListingImage,Listing,Amenity,Review,Profile,Message
from django_filters import CharFilter


class ListingImageFilter(django_filters.FilterSet):
    # Use CharFilter with lookup_expr='exact' to handle UUID filtering
    listing_id = CharFilter(field_name='listing__id', lookup_expr='exact')
    image_url = CharFilter(field_name='image_url', lookup_expr='icontains')
    owner_id=CharFilter(field_name='owner_id', lookup_expr='exact')

    class Meta:
        model = ListingImage
        fields = ['listing_id', 'image_url',"owner_id"]


class ListingAmenityFilter(django_filters.FilterSet):
    listing = CharFilter(field_name='listing__id', lookup_expr='exact')

    class Meta:
        model = Amenity
        fields = ['listing']

class ReviewsFilter(django_filters.FilterSet):
    listing = django_filters.NumberFilter(field_name="listing__id", lookup_expr='exact')

    class Meta:
        model = Review
        fields = ['listing']


class ProfileFilter(django_filters.FilterSet):
    user = django_filters.UUIDFilter(field_name='user__id')  # Filter by user UUID
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains')
    city_or_state = django_filters.CharFilter(field_name='city_or_state', lookup_expr='icontains')
    languages = django_filters.CharFilter(field_name='languages__name', lookup_expr='icontains')
    is_superhost = django_filters.BooleanFilter(field_name='is_superhost')

    class Meta:
        model = Profile
        fields = ['user', 'country', 'city_or_state', 'languages', 'is_superhost']


class ListingFilter(django_filters.FilterSet):
    owner = django_filters.UUIDFilter(field_name='owner', lookup_expr='exact')  # Adjust for UUID field
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")
    city = django_filters.CharFilter(field_name="city", lookup_expr="icontains")
    price_per_night = django_filters.RangeFilter(field_name="price_per_night")  # For filtering within a range
    category = django_filters.CharFilter(field_name="category", lookup_expr="icontains")

    class Meta:
        model = Listing
        fields = ['owner', 'country', 'city', 'price_per_night', 'category']


class MessageFilter(django_filters.FilterSet):
    sender = django_filters.UUIDFilter(field_name='sender')
    receiver = django_filters.UUIDFilter(field_name='receiver')

    class Meta:
        model = Message
        fields = ['sender', 'receiver']


