#from django.shortcuts import render
from rest_framework import viewsets
from apps.RES import serializers
from apps.RES import models as RES_models


class RES(viewsets.ModelViewSet):
	serializer_class = serializers.RES
	queryset = RES_models.RES.objects.all()
