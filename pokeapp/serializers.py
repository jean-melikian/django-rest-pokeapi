from rest_framework import serializers

from .models import Pokemon, PokedexEntry, Team, Match, Trainer


class PokemonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pokemon
		fields = ('id', 'pokemon_name', 'pokemon_type', 'pokemon_level')


class PokedexEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = PokedexEntry
		fields = ('pokedexentry_pokemon', 'pokedexentry_decription')


class TeamSerializer(serializers.ModelSerializer):
	team_pokemons = serializers.PrimaryKeyRelatedField(queryset=Pokemon.objects.all(), many=True)
	team_trainer = serializers.PrimaryKeyRelatedField(queryset=Trainer.objects.all())

	class Meta:
		model = Team
		fields = ('id', 'team_name', 'team_date', 'team_pokemons', 'team_trainer')


class TrainerSerializer(serializers.ModelSerializer):
	trainer_teams = serializers.StringRelatedField(many=True)

	class Meta:
		model = Trainer
		fields = ('id', 'trainer_name', 'trainer_age', 'trainer_teams')


class MatchSerializer(serializers.ModelSerializer):
	match_trainers = serializers.PrimaryKeyRelatedField(queryset=Trainer.objects.all(), many=True)

	class Meta:
		model = Match
		fields = ('id', 'match_winner', 'match_trainers')
