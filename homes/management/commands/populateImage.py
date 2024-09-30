from django.core.management.base import BaseCommand
from homes.models import Listing, ListingImage
import random

class Command(BaseCommand):
    help = 'Populate ListingImage model with image URLs for listings'

    def handle(self, *args, **kwargs):
        images = [
            "https://i.pinimg.com/474x/13/91/b5/1391b5eefe5c3b5b2d657aeb868e7b5e.jpg",
            "https://i.pinimg.com/474x/5c/06/19/5c06197dd3b53a69c6b5c967ec558a2b.jpg",
            "https://i.pinimg.com/474x/2f/fd/c2/2ffdc247e7089593b2ba3d8656d587b8.jpg",
            "https://i.pinimg.com/474x/ef/8d/1e/ef8d1e252e621f7d8226bd6b2b6bd7bd.jpg",
            "https://i.pinimg.com/474x/e4/f6/6c/e4f66ceedd7ebab7b2036b941807f58d.jpg",
            "https://i.pinimg.com/474x/e2/16/c5/e216c5d3ba2356676429bcf10bc5245a.jpg",
            "https://i.pinimg.com/474x/c9/e2/59/c9e2596d591f00979caf4007e5481bc0.jpg",
            "https://i.pinimg.com/474x/d8/a2/59/d8a259ea0c21ee411b5ee12b622e6b48.jpg",
            "https://i.pinimg.com/474x/dd/a8/72/dda872d9803f9c5f9653c76ecfc2781d.jpg",
            "https://i.pinimg.com/474x/e9/ce/c5/e9cec54d0a7143fd9f81f574d905b479.jpg",
            "https://i.pinimg.com/474x/ca/05/d0/ca05d000e642ba5b5cbde10dead887ef.jpg",
            "https://i.pinimg.com/474x/b1/3e/0b/b13e0baee6175152011efbee8e4ad958.jpg",
            "https://i.pinimg.com/474x/59/ce/d0/59ced0179bed07b0c0d3b6fdbc03a1d8.jpg",
            "https://i.pinimg.com/474x/4e/bf/61/4ebf61c8743198419d0c407ea93dbe80.jpg",
            "https://i.pinimg.com/474x/f7/45/b1/f745b17ae616b52b142a5cc69341723f.jpg",
            "https://i.pinimg.com/474x/05/bc/7a/05bc7abb5e5630e7df9201e265913bba.jpg",
            "https://i.pinimg.com/474x/2d/81/d5/2d81d5b0ab403c8f0933fcc37e77c94e.jpg",
            "https://i.pinimg.com/474x/f0/20/1f/f0201f4a6ad9cdc5f532f6c9c627e86a.jpg",
            "https://i.pinimg.com/474x/ba/af/0f/baaf0f4d7a965ca0979036a5ed52f080.jpg",
            "https://i.pinimg.com/564x/b2/fe/10/b2fe109278f8811a4a7f3a46b8a1f960.jpg",
            "https://i.pinimg.com/474x/d3/34/b1/d334b1a27c10a5abd617cf22343a08fe.jpg",
        ]

        # Get all listings (modify this query if you need a specific subset)
        listings = Listing.objects.all()[:50]  # Example: limiting to the first 50 listings

        for listing in listings:
            try:
                # Randomize or iterate through the image list
                for url in images:
                    ListingImage.objects.create(
                        listing=listing,
                        image_url=url
                    )
                self.stdout.write(self.style.SUCCESS(f'Successfully populated ListingImage model with image URLs for listing id={listing.id}.'))
            except Listing.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Listing with id={listing.id} does not exist.'))
