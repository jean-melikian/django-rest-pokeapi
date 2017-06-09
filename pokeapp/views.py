from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser

from pokeapp.models import Trainer
from pokeapp.serializers import TrainerSerializer


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
