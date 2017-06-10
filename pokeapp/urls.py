from django.conf.urls import url

from . import views

app_name = 'pokeapp'

urlpatterns = [
	url(r'^login$', views.login, name='login'),

	url(r'^trainers/$', views.trainer_list, name='trainer-list'),
	url(r'^trainers/(?P<pk>[0-9]+)/$', views.trainer_details, name='trainer-details'),

	url(r'^pokemons/$', views.pokemon_list, name='pokemon-list'),
	url(r'^pokemons/(?P<pk>[0-9]+)/$', views.pokemon_details, name='pokemon-details'),

	url(r'^teams/$', views.team_list, name='team-list'),
	url(r'^teams/(?P<pk>[0-9]+)/$', views.team_details, name='team-details'),

	url(r'^matchs/$', views.match_list, name='match-list'),
	url(r'^matchs/(?P<pk>[0-9]+)/$', views.match_details, name='match-details'),

	url(r'^pokedexentry/$', views.pokedexentry_list, name='pokedexentry-list'),
	url(r'^pokedexentry/(?P<pk>[A-Za-z]+)/$', views.pokedexentry_details, name='pokedexentry-details'),

]
