from django.core.management.base import BaseCommand
from homes.models import Amenity, Listing
import random

class Command(BaseCommand):
    help = 'Populates the Amenity model with different amenities for each listing'

    def handle(self, *args, **kwargs):
        # Common Airbnb amenities
        all_amenities = [
            "Wi-Fi", "Air Conditioning", "Kitchen", "Heating", "Washer/Dryer", 
            "Free Parking", "TV", "Pet-Friendly", "Swimming Pool", "Hot Tub",
            "Coffee Maker", "Hair Dryer", "Essentials", "Iron", "Private Entrance",
            "Smoke Detector", "First Aid Kit", "Fire Extinguisher", "Laptop-friendly Workspace", "Gym"
        ]

        # Get all listings
        listings = Listing.objects.all()

        if listings.exists():
            for listing in listings:
                # Select a random number of amenities for this listing (between 3 and 7)
                random_amenities = random.sample(all_amenities, random.randint(2, 15))

                for amenity_name in random_amenities:
                    # Check if the amenity already exists to avoid duplicates
                    amenity, created = Amenity.objects.get_or_create(listing=listing, name=amenity_name)
                    
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Successfully added {amenity_name} to {listing.title}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'{amenity_name} already exists for {listing.title}'))
        else:
            self.stdout.write(self.style.ERROR('No listings found to associate amenities with.'))
