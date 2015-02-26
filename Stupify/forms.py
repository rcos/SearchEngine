from django import forms

from Stupify.models import Phrase

class PhraseForm(forms.Form):
    """docstring for PhraseForm"""
    phrase = forms.CharField(label='Enter Your Phrase')
        