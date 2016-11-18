from django.forms import ModelForm
from .models import Bild

class UploadImageForm(ModelForm):
    class Meta:
        model = Bild
        fields = ['user_title','file']



