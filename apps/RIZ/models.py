from django.db import models

from apps.RES import models as RES
#from apps.Type_ASKUE import models as Type_ASKUE
#from apps.Type_USPD import models as Type_USPD
#from apps.Type_PLC import models as Type_PLC
#from apps.Type_dial import models as type_dial
#from apps.Worker import models as Worker


class RIZ(models.Model):
	class Meta:
		indexes = [
			models.Index(fields = ['adress',]),
			models.Index(fields = ['num_tp',]),
		]

	RES = models.ForeignKey(
		to = RES.RES,
		on_delete = models.CASCADE,
		related_name = 'RES',
	)

	adress = models.CharField(
		max_length = 100,
	)
	
	add_adress = models.CharField(
		max_length = 200,
		blank = True,
	)
	
	choices = tuple(enumerate((
		'РП',
		'ТП',
		'КТП',
		'МТП',
		'БКТП',
	)))
	
	type_tp = models.IntegerField(
		choices = choices,
	)
	
	num_tp = models.IntegerField()
	
	col_stt = models.IntegerField(
			default = 1,
			)
	
#	Type_ASKUE = models.ForeignKey(
#		to=Type_ASKUE.Type_ASKUE,
#		on_delete=models.CASCADE,
#		related_name='Type_ASKUE',
#	)
	
#	Type_USPD = models.ForeignKey(
#		to=Type_USPD.Type_USPD,
#		on_delete=models.CASCADE,
#		related_name='Type_USPD',
#	)
	
	num_USPD = models.IntegerField(
			default = 1,
			)
	
#	Type_PLC = models.ForeignKey(
#		to=Type_PLC.Type_PLC,
#		on_delete=models.CASCADE,
#		related_name='Type_PLC',
#	)
	
	remarks_equipment = models.CharField(
		max_length = 200,
		blank = True,
	)
	
#	Type_direct_dial = models.ForeignKey(
#		to=type_dial.Type_dial,
#		on_delete=models.CASCADE,
#		related_name='Type_direct_dial',
#	)
	
	num_direct_dial = models.CharField(
		max_length = 20,
		blank = True,
	)
		
#	Type_reserv_dial = models.ForeignKey(
#		to=type_dial.Type_dial,
#		on_delete=models.CASCADE,
#		related_name='Type_reserv_dial',
#	)
	
	num_reserv_dial = models.CharField(
		max_length = 20,
		blank = True,
	)
	
#	Worker = models.ForeignKey(
#		to=Worker.Worker,
#		on_delete=models.CASCADE,
#		related_name='Worker',
#	)
	
	GPS_latit = models.CharField(
		max_length = 20,
		blank = True,
	)
	
	GPS_longit = models.CharField(
		max_length = 20,
		blank = True,
	)
	def __repr__(self):
		return '<RIZ ' \
			'#{0.id}: ' \
			'of RES {0.RES}' \
			'{0.adress}' \
			'{0.add_adress}' \
			'{type_tp_name}' \
			'{0.num_tp}' \
			'{0.col_stt}' \
			'{0.num_USPD}' \
			'{0.remarks_equipment}' \
			'{0.num_direct_dial}' \
			'{0.num_reserv_dial}' \
			'{0.GPS_latit}' \
			'{0.GPS_longit}' \
		'>'.format(
			self = self,
			type_tp_name = self.get_type_tp_display(),
		)

	__str__ = __repr__
	
#			'of Type_ASKUE {0.Type_ASKUE}' \
#			'of Type_USPD {0.Type_USPD}' \
#			'of Type_PLC {0.Type_PLC}' \
#			'of type_dial {0.Type_direct_dial}' \
#			'of type_dial {0.Type_reserv_dial}' \
#			'of Worker {0.Worker}' \
