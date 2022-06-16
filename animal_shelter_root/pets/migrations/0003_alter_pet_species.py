# Generated by Django 4.0.4 on 2022-06-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(choices=[('CAT', 'Кот'), ('DOG', 'Собака'), ('PRT', 'Попугай')], default='CAT', max_length=3, verbose_name='Вид'),
        ),
    ]