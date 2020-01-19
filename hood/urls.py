from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    # url(r'^accounts/login', views.login, name= 'login'),
    # url(r'^accounts/signup', views.signup, name= 'signup'),
    url(r'^profile/(?P<user_id>\d+)', views.profile, name = 'profile'),
    url(r'^edit/profile', views.update_profile, name = 'update_profile'),
    url(r'^create/post', views.create_post, name = 'create_posts'),
    url(r'^change', views.change, name = 'change_neighbourhood'),
    url(r'^search', views.search, name = 'search'),
]
