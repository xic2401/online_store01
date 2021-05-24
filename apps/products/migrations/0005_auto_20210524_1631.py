# Generated by Django 2.2 on 2021-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210524_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pictures',
            field=models.ManyToManyField(blank=True, related_name='product_pictures', to='products.Picture'),
        ),
    ]
