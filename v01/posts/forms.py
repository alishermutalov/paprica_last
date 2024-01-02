from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number']
        error_messages = {
            'name': {
                'required': "Пожалуйста, введите ваше имя."
            },
            'phone_number': {
                'required': "Пожалуйста, введите ваш номер телефона."
            },
        }