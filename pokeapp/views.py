from django.http import HttpResponse, JsonResponse
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