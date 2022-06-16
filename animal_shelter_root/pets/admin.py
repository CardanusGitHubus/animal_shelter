from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ("species", "name", "gender", "breed", 'age',
                    "description", "adoption_date", "get_photo")

    @staticmethod
    def get_photo(obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="50">')
