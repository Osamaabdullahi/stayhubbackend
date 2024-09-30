from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from homes.models import ListingImage

class Command(BaseCommand):
    help = 'Populate ListingImage with owners from the User model'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Retrieve all users from the database
        users = User.objects.all()

        # Check if there are any users available
        if users.count() == 0:
            self.stdout.write(self.style.ERROR("No users found in the database."))
            return

        # Get all ListingImage instances that don't have an owner yet
        listing_images_without_owner = ListingImage.objects.filter(owner__isnull=True)

        if not listing_images_without_owner.exists():
            self.stdout.write(self.style.SUCCESS("All listing images already have an owner."))
            return

        # Populate owners by cycling through all available users
        for index, listing_image in enumerate(listing_images_without_owner):
            listing_image.owner = users[index % users.count()]  # Cycle through all users
            listing_image.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully populated {listing_images_without_owner.count()} ListingImage objects with owners."))
