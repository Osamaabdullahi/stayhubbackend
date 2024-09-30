# messages/management/commands/populate_messages.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from homes.models import Message
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the Message model with sample messages'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Retrieve all users
        users = list(User.objects.all())
        if len(users) < 2:
            self.stdout.write(self.style.WARNING('Not enough users to create messages.'))
            return

        for _ in range(50):  # Adjust the number of messages as needed
            sender = random.choice(users)
            receiver = random.choice([user for user in users if user != sender])
            content = fake.text(max_nb_chars=200)
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=content
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the Message model.'))
