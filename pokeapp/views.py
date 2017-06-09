from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from base64 import b64decode
from .auth import get_or_create_token, get_basic_auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from pokeapp.models import Trainer, Pokemon, Team, Match
from pokeapp.serializers import TrainerSerializer, PokemonSerializer, TeamSerializer, MatchSerializer


@csrf_exempt
def trainer_list(request):
	if request.method == 'GET':
		trainer = Trainer.objects.all()
		serializer = TrainerSerializer(trainer, many=True)
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		serializer = TrainerSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def trainer_details(request, pk):
	try:
		trainer = Trainer.objects.get(pk=pk)
	except Trainer.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = TrainerSerializer(trainer)
		return JsonResponse(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		serializer = TrainerSerializer(trainer, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_200_OK)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		trainer.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def pokemon_list(request):
	if request.method == 'GET':
		pokemon = Pokemon.objects.all()
		serializer = PokemonSerializer(pokemon, many=True)
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		serializer = PokemonSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def pokemon_details(request, pk):
	try:
		pokemon = Pokemon.objects.get(pk=pk)
	except Pokemon.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PokemonSerializer(pokemon)
		return JsonResponse(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		serializer = PokemonSerializer(pokemon, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_200_OK)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		pokemon.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def team_list(request):
	if request.method == 'GET':
		team = Team.objects.all()
		serializer = TeamSerializer(team, many=True)
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		serializer = TeamSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def team_details(request, pk):
	try:
		team = Team.objects.get(pk=pk)
	except Team.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = TeamSerializer(team)
		return JsonResponse(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		serializer = TeamSerializer(team, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_200_OK)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		team.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def match_list(request):
	if request.method == 'GET':
		match = Match.objects.all()
		serializer = MatchSerializer(match, many=True)
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)
		serializer = MatchSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def match_details(request, pk):
	try:
		match = Match.objects.get(pk=pk)
	except Match.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = MatchSerializer(match)
		return JsonResponse(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		try:
			data = JSONParser().parse(request)
		except ParseError:
			return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
		serializer = MatchSerializer(match, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_200_OK)
		else:
			return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		match.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)
	else:
		return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def login(request):
	basic = get_basic_auth(request)
	if basic is not None:
		log = b64decode(bytes(basic, 'ascii')).decode('ascii').split(';')
		user = authenticate(username=log[0], password=log[1])
		if user is not None:
			token = get_or_create_token(user)
			return JsonResponse(data={'token': token.hash})
	return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
