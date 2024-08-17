from django.db import models
from decimal import Decimal
class Order(models.Model):
    order_id = models.CharField('Номер заказа', max_length=255, blank=True, null=True)
    customer = models.CharField('ФИО', max_length=255, blank=True, null=True)
    phone = models.CharField('контактный телефон', max_length=255, blank=True, null=True)
    email = models.CharField('почта', max_length=255, blank=True, null=True)
    comment = models.TextField('комментарий к заказу', blank=True, null=True)
    payment_type = models.CharField('тип оплаты', max_length=255, blank=True, null=True)
    delivery_type = models.CharField('тип доставки', max_length=255, blank=True, null=True)
    delivery_address = models.TextField('адрес доставки', blank=True, null=True)
    created_at = models.DateTimeField('Создан',auto_now_add=True, null=True)
    is_paid = models.BooleanField('Оплачен', default=False, null=False)
    is_done = models.BooleanField('Обработан', default=False, null=False)
    is_deliveried = models.BooleanField('Доставлен', default=False, null=False)

    @property
    def total_price(self):
        price = 0
        for item in self.items.all():
            price += Decimal(item.price) * item.amount
        return price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    article = models.CharField('Артикул', max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    unit = models.CharField('Ед. измерения', max_length=255, blank=False, null=True)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)

