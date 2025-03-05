from django.db import models
from pytils.translit import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField

class UnitLen(models.Model):
    name = models.CharField('Длина', max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'Длина'
        verbose_name_plural = 'Длина'


class UnitWidth(models.Model):
    name = models.CharField('Ширина', max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ширина'
        verbose_name_plural = 'Ширина'

class UnitThin(models.Model):
    name = models.CharField('Толщина', max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Толщина'
        verbose_name_plural = 'Толщина'

class MaterialTag(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = 'Тег материала'
        verbose_name_plural = 'Теги материалов'

class MaterialRecommend(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = 'Материал рекомендуется для'
        verbose_name_plural = 'Материал рекомендуется для'

class Material(models.Model):
    image = ResizedImageField(size=[480, 320], quality=100, force_format='WEBP', upload_to='shop/product/material',
                              blank=False, null=True)
    tags = models.ManyToManyField(MaterialTag, blank=True)
    recommend = models.ManyToManyField(MaterialRecommend, blank=True)
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255, blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:

        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Category(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    image = ResizedImageField(size=[420, 420], quality=100, force_format='WEBP', upload_to='shop/category/images',
                              blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255,blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False)
    display_amount = models.IntegerField(default=0, blank=True, null=True)

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
    article = models.CharField('Артикул', max_length=20,blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_lower = models.CharField('Название', max_length=255, blank=False, null=True, editable=False)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    subcategory = models.ForeignKey(SubCategory,blank=True,null=True,on_delete=models.CASCADE, related_name='products')
    material = models.ForeignKey(Material,blank=True,null=True,on_delete=models.CASCADE, related_name='material_products')
    display_price = models.CharField('Цена на карточке', max_length=20,blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    description = CKEditor5Field('Описание', blank=True, null=True, config_name='extends')

    can_cut = models.BooleanField('Нарезка',default=False, null=False)
    is_active = models.BooleanField('Активен',default=True, null=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.name_lower = self.name.lower()
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

        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='features')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Параметр на карточке'
        verbose_name_plural = 'Параметры на карточке'

class ProductFeatureDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='features_detail')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Параметр на странице товара'
        verbose_name_plural = 'Параметры на странице товара'


class ProductUnit(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='units')
    thin = models.ForeignKey('UnitThin', on_delete=models.CASCADE, null=True, blank=False, verbose_name='Толщина')
    width = models.ForeignKey('UnitWidth', on_delete=models.CASCADE, null=True, blank=False, verbose_name='Ширина')
    length = models.ForeignKey('UnitLen', on_delete=models.CASCADE, null=True, blank=False, verbose_name='Длина')

    price = models.IntegerField('Цена',default=0, blank=False, null=True)
    price_description = models.CharField('Описание цены', max_length=255, blank=True, null=True)
    add_price = models.CharField('Доп. цена', max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.thin.name}x{self.width.name}x{self.length.name}'

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