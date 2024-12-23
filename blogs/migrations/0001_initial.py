# Generated by Django 4.1.2 on 2023-07-18 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30, null=True)),
                ('text', models.TextField()),
                ('whatsapp_url', models.CharField(max_length=100, null=True)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('blog_image2', models.ImageField(blank=True, null=True, upload_to='image')),
                ('blog_image3', models.ImageField(blank=True, null=True, upload_to='image')),
                ('blog_image4', models.ImageField(blank=True, null=True, upload_to='image')),
                ('blog_image5', models.ImageField(blank=True, null=True, upload_to='image')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.vendor')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
