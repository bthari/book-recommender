from django.db import models

class Book(models.Model):
	book_id = models.IntegerField()
	title = models.CharField(max_length=128)
	description = models.TextField(default='-')