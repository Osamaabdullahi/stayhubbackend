
# from django.core.management.base import BaseCommand
# from django.utils import timezone
# from faker import Faker
# from homes.models import Listing, CustomUser  # Replace with your actual app name
# import random

# class Command(BaseCommand):
#     help = 'Populates the Listing model with 50 realistic listings'

#     def handle(self, *args, **kwargs):
#         # Predefined realistic titles
    
#         # Initialize Faker
#         fake = Faker()

#         # Example images for listings
      
#         # List of categories
       

#         # Get all users to assign as owners
        # owners = CustomUser.objects.all()
        # if owners.count() == 0:
        #     self.stdout.write(self.style.ERROR('No users found. Please populate users first.'))
        #     return

#         # Create 50 listings
#         for i in range(50):
#             listing = Listing.objects.create(
#                 owner=random.choice(owners),  # Assign a random user as the owner
#                 title=titles[i],  # Use predefined realistic titles
#                 description=fake.paragraph(nb_sentences=5),  # Generate fake description
#                 address=fake.street_address(),  # Generate fake address
#                 city=fake.city(),  # Generate fake city
#                 state=fake.state(),  # Generate fake state
#                 country=fake.country(),  # Generate fake country
#                 price_per_night=round(random.uniform(50, 500), 2),  # Random price
#                 max_guests=random.randint(1, 10),  # Random max guests
#                 bedrooms=random.randint(1, 5),  # Random bedrooms
#                 bathrooms=random.randint(1, 3),  # Random bathrooms
#                 created_at=timezone.now(),
#                 updated_at=timezone.now(),
#                 is_available=random.choice([True, False]),  # Random availability
#                 mainImage_url=random.choice(images),  # Assign random image URL
#                 category=random.choice(categories)  # Assign random category
#             )

#             self.stdout.write(self.style.SUCCESS(f'Successfully created listing: {listing.title}'))

#         self.stdout.write(self.style.SUCCESS('Successfully populated Listing model with 50 listings.'))


# list= [
# "Beach house" ,
#  "Castles" ,
# "Amazing views",
# "Amazing pools" ,
#  "Tropical" ,
# "National parks" ,
# "Lakefront" ,
# "Campers" ,
#   "Islands" ,
# "top cities!" ,
# "Beach" ,
#  "Design" ,
#  "historical "
# ]



from django.core.management.base import BaseCommand
from django.utils import timezone
from homes.models import Listing, CustomUser  # Replace with your actual app name
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Populates the Listing model with realistic listings'

    def handle(self, *args, **kwargs):
        fake = Faker() 
        # List of dictionaries containing titles, categories, and images
        data_with_titles = [
            {
                "title": "Dreamy Castles",
                "category": "Castles",
                "image": "https://i.pinimg.com/474x/0f/05/b9/0f05b9c04e4ed09cfd9a7f7c410af0de.jpg",
            },
            {
                "title": "Exquisite Tropical Retreats",
                "category": "Tropical",
                "image": "https://i.pinimg.com/474x/83/1f/e7/831fe7cdc27fcbe558961dbf05956e01.jpg",
            },
            {
                "title": "Luxury Lakefront Villas",
                "category": "Lakefront",
                "image": "https://i.pinimg.com/474x/cc/49/95/cc4995ec34d816adb57e7dd772e9be15.jpg",
            },
            {
                "title": "Secluded Island Escapes",
                "category": "Islands",
                "image": "https://i.pinimg.com/474x/b1/2b/06/b12b061ddc4849688fe67ecd45ff9777.jpg",
            },
            {
                "title": "Serene Beach Houses",
                "category": "Beach house",
                "image": "https://i.pinimg.com/564x/f7/a4/9f/f7a49f2386fe3bf237ef55e23621652e.jpg",
            },
            {
                "title": "Adventures in National Parks",
                "category": "National parks",
                "image": "https://i.pinimg.com/474x/66/ed/ad/66edad5606a7fbe60918232b30103001.jpg",
            },
            {
                "title": "Charming Campers Getaways",
                "category": "Campers",
                "image": "https://i.pinimg.com/474x/f2/bb/54/f2bb5468ebe284d5b04c4146b8b4f30d.jpg",
            },
            {
                "title": "Breathtaking Amazing Views",
                "category": "Amazing views",
                "image": "https://i.pinimg.com/474x/db/f1/6a/dbf16a9cf4ffcaee5f00a01aaa58ccd0.jpg",
            },
            {
                "title": "Top Cities to Explore",
                "category": "Top cities!",
                "image": "https://i.pinimg.com/474x/fb/34/1a/fb341ad7e39dc8f98ad2b25928bc08d8.jpg",
            },
            {
                "title": "Best Beach Adventures",
                "category": "Beach",
                "image": "https://i.pinimg.com/474x/b1/2b/06/b12b061ddc4849688fe67ecd45ff9777.jpg",
            },
            {
                "title": "Discover Historical Landmarks",
                "category": "Historical",
                "image": "https://i.pinimg.com/474x/b4/e5/f8/b4e5f8aa97491ccedaf9bd966bfcf5cd.jpg",
            },
            {
                "title": "Stunning Design Homes",
                "category": "Design",
                "image": "https://i.pinimg.com/474x/fb/de/f4/fbdef43a1d5a49bade4d736d240497c4.jpg",
            },
            {
                "title": "Grand Beachfront Villas",
                "category": "Beach house",
                "image": "https://i.pinimg.com/474x/7c/8c/cc/7c8ccc2adf21b0736c84cd8c2226d4f1.jpg",
            },
            {
                "title": "Gorgeous Island Villas",
                "category": "Islands",
                "image": "https://i.pinimg.com/474x/d9/6a/9a/d96a9a9ed96a57d332efb0655f7ef549.jpg",
            },
            {
                "title": "Hidden Historical Gems",
                "category": "Historical",
                "image": "https://i.pinimg.com/474x/ca/3f/2c/ca3f2c6024e2d92c1e8e46c06c677a89.jpg",
            },
            {
                "title": "Elegant Tropical Getaways",
                "category": "Tropical",
                "image": "https://i.pinimg.com/474x/55/ef/39/55ef39c02be12735f36f69c7cae292d1.jpg",
            },
            {
                "title": "Unique Camper Experiences",
                "category": "Campers",
                "image": "https://i.pinimg.com/474x/9b/54/ad/9b54ad090a2b8230a6c8266db42c0c53.jpg",
            },
            {
                "title": "Magical Castle Retreats",
                "category": "Castles",
                "image": "https://i.pinimg.com/474x/41/48/37/4148373670cce590cb0f73544edefcf7.jpg",
            },
            {
                "title": "Scenic National Park Cabins",
                "category": "National parks",
                "image": "https://i.pinimg.com/474x/25/82/d1/2582d13c85b5ea2638456d85e47c1be8.jpg",
            },
            {
                "title": "Beach House Heaven",
                "category": "Beach house",
                "image": "https://i.pinimg.com/474x/85/37/90/853790e7d4334c8ae80688cd449de4d9.jpg",
            },
            {
                "title": "Luxury Island Living",
                "category": "Islands",
                "image": "https://i.pinimg.com/474x/74/1a/50/741a50083b01f57e0eb42dd1175b5d09.jpg",
            },
            {
                "title": "Majestic Historical Homes",
                "category": "Historical",
                "image": "https://i.pinimg.com/474x/b3/8c/00/b38c0099fd56a00281c7ae8aa4424a61.jpg",
            },
            {
                "title": "Stunning Lakefront Retreats",
                "category": "Lakefront",
                "image": "https://i.pinimg.com/474x/89/2e/d8/892ed82e7f670646fb135b61d7a358e2.jpg",
            },
            {
                "title": "Cozy Camper Cabins",
                "category": "Campers",
                "image": "https://i.pinimg.com/474x/36/0c/6a/360c6af623b5a32a81d2a21ad722080b.jpg",
            },
            {
                "title": "Peaceful National Park Homes",
                "category": "National parks",
                "image": "https://i.pinimg.com/474x/d4/31/7d/d4317de926a6c0f59608a915ab6067f0.jpg",
            },
            {
                "title": "Sunset Views in Top Cities",
                "category": "Top cities!",
                "image": "https://i.pinimg.com/474x/ec/73/3b/ec733bf00beb0235731122dad71333a9.jpg",
            },
            {
                "title": "Luxurious Beach Houses",
                "category": "Beach",
                "image": "https://i.pinimg.com/474x/8e/66/40/8e664076d35fa371e032a83d12af84d6.jpg",
            },
            {
                "title": "Design Lovers' Dream Homes",
                "category": "Design",
                "image": "https://i.pinimg.com/474x/f6/06/8a/f6068a17944ad61396f4b3c28c106bad.jpg",
            },
            {
                "title": "Historical Heritage Homes",
                "category": "Historical",
                "image": "https://i.pinimg.com/474x/69/7a/63/697a6340b16dc821e44e2f8fa81267a0.jpg",
            },
            {
                "title": "Spectacular Lakefront Getaways",
                "category": "Lakefront",
                "image": "https://i.pinimg.com/474x/a4/ca/54/a4ca544fb2afc28b8087d46b4245c49e.jpg",
            },
            {
                "title": "Charming Beach Towns",
                "category": "Beach house",
                "image": "https://i.pinimg.com/474x/66/d1/cc/66d1cc205230ea89144b29cbe5f9d886.jpg",
            },
            {
                "title": "Breathtaking Desert Retreats",
                "category": "Desert",
                "image": "https://i.pinimg.com/474x/77/f2/94/77f294c73e4c94e5931c5b11b39b85c3.jpg",
            },
        ]


        owners = CustomUser.objects.all()
        if owners.count() == 0:
            self.stdout.write(self.style.ERROR('No users found. Please populate users first.'))
            return
        
        # Loop through the data and create Listing objects
        for data in data_with_titles:
            title = data["title"]
            category = data["category"]
            image_url = data["image"]

            # Create a Listing object
            listing = Listing(
                title=title,
                category=category,
                mainImage_url=image_url,
                owner=random.choice(owners),  # Assign a random user as the owner
                description=fake.paragraph(nb_sentences=5),  # Generate fake description
                address=fake.street_address(),  # Generate fake address
                city=fake.city(),  # Generate fake city
                state=fake.state(),  # Generate fake state
                country=fake.country(),  # Generate fake country
                price_per_night=round(random.uniform(50, 500), 2),  # Random price
                max_guests=random.randint(1, 10),  # Random max guests
                bedrooms=random.randint(1, 5),  # Random bedrooms
                bathrooms=random.randint(1, 3),  # Random bathrooms
                created_at=timezone.now(),
                updated_at=timezone.now(),
                is_available=random.choice([True, False]),  # Random availability
               
            )
            listing.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the Listing model with data.'))
