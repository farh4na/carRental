from django import forms
from .models import Profile

class SearchForm(forms.Form):
    car_type = forms.ChoiceField(choices=[
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
    ])
    transmission = forms.ChoiceField(choices=[
        ('auto', 'Automatic'),
        ('manual', 'Manual'),
    ])
    brand = forms.ChoiceField(choices=[
        ('proton', 'Proton'),
        ('perodua', 'Perodua'),
        ('honda', 'Honda'),
        ('toyota', 'Toyota'),
    ])
    seats = forms.ChoiceField(choices=[
        (5, '5 seats'),
        (7, '7 seats'),
    ])
    price_range = forms.ChoiceField(choices=[
        ('0-200', '0-200'),
        ('200', '200 and above'),
    ])

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']  