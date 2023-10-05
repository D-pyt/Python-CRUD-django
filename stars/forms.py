from django import forms
from .models import Star


class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = ['star_name', 'star_constellation', 'star_type', 'star_distance', 'star_mass', 'star_temperature', 'star_period', 'star_turn_speed']
        labels = {
            'star_name': 'Star name',
            'star_constellation': 'Constellation',
            'star_type': 'Star type',
            'star_distance': 'Distance',
            'star_mass': 'Mass',
            'star_temperature': 'Temperature',
            'star_period': 'Period',
            'star_turn_speed': 'Turn speed'
        }
        widgets = {
            'star_name': forms.TextInput(attrs={'class': 'form-control'}),
            'star_constellation': forms.TextInput(attrs={'class': 'form-control'}),
            'star_type': forms.TextInput(attrs={'class': 'form-control'}),
            'star_distance': forms.TextInput(attrs={'class': 'form-control'}),
            'star_mass': forms.TextInput(attrs={'class': 'form-control'}),
            'star_temperature': forms.TextInput(attrs={'class': 'form-control'}),
            'star_period': forms.TextInput(attrs={'class': 'form-control'}),
            'star_turn_speed': forms.TextInput(attrs={'class': 'form-control'})
        }
