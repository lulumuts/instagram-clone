from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
import datetime as dt


# Create your models here.


class followers(models.Model):

    following= models.ForeignKey(User,related_name='who_follows')
    follower=models.ForeignKey(User,related_name='who_is_followed')


class Profile(models.Model):

    profile_photo = models.ImageField(upload_to = 'posts/',blank=True)
    bio = models.CharField(max_length=60)
    profile_user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_follows = models.ManyToManyField("self",related_name='follows',symmetrical = False)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @staticmethod
    def update_profile(self):
        Image.objects.filter(pk=id).update(profile_photo=profile_photo,bio=bio,profile_user=profile_user,profile_follows=profile_follows)

    # def find_profile(self,name):

    @classmethod
    def search_profile(cls,search_term):
        profile = cls.objects.filter(profile_user__username__icontains=search_term)
        print(profile)
        return profile


    def __str__(self):
        return self.bio


class Image(models.Model):

    image=models.ImageField(upload_to = 'posts/',blank=True)
    image_name= models.CharField(max_length=60)
    image_caption=models.CharField(max_length=60)
    image_profile= models.ForeignKey(Profile,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="likes",default=None)


    @property
    def total_likes(self):
        '''Likes for images'''
        return self.likes.count()



    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @staticmethod
    def update_caption(id,image,image_name,image_caption):

        Image.objects.filter(pk=id).update(image=image,image_name=image_name,image_caption=image_caption)

    def get_image_by_id(self,id):
        return self.objects.get(pk=id)

    def get_like_url(self):
        return reverse("image:like-toggle")



    
    def __str__(self):
        return self.image_name



class Comments(models.Model):

    comment=models.CharField(max_length=60)
    image_id= models.ForeignKey(Image,null=True)
    profile_id=models.ForeignKey(Profile)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def __str__(self):
        return self.comment


class InstaLetterRecipients(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField()
