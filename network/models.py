from django.db import models


class NetworkNode(models.Model):
    LEVEL_CHOICES = (
        (0, 'Factory'),
        (1, 'Retail Network'),
        (2, 'Individual Entrepreneur'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, editable=False)

    def save(self, *args, **kwargs):

        self.level = self.calculate_level()
        super().save(*args, **kwargs)

    def calculate_level(self):

        if self.supplier is None:
            return 0  # Завод
        elif self.supplier.level == 0:
            return 1  # Розничная сеть
        else:
            return 2  # Индивидуальный предприниматель

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'Узел сети'
    verbose_name_plural = 'Узлы сети'


class Product(models.Model):
    network_node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE,
                                     verbose_name='Узел сети')
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
