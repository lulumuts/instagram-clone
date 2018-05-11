from django.shortcuts import render
from .forms import InstaLetterForm,NewProfileForm
from .models import InstaLetterRecipients
from .email import send_welcome_email
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def welcome(request):

    if request.method == 'POST':
        form = InstaLetterForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstaLetterRecipients(name = name, email=email)
            recipient.save()
            send_welcome_email(name,email)


            HttpResponseRedirect('welcome')
    else:
        form = InstaLetterForm()
    return render(request, 'gram/newsfeed.html',{"letterForm" : form})


@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.image_profile = current_user
            profile.save()

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form":form})
