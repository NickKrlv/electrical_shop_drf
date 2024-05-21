from django.db import connection
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE users_user, network_networknode, network_product RESTART IDENTITY CASCADE;")

        admin = User.objects.create(email="admin@example.com", password="admin", is_superuser=True, is_staff=True)
        admin.set_password("admin")
        admin.save()
