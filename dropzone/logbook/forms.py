from .models import Jump
from django.forms import ModelForm

class JumpForm(ModelForm):
    class Meta:
        model = Jump
        fields = '__all__'
