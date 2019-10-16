from django.db import models

from apps.RIZ import models as RIZ
#from apps.Worker import models as Worker
from apps.Ajust import models as Ajust
from apps.Customr import models as Customr

class Commising(models.Model):
	class Meta:
		indexes = [
			models.Index(fields = ['num_akt',]),
		]

	RIZ = models.ForeignKey(
		to=RIZ.RIZ,
		on_delete=models.CASCADE,
	)

	num_akt = models.CharField(
		max_length=6,
		blank=True,)
	
	akt_date = models.DateField(
#		auto_now=False, 
#		auto_now_add=False
	)
	
#	Worker = models.ForeignKey(
#		to=Worker.Worker,
#		on_delete=models.CASCADE,
#	)
	
	Ajust = models.ForeignKey(
		to=Ajust.Ajust,
		on_delete=models.CASCADE,
	)
	
	Customr = models.ForeignKey(
		to=Customr.Customr,
		on_delete=models.CASCADE,
	)
	
	remarks = models.CharField(
		max_length=200,
		blank=True,
	)
	
	
	def __repr__(self):
		return '<Commising ' \
			'#{0.id}: ' \
			'of RIZ {0.RIZ}' \
			'{0.num_akt}' \
			'{0.akt_date}' \
			'of Ajust {0.Ajust}' \
			'of Customr {0.Customr}' \
			'{0.remarks}' \
		'>'.format(self)

	__str__ = __repr__
	
#			'of Worker {0.Worker}' \