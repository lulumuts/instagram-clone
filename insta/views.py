from django.shortcuts import render,render_to_response,redirect
from .forms import InstaLetterForm,NewProfileForm,NewPostsForm
from .models import InstaLetterRecipients,Image,Profile
from django.contrib.auth.models import User
from .email import send_welcome_email
from django.http import HttpResponseRedirect,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

def welcome(request):

    if request.method == 'POST':
        form = InstaLetterForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = InstaLetterRecipients(name = name, email=email)
            recipient.save()
            send_welcome_email(name,email)


            return HttpResponseRedirect('/accounts/login/')
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


def home(request):
    photo = Image.objects.all()
    mass = Profile.objects.all()
    return render(request, 'gram/home.html',{"mass":mass,"photo":photo})

def photos(request):

    current_user = request.user
    photo = Image.objects.all()
    comments = Image.objects.all().prefetch_related('image_comments')
    if current_user.is_authenticated():
        HttpResponseRedirect('index')
    return render(request, 'gram/myprofile.html', {'photo': photo})


@login_required
def myprofile(request, profile_id):
    if profile_id == "0":
        if request.user.is_authenticated:
            userProfile = Profile.objects.get(pk=profile_id)

    else:
        userProfile = Profile.objects.get(pk=profile_id)

    current_user = request.user
    photo = Image.objects.all()
    print(photo)
    comments = Image.objects.all().prefetch_related('image_comments')
    if current_user.is_authenticated():
        HttpResponseRedirect('index')

    userProfile = Profile.objects.get(pk=current_user.id)
    print(userProfile)


    return render(request,'gram/myprofile.html', {'userProfile':userProfile,"photo":photo})


@login_required(login_url='/accounts/login/')
def register(request):
    return render(request,'registration/registration_form.html')



@login_required(login_url='/accounts/login/')
def new_posts(request):
    current_user = request.user
    profile_o = Profile.objects.get(profile_user=current_user)
    if request.method == 'POST':
        form = NewPostsForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.image_profile = profile_o
            image.save()
            return redirect('/')
    else:
        form = NewPostsForm()
    return render(request, 'posts.html', {"form":form})
