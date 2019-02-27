from django import forms
from .models import Contact

class ContactForm(forms.Form):
    first_name          = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    last_name           = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    email               = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone               = forms.CharField(required=True)
    date                = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'datepicker',
                                    'type':'text',
                                    'placeholder': 'Choose your event date'
                                }))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"class":"materialize-textarea", 'placeholder': 'Message'}))