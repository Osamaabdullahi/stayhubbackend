from django.core.management.base import BaseCommand
from django.utils import timezone
from homes.models import Listing, Review
from homes.models import CustomUser  # Assuming CustomUser is in a users app
import random

class Command(BaseCommand):
    help = 'Populates the Review model with sample data for existing listings and users'

    def handle(self, *args, **kwargs):
        # Get all listings
        listings = Listing.objects.all()

        # Get all users
        users = CustomUser.objects.all()

        if not listings.exists():
            self.stdout.write(self.style.ERROR('No listings found.'))
            return

        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found.'))
            return

        # Prepare sample review comments and ratings
        review_comments = [
            'Amazing place! Highly recommended.',
            'Very comfortable stay, just a bit noisy.',
            'Average experience, could have been better.',
            'Loved the place! Will visit again.',
            'Not what I expected, too far from the city.',
            'A perfect stay with great amenities.',
            'The host was super helpful!',
            'Beautiful views, but the apartment was too small.',
        ]

        # Iterate through listings and assign random users to create reviews
        for listing in listings:
            # Create a random number of reviews for each listing (between 1 and 3)
            num_reviews = random.randint(1, 3)

            for _ in range(num_reviews):
                # Randomly select a user to review this listing
                user = random.choice(users)

                # Generate a random rating (between 1 and 5)
                rating = random.randint(1, 5)

                # Select a random review comment
                comment = random.choice(review_comments)

                # Create the review
                review, created = Review.objects.get_or_create(
                    user=user,
                    listing=listing,
                    rating=rating,
                    comment=comment,
                    defaults={'created_at': timezone.now(), 'updated_at': timezone.now()}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Review for {listing.title} by {user.email} created.'))
                else:
                    self.stdout.write(self.style.WARNING(f'Review for {listing.title} by {user.email} already exists.'))

        self.stdout.write(self.style.SUCCESS('Sample reviews populated successfully.'))
