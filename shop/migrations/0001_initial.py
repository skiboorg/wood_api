# Generated by Django 5.1.6 on 2025-03-05 05:52

import django.db.models.deletion
import django_ckeditor_5.fields
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[420, 420], upload_to='shop/category/images')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, verbose_name='ЧПУ')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('html_content', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='SEO текст')),
                ('display_amount', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('order_num',),
            },
        ),
        migrations.CreateModel(
            name='MaterialRecommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='ЧПУ')),
            ],
            options={
                'verbose_name': 'Материал рекомендуется для',
                'verbose_name_plural': 'Материал рекомендуется для',
            },
        ),
        migrations.CreateModel(
            name='MaterialTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='ЧПУ')),
            ],
            options={
                'verbose_name': 'Тег материала',
                'verbose_name_plural': 'Теги материалов',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[800, 600], upload_to='shop/product/images')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('slug', models.CharField(blank=True, editable=False, help_text='Если не заполнено, создается на основе поля Назавание', max_length=255, null=True, verbose_name='ЧПУ')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('html_content', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ('order_num',),
            },
        ),
        migrations.CreateModel(
            name='UnitLen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Длина')),
            ],
            options={
                'verbose_name': 'Длина',
                'verbose_name_plural': 'Длина',
            },
        ),
        migrations.CreateModel(
            name='UnitThin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Толщина')),
            ],
            options={
                'verbose_name': 'Толщина',
                'verbose_name_plural': 'Толщина',
            },
        ),
        migrations.CreateModel(
            name='UnitWidth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ширина')),
            ],
            options={
                'verbose_name': 'Ширина',
                'verbose_name_plural': 'Ширина',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[480, 320], upload_to='shop/product/material')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, verbose_name='ЧПУ')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('html_content', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='SEO текст')),
                ('recommend', models.ManyToManyField(blank=True, to='shop.materialrecommend')),
                ('tags', models.ManyToManyField(blank=True, to='shop.materialtag')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(blank=True, max_length=20, null=True, verbose_name='Артикул')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('slug', models.CharField(blank=True, editable=False, help_text='Если не заполнено, создается на основе поля Назавание', max_length=255, null=True, verbose_name='ЧПУ')),
                ('display_price', models.CharField(blank=True, max_length=20, null=True, verbose_name='Цена на карточке')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Описание')),
                ('can_cut', models.BooleanField(default=False, verbose_name='Нарезка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_products', to='shop.material')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='shop.product')),
            ],
            options={
                'verbose_name': 'Параметр на карточке',
                'verbose_name_plural': 'Параметры на карточке',
            },
        ),
        migrations.CreateModel(
            name='ProductFeatureDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features_detail', to='shop.product')),
            ],
            options={
                'verbose_name': 'Параметр на странице товара',
                'verbose_name_plural': 'Параметры на странице товара',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[800, 600], upload_to='shop/product/images')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основное')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товара',
            },
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Значение')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='shop.service')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=255, null=True, verbose_name='ЧПУ')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[420, 420], upload_to='shop/category/images')),
                ('short_description', models.TextField(blank=True, verbose_name='Короткое описание')),
                ('html_content', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='SEO текст')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='shop.category')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ('order_num',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.subcategory'),
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('price', models.IntegerField(default=0, null=True, verbose_name='Цена')),
                ('price_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание цены')),
                ('add_price', models.CharField(max_length=255, null=True, verbose_name='Доп. цена')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='shop.product')),
                ('length', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.unitlen', verbose_name='Длина')),
                ('thin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.unitthin', verbose_name='Толщина')),
                ('width', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.unitwidth', verbose_name='Ширина')),
            ],
            options={
                'verbose_name': 'Фасовка',
                'verbose_name_plural': 'Фасовка',
                'ordering': ('order_num',),
            },
        ),
    ]
