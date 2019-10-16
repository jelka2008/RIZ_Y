#from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.Commising import serializers
from apps.Commising import models as Commising_models


class Commising(viewsets.ModelViewSet):
	serializer_class = serializers.Commising
	queryset = Commising_models.Commising.objects.all()
	filter_backends = (
		DjangoFilterBackend,
	)
	filterset_fields = (
		'RIZ_id',
		'Customr_id',
		'Ajust_id',
	)