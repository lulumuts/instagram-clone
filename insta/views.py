from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from .forms import InstaLetterForm,NewProfileForm,NewPostsForm,CommentsForm
from .models import InstaLetterRecipients,Image,Profile,Comments
from django.contrib.auth.models import User
from .email import send_welcome_email
from django.http import HttpResponseRedirect,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import RedirectView

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
    photos = Image.objects.all()
    mass = Profile.objects.all()


    current_user = request.user
    userProfile = Profile.objects.filter(profile_user=current_user).first()
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)

            userProfile = Profile.objects.filter(profile_user=current_user).first()

            print(userProfile)
            print(image)
            comments.profile_id = userProfile
            comments.image_id = image
            comments.save_comment()
    else:
        form = CommentsForm()

    return render(request, 'gram/home.html',{"mass":mass,"photos":photos,"form":form})

def photos(request):

    current_user = request.user
    photo = Image.objects.all()
    comments = Image.objects.all().prefetch_related('image_comments')
    if current_user.is_authenticated():
        HttpResponseRedirect('index')
    return render(request, 'gram/myprofile.html', {'photo': photo})


@login_required
def myprofile(request):


    current_user = request.user
    print (current_user.id)
    userProfile = Profile.objects.filter(profile_user=current_user).first()
    print(userProfile)

    photo = Image.objects.filter(image_profile=userProfile).all()
    print(photo)



    return render(request,'gram/myprofile.html', {'userProfile':userProfile,"photo":photo})


def sample_view(request):
    current_user = request.user
    print (current_user.id)

@login_required(login_url='/accounts/login/')
def register(request):
    return render(request,'registration/registration_form.html')



@login_required(login_url='/accounts/login/')
def new_posts(request):
    current_user = request.user
    userProfile = Profile.objects.filter(profile_user=current_user).first()
    if request.method == 'POST':
        form = NewPostsForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            userProfile = Profile.objects.filter(profile_user=current_user).first()
            image.image_profile=userProfile
            image.save()
            return redirect('/home')
    else:
        form = NewPostsForm()
    return render(request, 'posts.html', {"form":form})

def search_profile(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request,'gram/search.html',{"message":message, "username":searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gram/search.html',{"message":message})

def comments(request):

    current_user = request.user
    userProfile = Profile.objects.filter(profile_user=current_user).first()

    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)

            userProfile = Profile.objects.filter(profile_user=current_user).first()
            image = Image.objects.filter(id=request.POST.get('photo_id')).first()
            print(request.POST.get('photo_id'))
            print(userProfile)
            print(image)

            comments.profile_id = userProfile
            comments.image_id = image
            comments.save()
            return redirect('/home')
    else:
        form = CommentsForm()

    return render(request, 'gram/comments.html', {"form":form,"comments":comments})

def show_comments(request,image_id):
    try:
        comment= get_image_by_id(id=image_id)
    except DoesNotExist:
        raise Http404()

    return render(request, 'gram/comments.html', {"comments":comments})

def single_view(request,image_id):

    images = Image.objects.get(id=image_id)

    try:
        images = Image.objects.get(id=image_id)
        comments = Comments.objects.filter(image_id=images).all()
        print(images)
        print(comments)

    except Image.DoesNotExist:

        raise Http404("Image does not exist")

    return render(request, 'gram/single.html', {"images":images,"comments":comments})

class ImageLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):

        print(slug)
        obj = get_object_or_404(Image, pk=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_
