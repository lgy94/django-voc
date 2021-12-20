from django.forms import ModelForm

from categoryapp.models import Categorylist


class CategoryCreationForm(ModelForm):
    class Meta:
        model = Categorylist
        fields=['service_name']