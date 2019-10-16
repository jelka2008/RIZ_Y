#from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from apps.RIZ import serializers
from apps.RIZ import models as RIZ_models


class RIZ(viewsets.ModelViewSet):
	serializer_class = serializers.RIZ
	queryset = RIZ_models.RIZ.objects.all()
	filter_backends = (
		DjangoFilterBackend,
	)
	filterset_fields = (
		'RES_id',
	)
