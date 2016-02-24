from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/(?P<user_id>[\w\d_\s]+)$', views.ProfileView.as_view(), name='input'),
    url(r'^create/$', views.CreateProfileView.as_view(), name='input'),
]