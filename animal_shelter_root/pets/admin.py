from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ("species", "name", "get_photo", "gender", "breed", 'age',
                    "description", "adoption_date")

    @staticmethod
    def get_photo(obj):
        return mark_safe(f'<img src={obj.photo.url} width="150">')
