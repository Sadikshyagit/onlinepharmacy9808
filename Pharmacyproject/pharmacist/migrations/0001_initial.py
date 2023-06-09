# Generated by Django 3.1 on 2023-05-20 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharamcist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=200, null=True)),
                ('license_number', models.CharField(blank=True, max_length=200, null=True)),
                ('company_pic', models.ImageField(upload_to='products')),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
