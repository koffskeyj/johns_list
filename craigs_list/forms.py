from django import forms
from craigs_list.models import Profile

class CityForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["city"]
