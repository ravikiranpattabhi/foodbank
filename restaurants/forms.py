from django import forms
from .models import Restaurant, Comment
from .snippets import choices
from django.contrib.auth.models import User  # Import the default User model

class RestaurantCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter title'}))
    categories = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categories separated by comma. Example: chinese,thai'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    location = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Location'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}))
    persons = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Restaurant
        fields = ['title', 'image', 'categories', 'location', 'details', 'contact','persons']
