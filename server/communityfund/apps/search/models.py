from django.db import models

class User(models.Model):
	uID = models.IntegerField(primary_key=True)
	firstName = models.TextField()
	lastName = models.TextField()
	email = models.EmailField()
	rating = models.FloatField()

	@classmethod
	def create(cls, uID, firstName, lastName, email, rating):
		try:
			user=cls(uID=uID, firstName=firstName, lastName=lastName, email=email, rating=rating)
		except:
			return None
		return user
	def __unicode__(self):
		return u'%s %s %s' %(self.uID, self.firstName, self.lastName)
	def __str__(self):
		return '%s %s %s' %(self.uID, self.firstName, self.lastName)

class Project(models.Model):
	pID = models.IntegerField(primary_key=True)
	initiator = models.ForeignKey(User)
	name = models.TextField()
	goal = models.IntegerField()
	description = models.TextField()
	timeToFund = models.DateField()

	@classmethod
	def create(cls, pID, initiator, name, goal, description, timeToFund):
		try:
			project = cls(pID=pID, initiator=initiator, name=name, goal=goal, description=description, timeToFund=timeToFund)
			project.save()
		except:
			return None
		return project
	def __unicode__(self):
		return u'%s %s %s' %(self.pID, self.initiator, self.name)
	def __str__(self):
		return '%s %s %s' %(self.pID, self.initiator, self.name)


