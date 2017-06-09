from django.conf.urls import url

from . import views

app_name = 'pokeapp'

urlpatterns = [
	url(r'^trainers/$', views.trainer_list, name='trainer-list'),
	url(r'^trainers/(?P<pk>[0-9]+)/$', views.trainer_details, name='trainer-details'),
]
