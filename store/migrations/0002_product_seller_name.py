# Generated by Django 4.0.4 on 2022-05-29 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Seller_Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]