#from django.shortcuts import render
from rest_framework import viewsets
from apps.Customr import serializers
from apps.Customr import models as Customr_models


class Customr(viewsets.ModelViewSet):
	serializer_class = serializers.Customr
	queryset = Customr_models.Customr.objects.all()