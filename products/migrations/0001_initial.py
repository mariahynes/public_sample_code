# Generated by Django 3.1.5 on 2021-01-12 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_display_name', models.CharField(max_length=255, verbose_name='Name of Account')),
                ('stock_manufactured', models.PositiveSmallIntegerField(default=0, verbose_name='Manufactured')),
                ('product_image_1', models.ImageField(blank=True, null=True, upload_to='shady_dog_product_images', verbose_name='Product Image 1')),
                ('product_image_2', models.ImageField(blank=True, null=True, upload_to='shady_dog_product_images', verbose_name='Product Image 2')),
                ('product_image_3', models.ImageField(blank=True, null=True, upload_to='shady_dog_product_images', verbose_name='Product Image 3')),
                ('product_image_4', models.ImageField(blank=True, null=True, upload_to='shady_dog_product_images', verbose_name='Product Image 4')),
                ('product_image_1_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product Image 1 Description')),
                ('product_image_2_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product Image 2 Description')),
                ('product_image_3_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product Image 3 Description')),
                ('product_image_4_desc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Product Image 4 Description')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('is_activated', models.BooleanField(blank=True, default=False, verbose_name='is this product activated?')),
            ],
        ),
    ]
