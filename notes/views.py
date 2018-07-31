from django.shortcuts import render

from .forms import NewCardForm


def index(request):
    return render(request, 'index.html')


def new_card(request):
    form = NewCardForm()
    return render(request, 'new_card_form.html', {"form":form})
