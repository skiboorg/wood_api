from django.db import models

class Order(models.Model):
    order_id = models.CharField('Номер заказа', max_length=255, blank=True, null=True)
    customer = models.CharField('ФИО', max_length=255, blank=True, null=True)
    phone = models.CharField('контактный телефон', max_length=255, blank=True, null=True)
    email = models.CharField('почта', max_length=255, blank=True, null=True)
    comment = models.TextField('комментарий к заказу', blank=True, null=True)
    payment_type = models.CharField('тип оплаты', max_length=255, blank=True, null=True)
    delivery_type = models.CharField('тип доставки', max_length=255, blank=True, null=True)
    delivery_address = models.TextField('адрес доставки', blank=True, null=True)
    # @property
    # def total_price(self):
    #     price = 0
    #     for item in self.items.all():
    #         price += item.price * item.amount
    #     return price


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    article = models.CharField('Артикул', max_length=255, blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    unit = models.CharField('Ед. измерения', max_length=255, blank=False, null=True)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)
    amount = models.IntegerField(default=0, blank=True, null=True)

