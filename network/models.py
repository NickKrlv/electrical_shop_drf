from django.db import models
from django.utils import timezone


class NetworkNode(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Узел сети'
        verbose_name_plural = 'Узлы сети'


class Product(models.Model):
    network_node = models.ForeignKey(NetworkNode, related_name='products', on_delete=models.CASCADE, verbose_name='Узел сети')
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
