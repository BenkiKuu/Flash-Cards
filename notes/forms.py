from django import forms
from .models import FlashCard


class NewCardForm(forms.ModelForm):
    class Meta:
        model = FlashCard
        exclude = ['owner', 'pub_date']
