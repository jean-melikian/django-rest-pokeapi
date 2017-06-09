from rest_framework import serializers

from .models import Pokemon, PokedexEntry, Team, Match, Trainer


class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ('id', 'pokemon_name', 'pokemon_type', 'pokemon_level', 'team_name')


class PokedexEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexEntry
        fields = ('pokemon_name', 'description')


class TeamSerializer(serializers.ModelSerializer):
    team_pokemons = serializers.StringRelatedField(many=True)

    class Meta:
        model = Team
        fields = ('id', 'team_name', 'team_date', 'team_pokemons')


class TrainerSerializer(serializers.ModelSerializer):
    trainer_teams = serializers.StringRelatedField(many=True)

    class Meta:
        model = Trainer
        fields = ('id', 'trainer_name', 'trainer_age', 'trainer_teams')


class MatchSerializer(serializers.ModelSerializer):
    trainers = TrainerSerializer(read_only=True, many=True)

    class Meta:
        model = Match
        fields = ('id', 'match_winner')
