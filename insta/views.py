from django.shortcuts import render
from .forms import InstaLetterForm
from .models import InstaLetterRecipients
from .email import send_welcome_email
from django.http import HttpResponseRedirect
#................
# Create your views here.
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
