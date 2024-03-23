from django.core.management.base import BaseCommand
from django.db import transaction
from core.comments import Comment, Reply


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
                comment_1 = Comment.objects.create(
                    body="body one", user=1, article=1, status=True
                )
                comment_2 = Comment.objects.create(
                    body="body one", user=1, article=1, status=True
                )
                comment_3 = Comment.objects.create(
                    body="body one", user=2, article=2, status=True
                )
                comment_4 = Comment.objects.create(
                    body="body one", user=4, article=2, status=True
                )
                comment_5 = Comment.objects.create(
                    body="body one", user=4, article=3, status=True
                )

                self.success("comment created.")

                self.warning("creating replies")
                Reply.objects.create(
                    body="body one", user=1, comment_id=comment_1.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=2, comment_id=comment_1.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=4, comment_id=comment_1.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=1, comment_id=comment_2.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=4, comment_id=comment_1.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=1, comment_id=comment_2.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=1, comment_id=comment_3.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=1, comment_id=comment_4.id, status=True
                )
                Reply.objects.create(
                    body="body one", user=1, comment_id=comment_5.id, status=True
                )
                self.success("replies created.")
            except Exception as err:
                self.error(f"please provide email and password {err}")
