from django.db import models
from pytils.translit import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField

class Category(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    image = ResizedImageField(size=[420, 420], quality=95, force_format='WEBP', upload_to='shop/category/images',
                              blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255,blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True, related_name='sub_categories')
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255,blank=True, null=True)
    image = ResizedImageField(size=[420, 420], quality=95, force_format='WEBP', upload_to='shop/category/images',
                              blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Product(models.Model):
    article = models.CharField('Артикул',max_length=20,blank=True, null=True)
    order_num = models.IntegerField(default=1, null=True)
    subcategory = models.ForeignKey(SubCategory,blank=True,null=True,on_delete=models.CASCADE, related_name='products')
    is_new = models.BooleanField('Новинка', default=False, null=False)
    is_in_stock = models.BooleanField('В наличии?', default=True, null=False)
    is_popular = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(default=True, null=False)
    display_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ',max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    description = CKEditor5Field('Описание', blank=True, null=True, config_name='extends')


    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='images')
    image = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/product/images',
                              blank=False, null=True)
    is_main = models.BooleanField('Основное', default=False, null=False)

    def __str__(self):
        return f''

    class Meta:

        verbose_name = 'Доп. изображение товара'
        verbose_name_plural = 'Доп. изображения товара'


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='features')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class ProductUnit(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='units')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Ед. измерения', max_length=255, blank=False, null=True)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)
    price_description = CKEditor5Field('Доп. описание цены', blank=True, null=True, config_name='extends')
    is_decimal_price = models.BooleanField('Цена дробная', default=False, null=False)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Фасовка'
        verbose_name_plural = 'Фасовка'


class Service(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    image = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/product/images',
                                   blank=False, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('Описание', blank=True, null=True, config_name='extends')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ServicePrice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='prices')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'