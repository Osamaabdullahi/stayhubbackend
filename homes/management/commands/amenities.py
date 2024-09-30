# from django.core.management.base import BaseCommand
# from homes.models import Listing, Amenity, ListingAmenity

# class Command(BaseCommand):
#     help = 'Populate the ListingAmenity model with amenities for each listing'

#     def handle(self, *args, **kwargs):
#         # Define amenities for each listing
#         amenities_per_listing = {
#             1: ["Wi-Fi", "Air Conditioning", "Kitchen"],
#             2: ["Heating", "Free Parking", "TV"],
#             3: ["Washer/Dryer", "Pet-Friendly", "Swimming Pool"],
#             4: ["Wi-Fi", "Kitchen", "Free Parking"],
#             5: ["Air Conditioning", "TV", "Swimming Pool"],
#             6: ["Elevator", "Gym", "Wi-Fi", "Kitchen"],
#             # Ensure all listings have amenities
#         }

#         # Retrieve all listings and amenities
#         for listing_id, amenity_names in amenities_per_listing.items():
#             try:
#                 listing = Listing.objects.get(id=listing_id)
#             except Listing.DoesNotExist:
#                 self.stdout.write(self.style.ERROR(f'Listing with ID {listing_id} does not exist.'))
#                 continue

#             for amenity_name in amenity_names:
#                 try:
#                     amenity = Amenity.objects.get(name=amenity_name)
#                 except Amenity.DoesNotExist:
#                     self.stdout.write(self.style.ERROR(f'Amenity "{amenity_name}" does not exist.'))
#                     continue
                
#                 ListingAmenity.objects.get_or_create(listing=listing, amenity=amenity)

#         self.stdout.write(self.style.SUCCESS('Successfully populated ListingAmenity'))
