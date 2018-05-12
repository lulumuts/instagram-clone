from django.test import TestCase
from .models import Image, Profile, Comments,followers,likes
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.




class ProfileTestClass(TestCase):
    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016')
        self.user.save()

        self.profile=Profile(profile_photo=
    '/posts',bio='love chocolate',profile_user=self.user,profile_follows="True")


    def test_instance(self):
        self.assertTrue(isinstance(self.bio,Profile))

    def test_save_method(self):
        self.bio.save_bio()
        profile =Profile.objects.all()
        self.assertTrue(len(category) > 0)


    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(locations) == 0)

    def tearDown(self):
        Image.objects.all().delete()

class ImageTestClass(TestCase):



    def setUp(self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016')
        self.user.save()
        self.likes=likes(profile=self.user)
        self.likes.save()
        self.profile=Profile(profile_photo=
    '/posts',bio='love chocolate',profile_user=self.user,)
        self.profile.save()
        self.image = Image(image='posts/',image_name='testing',image_caption='testing2',pub_date='02/04/2018',image_profile=self.profile,likes=self.profile)

        self.image.save_image()
        self.image.likes.add(self.user)


    def test_instance(self):
        self.assertTrue(issintance(self.image,Image))

    def test_save_image(self):
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self):
        self.image.save_image()
        kwargs={'image':'/posts','image_name':'myname','image_caption':'myself'}
        Image.update_caption(self.image.id,**kwargs)
        self.assertEqual("myname",self.image.image_name)


    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_get_image_id(self):
        image_id = id
        self.image.objects.get(pk=id)
        self.assertTrue(pk=id)

    def tearDown(self):
        Image.objects.all().delete()

class CommentsTestClass(TestCase):


    def setup (self):
        self.image = Image(image='posts/',image_name='testing',image_caption='testing2',pub_date='02/04/2018',image_profile=self.profile,likes=self.profile)

        self.profile=Profile(profile_photo=
    '/posts',bio='love chocolate',profile_user=self.user,profile_follows="True")

        self.comments=Comments(comment='blah blah',image_id=self.image, profile_id=self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_save_method(self):
        self.comment.save_comment()
        comments =Comments.objects.all()
        self.assertTrue(len(Comments) > 0)

    def test_delete_comments(self):
        self.comments.save_comments()
        self.comments.delete_comments()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 0)

    def tearDown(self):
        Comments.objects.all().delete()

class followersTestCase(TestCase):

    following= models.ForeignKey(User,related_name='who_follows')
    follower=models.ForeignKey(User,related_name='who_is_followed')

    def setup (self):
        self.user= User(username='lulu',email='lulumutuli24@gmail.com', password='snoopdogg2016')
        self.user.save()
        self.followers= followers(following=self.User, follower=self.User)

    def test_instance(self):
        self.assertTrue(issintance(self.followers,followers))

    def tearDown(self):
        followers.objects.all().delete()
