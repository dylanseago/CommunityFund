from django.db import models

class Project(models.Model):
	pID = models.IntegerField()
	initiator = models.IntegerField()
	name = models.TextField()
	goal = models.IntegerField()
	description = models.TextField()
	timeToFund = models.DateField()

