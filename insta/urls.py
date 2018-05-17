from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static




urlpatterns=[

    url('^$',views.welcome,name='insta'),
    url(r'^home/$',views.home,name='home'),
    url(r'^profile/',views.new_profile, name='new-profile'),
    url(r'^posts/',views.new_posts, name='new-posts'),
    url(r'^myprofile/$',views.myprofile, name='myprofile'),
    url(r'^search/', views.search_profile, name='searched_profiles'),
    url(r'^register/',views.register, name='register'),
    url(r'^photos/$',views.photos,name='photos'),
    url(r'^comments/$',views.comments,name='comments'),
    url(r'^single/(?P<image_id>\d+)/$',views.single_view,name='single'),





]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
