from django import forms
from .models import Pet


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            "species",
            "name",
            "gender",
            "breed",
            "age",
            "description",
            "adoption_date",
            "photo",
        ]
