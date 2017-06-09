from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from base64 import b64decode
from .auth import get_or_create_token, get_basic_auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from pokeapp.models import Trainer
from pokeapp.serializers import TrainerSerializer


@csrf_exempt
def trainer_list(request):
	if request.method == 'GET':
		trainer = Trainer.objects.all()
		serializer = TrainerSerializer(trainer, many=True)
		return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


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
