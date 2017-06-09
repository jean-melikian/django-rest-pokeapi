from django.conf.urls import url

from . import views

app_name = 'pokeapp'

urlpatterns = [
	url(r'^login$', views.login, name='login'),
	url(r'^trainers/$', views.trainer_list, name='trainer-list')
]
