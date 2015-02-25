from django.shortcuts import render
from django import forms

class Form(forms.Form):

    text = forms.CharField(label='')

def home(request):

    if request.method == 'POST':
        if form.is_valid():
            return
    else:
        form = Form()

    return render(request, 'home.html', {'form': form})
