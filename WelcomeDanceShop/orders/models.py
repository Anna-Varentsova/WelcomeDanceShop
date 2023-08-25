from django.db import models
from goods.models import Goods


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField()
    address = models.CharField(max_length=255, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменён')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']),]
        verbose_name_plural = 'Заказы'
        verbose_name = 'заказы'

    def __str__(self):
        return f'Заказ {self.pk}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Goods, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        ordering = ['-order']
        verbose_name_plural = 'Товары в заказе'
        verbose_name = 'товары в заказе'

    def __str__(self):
        return str(self.pk)

    def get_cost(self):
        return self.price * self.quantity

