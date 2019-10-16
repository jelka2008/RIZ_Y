from rest_framework import serializers
from . import models


class Customr(serializers.Serializer):
	class Meta:
		model = models.Customr

	id = serializers.IntegerField(
		read_only=True,
	)
	name = serializers.CharField(max_length=100)
	worker = serializers.CharField(
			max_length=100,
			required=False,
			)
	phone_worker = serializers.CharField(
			max_length=20,
			required=False,
			)
	remarks = serializers.CharField(
			max_length=200,
			required=False,
			)

	def create(self, validated_data):
		return self.Meta.model.objects.create(**validated_data)

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			setattr(
				instance,
				key,
				value,
			)
		instance.save()
		return instance