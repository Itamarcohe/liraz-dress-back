# Generated by Django 3.2.12 on 2022-08-20 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('dress_name', models.CharField(max_length=512)),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=1028, null=True)),
                ('image', models.URLField(max_length=512)),
                ('size', models.CharField(blank=True, max_length=128, null=True)),
                ('featured_image', models.URLField(default='https://cdn1.bambinifashion.com/img/p/6/4/9/4/0/8/649408--product-gallery.jpg', max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=512)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=2048)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('customer_name', models.CharField(max_length=512)),
                ('phone_number', models.CharField(max_length=128)),
                ('top_item', models.IntegerField()),
                ('back_item', models.IntegerField()),
                ('bottom_item', models.IntegerField()),
                ('color', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]