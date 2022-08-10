from django.db import models

# Create your models here.
class Comment(models.Model):
	email   = models.EmailField(max_length=128)
	content = models.CharField(max_length=256)
	created = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'comments'
