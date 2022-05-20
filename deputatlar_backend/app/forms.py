from django import forms
from .models import Taklif


class AddTaklifForm(forms.ModelForm):

    f_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class" : "form-control",
        "id" : "floatingInput1",
        "placeholder" : "Example Name"
    }))
    phone = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        "class": "form-control",
        "id": "floatingInput2",
        "placeholder": "Example Name"
    }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "floatingInput3",
        "placeholder": "Example Name"
    }))
    comment = forms.CharField(max_length=100, widget=forms.Textarea(attrs={
        "class": "form-control",
        "id": "floatingTextarea2",
        "placeholder": "Example Name"
    }))

    class Meta:
        model = Taklif
        fields = ("f_name", "phone", "subject", "comment")
