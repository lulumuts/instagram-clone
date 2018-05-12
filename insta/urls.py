from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns=[

    url('^$',views.welcome,name='insta'),
    url(r'^profile/$',views.new_profile, name='new-profile'),
    url(r'^myprofile/$',views.myprofile,name='myprofile')


]
