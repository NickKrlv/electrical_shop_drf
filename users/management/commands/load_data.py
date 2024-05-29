from django.core.management.base import BaseCommand
from django.db import connection
from users.models import User
from network.models import NetworkNode, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Очистка таблиц
        with connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE TABLE users_user, network_networknode, network_product RESTART IDENTITY CASCADE;")

        # Создание администратора
        admin = User.objects.create(email="admin@example.com", password="admin", is_superuser=True, is_staff=True)
        admin.set_password("admin")
        admin.save()

        # Создание активных пользователей
        active_user1 = User.objects.create(email="active1@example.com", password="password", is_active=True)
        active_user1.set_password("password")
        active_user1.save()

        active_user2 = User.objects.create(email="active2@example.com", password="password", is_active=True)
        active_user2.set_password("password")
        active_user2.save()

        # Создание неактивных пользователей
        inactive_user1 = User.objects.create(email="inactive1@example.com", password="password", is_active=False)
        inactive_user1.set_password("password")
        inactive_user1.save()

        inactive_user2 = User.objects.create(email="inactive2@example.com", password="password", is_active=False)
        inactive_user2.set_password("password")
        inactive_user2.save()

        # Создание заводов (уровень 0)
        factory1 = NetworkNode.objects.create(
            name="Factory 1",
            email="factory1@example.com",
            country="USA",
            city="New York",
            street="Factory Street",
            house_number="1",
            debt_to_supplier=0
        )

        factory2 = NetworkNode.objects.create(
            name="Factory 2",
            email="factory2@example.com",
            country="Germany",
            city="Berlin",
            street="Factory Street",
            house_number="2",
            debt_to_supplier=0
        )

        # Создание розничных сетей (уровень 1)
        retail1 = NetworkNode.objects.create(
            name="Retail Network 1",
            email="retail1@example.com",
            country="USA",
            city="Los Angeles",
            street="Retail Street",
            house_number="10",
            supplier=factory1,
            debt_to_supplier=1000.50
        )

        retail2 = NetworkNode.objects.create(
            name="Retail Network 2",
            email="retail2@example.com",
            country="Germany",
            city="Munich",
            street="Retail Street",
            house_number="20",
            supplier=factory2,
            debt_to_supplier=2000.75
        )

        retail3 = NetworkNode.objects.create(
            name="Retail Network 3",
            email="retail3@example.com",
            country="USA",
            city="San Francisco",
            street="Retail Street",
            house_number="30",
            supplier=factory1,
            debt_to_supplier=1500.25
        )

        # Создание индивидуальных предпринимателей (уровень 2)
        entrepreneur1 = NetworkNode.objects.create(
            name="Entrepreneur 1",
            email="entrepreneur1@example.com",
            country="USA",
            city="Chicago",
            street="Entrepreneur Street",
            house_number="100",
            supplier=retail1,
            debt_to_supplier=500.00
        )

        entrepreneur2 = NetworkNode.objects.create(
            name="Entrepreneur 2",
            email="entrepreneur2@example.com",
            country="Germany",
            city="Hamburg",
            street="Entrepreneur Street",
            house_number="200",
            supplier=retail2,
            debt_to_supplier=750.00
        )

        entrepreneur3 = NetworkNode.objects.create(
            name="Entrepreneur 3",
            email="entrepreneur3@example.com",
            country="USA",
            city="Seattle",
            street="Entrepreneur Street",
            house_number="300",
            supplier=retail3,
            debt_to_supplier=600.00
        )

        entrepreneur4 = NetworkNode.objects.create(
            name="Entrepreneur 4",
            email="entrepreneur4@example.com",
            country="USA",
            city="Houston",
            street="Entrepreneur Street",
            house_number="400",
            supplier=retail1,
            debt_to_supplier=700.00
        )

        entrepreneur5 = NetworkNode.objects.create(
            name="Entrepreneur 5",
            email="entrepreneur5@example.com",
            country="Germany",
            city="Stuttgart",
            street="Entrepreneur Street",
            house_number="500",
            supplier=retail2,
            debt_to_supplier=800.00
        )

        # Создание продуктов для каждого узла
        products_data = [
            (factory1, "Product A1", "Model X1", "2022-01-01"),
            (factory1, "Product A2", "Model X2", "2023-01-01"),
            (factory2, "Product B1", "Model Y1", "2022-02-01"),
            (factory2, "Product B2", "Model Y2", "2023-02-01"),
            (retail1, "Product C1", "Model Z1", "2022-03-01"),
            (retail1, "Product C2", "Model Z2", "2023-03-01"),
            (retail2, "Product D1", "Model W1", "2022-04-01"),
            (retail2, "Product D2", "Model W2", "2023-04-01"),
            (retail3, "Product E1", "Model V1", "2022-05-01"),
            (retail3, "Product E2", "Model V2", "2023-05-01"),
            (entrepreneur1, "Product F1", "Model U1", "2022-06-01"),
            (entrepreneur1, "Product F2", "Model U2", "2023-06-01"),
            (entrepreneur2, "Product G1", "Model T1", "2022-07-01"),
            (entrepreneur2, "Product G2", "Model T2", "2023-07-01"),
            (entrepreneur3, "Product H1", "Model S1", "2022-08-01"),
            (entrepreneur3, "Product H2", "Model S2", "2023-08-01"),
            (entrepreneur4, "Product I1", "Model R1", "2022-09-01"),
            (entrepreneur4, "Product I2", "Model R2", "2023-09-01"),
            (entrepreneur5, "Product J1", "Model Q1", "2022-10-01"),
            (entrepreneur5, "Product J2", "Model Q2", "2023-10-01"),
        ]

        for node, name, model, release_date in products_data:
            Product.objects.create(
                network_node=node,
                name=name,
                model=model,
                release_date=release_date
            )
