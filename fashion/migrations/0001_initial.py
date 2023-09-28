# Generated by Django 4.1.2 on 2023-07-18 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bluemartin', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fashion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fashion_category', models.CharField(max_length=20)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bluemartin.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex')], default='Unisex', max_length=10, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('haggle', models.CharField(choices=[('Negotiable', 'Negotiable'), ('Unnegotiable', 'Unnegotiable')], default='Negotiable', max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='image')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='image')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='image')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='fashion.fashion')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.vendor')),
                ('sizes', models.ManyToManyField(blank=True, to='fashion.size')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
