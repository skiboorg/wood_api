# Generated by Django 5.1 on 2024-08-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_created_at_order_is_deliveried_order_is_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан'),
        ),
    ]
