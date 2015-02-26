from django.shortcuts import render

from Stupify.forms import PhraseForm

def home(request):
    form = PhraseForm
    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():

            return render(request, 'home.html', {'form': form})
    else:
        form = PhraseForm()

    return render(request, 'home.html', {'form': form})
