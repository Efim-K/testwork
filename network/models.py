from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class Product(models.Model):
    """ Электронный товар """

    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель", **NULLABLE)
    release_date = models.DateField(verbose_name="Дата выхода на рынок", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class SalesNetwork(models.Model):
    """ Сеть по продажам электроники """

    NETWORK_CHOICES = (
        ('FA', "Завод"),
        ('NW', "Розничная сеть"),
        ('IE', "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=255, unique=True, verbose_name="Название")
    network_type = models.CharField(max_length=2, default='FA', choices=NETWORK_CHOICES,
                                    verbose_name="Тип сети продаж")
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронный адрес", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="Страна", **NULLABLE)
    city = models.CharField(max_length=100, verbose_name="Город", **NULLABLE)
    street = models.CharField(max_length=100, verbose_name="Улица", **NULLABLE)
    house_number = models.CharField(max_length=10, verbose_name="Номер дома", **NULLABLE)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name="Продукты", **NULLABLE)
    supplier = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Поставщик", **NULLABLE)
    debt = models.DecimalField(default=0, max_digits=20, decimal_places=2,
                               verbose_name="Задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сеть по продажам электроники"
        verbose_name_plural = "Сети по продажам электроники"
        ordering = ["name"]
