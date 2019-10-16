from rest_framework import serializers
from . import models


class RIZ(serializers.Serializer):
	class Meta:
	
		model = models.RIZ
		choices = model.choices

	id = serializers.IntegerField(
		read_only=True,
	)
	adress = serializers.CharField(max_length = 100)
	add_adress = serializers.CharField(
			max_length = 200,
			required = False,
			)
	type_tp = serializers.ChoiceField(
		choices = Meta.choices,
		style = {'base_template': 'radio.html'},
		allow_blank = False,
		allow_null = False,
	)
	num_tp = serializers.IntegerField()
	col_stt = serializers.IntegerField(
			required = False
			)
	num_USPD = serializers.IntegerField(
			required = False
			)
	remarks_equipment = serializers.CharField(
			max_length = 200,
			required = False,
			)
	num_direct_dial = serializers.CharField(
			max_length = 20,
			required = False,
			)
	num_reserv_dial = serializers.CharField(
			max_length = 20,
			required = False,
			)
	GPS_latit = serializers.CharField(
			max_length = 20,
			required = False,
			)
	GPS_longit = serializers.CharField(
			max_length = 20,
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