from cProfile import label
from django import forms
from .models import ContactUS
class MyForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = ["name", "mail","subject","contactNo","message",]
        label = ["name", "mail","subject","contactNo","message",]