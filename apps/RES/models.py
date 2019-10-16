from django.db import models

#from apps.Region import models as Region
#from apps.Worker import models as worker

class RES(models.Model):
	class Meta:
		indexes = [
			models.Index(fields=['name',]),
		]

#	Region = models.ForeignKey(
#		to=Region.Region,
#		on_delete=models.CASCADE,
#	)

	name = models.CharField(
		max_length=200,
	)
	
	adress = models.CharField(
		max_length=200,
		blank=True,
	)
	
#	fix_worker = models.ForeignKey(
#		to=worker.Worker,
#		on_delete=models.CASCADE,
#		blank=True,
#	)

	remarks = models.CharField(
		max_length=200,
		blank=True,
	)

	def __repr__(self):
		return '<RES ' \
			'#{0.id}: ' \
			'{0.name}' \
			'{0.adress}' \
			'{0.remarks}' \
		'>'.format(self)

	__str__ = __repr__
	
	
	
#			'of Region {0.Region}' \
#			'of worker {0.fix_worker}' \