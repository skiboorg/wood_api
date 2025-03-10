from django.db import models
from django_resized import ResizedImageField

from shop.models import Product


class CallbackForm(models.Model):

    name = models.CharField('Имя',max_length=255,blank=False, null=True)
    phone= models.CharField('Телефон',max_length=255,blank=False, null=True)
    product= models.CharField('Заказ',max_length=255,blank=False, null=True)

    is_done = models.BooleanField('Обработана', default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Banner(models.Model):
    order_num = models.IntegerField(default=10)
    image_big = ResizedImageField('Баннер десктоп', size=[1440, 640], quality=95, force_format='WEBP', upload_to='banner/images',
                              blank=False, null=True)
    image_small = ResizedImageField('Баннер мобилка', size=[760, 640], quality=95, force_format='WEBP',
                                 upload_to='banner/images',
                                 blank=False, null=True)
    text_big = models.TextField('Текст большой', blank=True, null=True)
    text_small = models.TextField('Текст маленький', blank=True, null=True)
    def __str__(self):
        return f'{self.order_num}'



    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['order_num']


class Faq(models.Model):
    order_num = models.IntegerField(default=10)
    question = models.CharField('Вопрос',max_length=255,blank=False, null=True)
    answer = models.TextField('Ответ', blank=False, null=True)
    def __str__(self):
        return f'{self.question}'
    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = 'Faq'
        ordering = ['order_num']