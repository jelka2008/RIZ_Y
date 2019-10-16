from rest_framework import serializers
from . import models


class Commising(serializers.Serializer):
	class Meta:
	
		model = models.Commising

	id = serializers.IntegerField(
		read_only = True,
	)
	num_akt = serializers.CharField(
		max_length = 6,
		required = False,
	)
	akt_date = serializers.DateField()
	remarks = serializers.CharField(
		max_length = 200,
		required = False,
	)

	def create(self, validated_data):

		get_object = self.context['request'].GET
		get_kwargs = {
			key: get_object[key]
			for key in self.context['request'].GET
		}

		return self.Meta.model.objects.create(
			**validated_data,
			**get_kwargs,
		)
		
	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			setattr(
				instance,
				key,
				value,
			)
		instance.save()
		return instance