from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns=[

    url('^$',views.welcome,name='insta'),
    url(r'^home/$',views.home,name='home'),
    url(r'^profile/',views.new_profile, name='new-profile'),
    url(r'^posts/',views.new_posts, name='new-posts'),
    url(r'^myprofile/(?P<profile_id>\d+)/$',views.myprofile, name='myprofile'),
    url(r'^register/',views.register, name='register'),
    url(r'^myprofile/$',views.photos,name='photos'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
