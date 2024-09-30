from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from homes.models import Profile, Language  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Populate remaining fields in the Profile model for all users'

    def handle(self, *args, **kwargs):
        # Get the user model
        User = get_user_model()

        # Get the languages that have already been populated
        try:
            english = Language.objects.get(name='English')
            spanish = Language.objects.get(name='Spanish')
            french = Language.objects.get(name='French')
            german = Language.objects.get(name='German')
        except Language.DoesNotExist:
            self.stdout.write(self.style.ERROR("Some languages are missing in the database."))
            return

        # Fetch all users and populate their profiles
        users = User.objects.all()

        for user in users:
            # Create or get the profile for each user
            profile, created = Profile.objects.get_or_create(user=user)

            # Populate the profile with some data (customize this as needed)
            if created or not profile.country:
                profile.country = 'USA' if user.email.endswith('.com') else 'Spain'
            if created or not profile.city_or_state:
                profile.city_or_state = 'California' if user.email.endswith('.com') else 'Madrid'
            if not profile.bio:
                profile.bio = f"This is the bio for {user.email}"

            # Assign languages (you can change this logic as needed)
            if not profile.languages.exists():
                if user.email.endswith('.com'):
                    profile.languages.set([english, spanish])
                else:
                    profile.languages.set([french, german])

            # Set superhost status
            if not profile.is_superhost:
                profile.is_superhost = False

            # Save the profile
            profile.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated profiles for all users.'))
