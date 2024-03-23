from django.core.management.base import BaseCommand
from django.db import transaction
from core.user import User
from core.profile import Profile


class Command(BaseCommand):
    help = "provide user name and password"

    def success(self, message):
        return self.stdout.write(self.style.SUCCESS(message))

    def warning(self, message):
        return self.stdout.write(self.style.WARNING(message))

    def error(self, message):
        return self.stdout.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        self.warning(
            "if something goes wrong after installations, \n"
            "please use develop environment: \n"
            "docker-compose exec api python manage.py flush"
        )

        with transaction.atomic():
            try:
                self.warning("creating admin user")
                User.objects.create_superuser("admin@mrcode.com", "admin2024")
                self.success("admin user created successfully.")
                self.success("creating users creators")
                user_1 = User.objects.create_user(
                    email="jhon@yopmail.com",
                    password="me123456",
                    first_name="jhon",
                    last_name="doe",
                    is_active=True,
                    user_type=2,
                )

                user_2 = User.objects.create_user(
                    email="azumi@yopmail.com",
                    password="me123456",
                    first_name="azumi",
                    last_name="doe",
                    is_active=True,
                    user_type=2,
                )
                self.success("users creators created.")
                self.warning("creating profiles for users")
                Profile.objects.create(
                    user=user_1,
                    bio="I am a software developer",
                    location="Nairobi, Kenya",
                )
                Profile.objects.create(
                    user=user_2,
                    bio="I am a software developer",
                    location="Nairobi, Kenya",
                )
            except Exception as err:
                self.error(f"please provide email and password {err}")
