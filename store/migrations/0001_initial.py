# Generated by Django 4.0.4 on 2022-05-29 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category Title')),
                ('slug', models.SlugField(max_length=55, verbose_name='Category Slug')),
                ('description', models.TextField(blank=True, verbose_name='Category Description')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Category Image')),
                ('is_active', models.BooleanField(verbose_name='Is Active?')),
                ('is_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Product Title')),
                ('slug', models.SlugField(max_length=160, verbose_name='Product Slug')),
                ('sku', models.CharField(max_length=255, unique=True, verbose_name='Unique Product ID (SKU)')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('detail_description', models.TextField(blank=True, null=True, verbose_name='Detail Description')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Product Image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(verbose_name='Is Active?')),
                ('is_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Product Categoy')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
    ]
