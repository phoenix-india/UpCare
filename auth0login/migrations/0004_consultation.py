# Generated by Django 3.0.5 on 2020-06-20 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth0login', '0003_auto_20200619_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('symptoms', models.TextField()),
            ],
        ),
    ]
