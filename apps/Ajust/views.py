#from django.shortcuts import render
from rest_framework import viewsets
from apps.Ajust import serializers
from apps.Ajust import models as Ajust_models


class Ajust(viewsets.ModelViewSet):
	serializer_class = serializers.Ajust
	queryset = Ajust_models.Ajust.objects.all()