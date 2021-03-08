# Generated by Django 3.1.5 on 2021-01-28 12:34

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210114_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region', models.CharField(choices=[('IE', 'Ireland & Northern Ireland'), ('GB', 'Great Britain'), ('EUR', 'Europe'), ('Z', 'Rest of the World')], default='Z', max_length=3, primary_key=True, serialize=False, verbose_name='Region')),
            ],
        ),
        migrations.CreateModel(
            name='PostageRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_tracked', models.BooleanField(default=False, verbose_name='Tracked Shipping?')),
                ('postage_rate', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Postage Rate')),
                ('postage_rate_max_items', models.PositiveSmallIntegerField(default=5, verbose_name='Maximum number of items for Postage Rate')),
                ('postage_rate_per_extra_item', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Postage Rate per extra item')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.region', verbose_name='Postage Region')),
            ],
        ),
        migrations.CreateModel(
            name='CountryRegion',
            fields=[
                ('country_code', django_countries.fields.CountryField(max_length=2, primary_key=True, serialize=False, verbose_name='Country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.region', verbose_name='Region')),
            ],
        ),
    ]