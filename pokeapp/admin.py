from django.contrib import admin

# Register your models here.
from pokeapp.models import Trainer, PokedexEntry, Pokemon, Team, Match

admin.site.register({
	Trainer,
	PokedexEntry,
	Pokemon,
	Team,
	Match
})
