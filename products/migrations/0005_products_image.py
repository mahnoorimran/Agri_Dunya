# Generated by Django 3.2.6 on 2022-05-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]