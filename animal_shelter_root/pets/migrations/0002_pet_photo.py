# Generated by Django 4.0.4 on 2022-06-06 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='photo',
            field=models.ImageField(default='photos/default_photo.jpg', upload_to='photos', verbose_name='Фото'),
        ),
    ]