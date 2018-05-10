from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class InstaLetterRecipients(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField()

class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'posts/',blank=True)
    bio=HTMLField()
    profile_user=models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    image=models.ImageField(upload_to = 'posts/',blank=True)
    image_name= models.CharField(max_length=60)
    image_caption=models.CharField(max_length=60)
    image_profile= models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)
