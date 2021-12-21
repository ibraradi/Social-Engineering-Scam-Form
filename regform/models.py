from django.db import models

class student(models.Model):
	stid = models.TextField()
	password = models.TextField()