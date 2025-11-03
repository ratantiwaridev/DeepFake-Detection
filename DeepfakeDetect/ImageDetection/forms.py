from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    """
    A form for uploading image files based on the Image model.
    """
    class Meta:
        model = Image
        fields = ['image_file']