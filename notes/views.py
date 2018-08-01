from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewCardForm
from .models import FlashCard



@login_required(login_url='/accounts/login/')
def index(request):
    texts = FlashCard.objects.all()
    return render(request, 'index.html', {"texts":texts})

@login_required(login_url='/accounts/login/')
def new_card(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCardForm(request.POST, request.FILES)
        if form.is_valid():
            texts = form.save(commit=False)
            texts.owner = current_user
            texts.save()
            return redirect('home')
    else:
        form = NewCardForm()
    return render(request, 'new_card_form.html', {"form":form})
