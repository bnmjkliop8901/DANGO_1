from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100 , required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=55)
    message = forms.CharField(max_length=55 , required=True)
