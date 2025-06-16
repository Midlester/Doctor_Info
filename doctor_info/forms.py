from django import forms
from .models import DoctorInfo

class DoctorInfoForm(forms.ModelForm):
    class Meta:
        model = DoctorInfo
        fields = ['sl','dls_id', 'aci_id', 'name', 'divisions', 'district', 'upazilla', 'union', 'photo']
        widgets = {
            'dls_id': forms.TextInput(attrs={'class': 'form-control'}),
            'aci_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'divisions': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'upazilla': forms.TextInput(attrs={'class': 'form-control'}),
            'union': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
