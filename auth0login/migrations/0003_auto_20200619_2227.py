# Generated by Django 3.0.5 on 2020-06-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth0login', '0002_auto_20200619_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(default='image_1.jpg', upload_to='blogs/images/'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(),
        ),
    ]
