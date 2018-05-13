from django import forms
from .models import Profile,Image


class InstaLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_follows']

class NewPostsForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date','image_profile','likes']
