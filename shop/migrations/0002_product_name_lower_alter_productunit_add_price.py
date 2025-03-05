# Generated by Django 5.1.6 on 2025-03-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_lower',
            field=models.CharField(editable=False, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productunit',
            name='add_price',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Доп. цена'),
        ),
    ]
