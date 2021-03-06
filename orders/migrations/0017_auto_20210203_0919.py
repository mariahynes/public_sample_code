# Generated by Django 3.1.5 on 2021-02-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_order_shipping_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_discount_code',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Order Discount Code'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_type',
            field=models.CharField(choices=[('TK', 'Tracked'), ('SD', 'Standard'), ('XX', 'Free')], default='TK', max_length=2, verbose_name='Shipping Type'),
            preserve_default=False,
        ),
    ]
