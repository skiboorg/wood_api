# Generated by Django 5.1 on 2024-08-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_short_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productunit',
            options={'ordering': ('order_num',), 'verbose_name': 'Фасовка', 'verbose_name_plural': 'Фасовка'},
        ),
        migrations.AddField(
            model_name='product',
            name='display_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='productunit',
            name='order_num',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
