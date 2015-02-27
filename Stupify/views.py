from django.shortcuts import render
from django.http import HttpResponseRedirect

from Stupify.forms import PhraseForm
from Stupify.models import Phrase

from settings import dictionary
import word_replace

def home(request):
    form = PhraseForm
    newPhrase = ''

    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            phrase = form.cleaned_data['phrase']
            newPhrase = word_replace.stupify(phrase)
            Phrase.objects.create(originalPhrase=phrase, newPhrase=newPhrase)
    else:
        form = PhraseForm()

    phrases = Phrase.objects.all().order_by('votes').reverse()
    form = PhraseForm()
    return render(request, 'home.html', {'form': form, 'newPhrase': newPhrase, 'phrases': phrases})

def manage(request):
    phrases = Phrase.objects.all().order_by('votes').reverse()
    return render(request, 'manage.html', {'phrases': phrases})

def vote(request, pk):
    phrase = Phrase.objects.get(pk=pk)
    phrase.votes += 1
    phrase.save()
    return HttpResponseRedirect('/')

def delete(request, pk):
    Phrase.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/manage/')
