from django.core.management.base import BaseCommand
from .models import CustomUser  # Import your CustomUser model
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake users'

    def handle(self, *args, **kwargs):
        for _ in range(20):  # Create 20 fake users
            email = fake.email()
            first_name = fake.first_name()
            last_name = fake.last_name()
            is_staff = random.choice([True, False])
            is_active = True  # Users will be active by default
            date_joined = fake.date_time_this_year()

            CustomUser.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_staff=is_staff,
                is_active=is_active,
                date_joined=date_joined,
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake users'))
