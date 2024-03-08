from django.core.management.base import BaseCommand
from django.db import transaction
from core.category import Category
from core.post import Post


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
                self.warning("creating categories")
                cat_1 = Category.objects.create(name="category one", slug="category-one")
                cat_2 =Category.objects.create(name="category two", slug="category-two")
                cat_3 =Category.objects.create(name="category three", slug="category-three")
                cat_4 =Category.objects.create(name="category four", slug="category-four")
                cat_5 =Category.objects.create(name="category five", slug="category-five")
                cat_6 =Category.objects.create(name="category six", slug="category-six")
                self.success("categories created.")

                self.warning("creating posts")
                post_1 = Post.objects.create(
                    title="title one",
                    banner="https://loremflickr.com/320/240",
                    video_link="https://www.youtube.com/watch?v=9bZkp7q19f0",
                    content="content one",
                    summary="summary one",
                    created_at="2021-09-01 00:00:00",
                    updated_at="2021-09-01 00:00:00",
                    author=2
                )
                post_1.category.set([cat_1.id, cat_2.id])
                post_2 = Post.objects.create(
                    title="title one",
                    banner="https://loremflickr.com/320/240",
                    video_link="https://www.youtube.com/watch?v=9bZkp7q19f0",
                    content="content one",
                    summary="summary one",
                    created_at="2021-09-01 00:00:00",
                    updated_at="2021-09-01 00:00:00",
                    author=10,
                )
                post_2.category.set([cat_3.id, cat_4.id])
                post_3 = Post.objects.create(
                    title="title one",
                    banner="https://loremflickr.com/320/240",
                    video_link="https://www.youtube.com/watch?v=9bZkp7q19f0",
                    content="content one",
                    summary="summary one",
                    created_at="2021-09-01 00:00:00",
                    updated_at="2021-09-01 00:00:00",
                    author=11,
                )
                post_3.category.set([cat_5.id, cat_6.id, cat_1.id])
                self.success("articles created.")
            except Exception as err:
                self.error(f"please provide email and password {err}")
