from django.db import models


class Pokemon(models.Model):
	pokemon_name = models.CharField(max_length=255)
	pokemon_type = models.CharField(max_length=255)
	pokemon_level = models.IntegerField(default=0)
	pokemon_team = models.ForeignKey('Team', related_name='team_pokemons', on_delete=models.CASCADE)

	def __str__(self):
		return self.pokemon_name

	class Meta:
		ordering = ('pokemon_name',)


class Team(models.Model):
	team_name = models.CharField(max_length=255)
	team_date = models.DateTimeField('date published')
	team_trainer = models.ForeignKey('Trainer', related_name='trainer_teams', on_delete=models.CASCADE)

	def __str__(self):
		return self.team_name

	class Meta:
		ordering = ('team_name',)


class Trainer(models.Model):
	trainer_name = models.CharField(max_length=255)
	trainer_age = models.IntegerField(default=0)

	def __str__(self):
		return self.trainer_name

	class Meta:
		ordering = ('trainer_name',)


class Match(models.Model):
	match_winner = models.CharField(max_length=255)
	match_trainers = models.ManyToManyField('Trainer')


class PokedexEntry(models.Model):
    PokedexEntry_pokemon = models.OneToOneField(
        'Pokemon',
        primary_key=True,
    )
    PokedexEntry_decription = models.CharField(max_length=255)
