from django.forms import ModelForm
from django.forms.widgets import EmailInput, TextInput, Textarea
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "message",
        ]
        widgets = {
            "first_name": TextInput(attrs={"class": "contact__form_field"}),
            "last_name": TextInput(attrs={"class": "contact__form_field"}),
            "email": EmailInput(attrs={"class": "contact__form_field"}),
            "phone_number": TextInput(attrs={"class": "contact__form_field"}),
            "message": Textarea(attrs={"class": "contact__form_field"}),
        }
