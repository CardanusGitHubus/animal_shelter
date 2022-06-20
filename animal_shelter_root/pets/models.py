# import datetime
# from email.policy import default

from django.db import models
# from django.utils import timezone
from PIL import Image


class Pet(models.Model):
    CAT = 'CAT'
    DOG = 'DOG'
    PARROT = 'PRT'
    SPECIES_CHOICES = [
        (CAT, 'Кот'),
        (DOG, 'Собака'),
        (PARROT, 'Попугай'),
    ]

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Самец'),
        (FEMALE, 'Самка')
    ]

    species = models.CharField(  # verbose_name is an optional first positional argument
        verbose_name='Вид',
        max_length=3,
        choices=SPECIES_CHOICES,
        default=CAT,
    )
    name = models.CharField('Имя', max_length=127)
    photo = models.ImageField(
        'Фото', upload_to='photos', default='photos/default_photo.jpg')
    gender = models.CharField(
        verbose_name='Пол',
        max_length=6,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    breed = models.CharField('Порода', max_length=127)
    age = models.CharField('Возраст', max_length=127)
    description = models.TextField('Описание')
    adoption_date = models.DateTimeField('Дата поступления')

    def save(self):
        super().save()
        img = Image.open(self.photo.path)
        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
