from django.db import models

class Ajust(models.Model):
	class Meta:
		indexes = [
			models.Index(fields=['name',]),
			models.Index(fields=['worker',]),
		]

	name = models.CharField(
		max_length=100,
	)
	
	worker = models.CharField(
		max_length=100,
		blank=True,
	)
	
	phone_worker = models.CharField(
		max_length=20,
		blank=True,
	)

	remarks = models.CharField(
		max_length=200,
		blank=True,
	)

	def __repr__(self):
		return '<Ajust ' \
			'#{0.id}: ' \
			'{0.name}' \
			'{0.worker}' \
			'{0.phone_worker}' \
			'{0.remarks}' \
		'>'.format(self)

	__str__ = __repr__