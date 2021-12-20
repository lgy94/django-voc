from django import forms
from django.forms import ModelForm

from categoryapp.models import Categorylist
from vocapp.models import Voclist


class VocCreationForm(forms.ModelForm):
    class Meta:
        model = Voclist
        fields = ['voc_date','voc_method','client_number','client_number','client_name','voc_number',
                  'voc_title','voc_content','voc_comment','voc_manger','report','partner','category_num']

        widgets = {
            'voc_date': forms.TextInput(attrs={'class': 'form-control','rows':2}),
            'voc_method': forms.TextInput(attrs={'class': 'form-control','rows':2}),
            'client_number' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'client_name' : forms.TextInput(attrs={'class': 'form-control','size':55}),
            'voc_number' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'voc_title' : forms.TextInput(attrs={'class': 'form-control','size':55}),
            'voc_content' : forms.Textarea(attrs={'class': 'form-control'}),
            'voc_comment' : forms.Textarea(attrs={'class': 'form-control'}),
            'voc_manger' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'report' : forms.TextInput(attrs={'class': 'form-control'}),
            'partner' : forms.TextInput(attrs={'class': 'form-control','lows':2}),
            'category_num': forms.TextInput(attrs={'class': 'form-control', 'lows': 2}),
        }

        def save(self, commit=True, id=0):
            apply = super(Categorylist, self).save(commit=False)
            if commit:
                apply.category_num = Categorylist.objects.get(pk=id)

                apply.save()
            return apply
