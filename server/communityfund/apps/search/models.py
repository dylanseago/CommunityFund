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
			user.save()
		except:
			return None
		return user

	def update_User(uObj, uID, firstName, lastName, email, rating):
		uObj.uID=uID
		uObj.firstName=firstName
		uObj.lastName=lastName
		uObj.email=email
		uObj.rating=rating
		try:
			uObj.save()
		except:
			return None
		return uObj

	@staticmethod
	def get_User(uID=None, firstName=None, lastName=None, email=None, rating=None):
		# Change like this later
		# def get_User(*args, **kwargs):
		user=[]
		if (uID == None):
			return None
		user=User.objects.get(uID=uID)
		return user

	@staticmethod
	def set_User(uID, firstName, lastName, email, rating):
		user=User.create(uID=uID, firstName=firstName, lastName=lastName, email=email, rating=rating)
		return user


	def __unicode__(self):
		return u'%s %s %s %s %s' %(self.uID, self.firstName, self.lastName, self.email, self.rating)

	def __str__(self):
		return '%s %s %s %s %s' %(self.uID, self.firstName, self.lastName, self.email, self.rating)


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

	@staticmethod
	def get_Project(initiator=None, name=None):
		if ((initiator == None) and (name == None)):
			return None
		project=[]
		try:
			if (name):
				project=Project.objects.filter(name__contains=name)
				#project=Project.objects.get(name=name)
			else:
				project=Project.objects.get(initiator=initiator)
		except Project.DoesNotExist:
			return None
		return project

	def update_Project(pObj, pID, initiator, name, goal, description, timeToFund):
		pObj.pID=pID
		pObj.initiator=initiator
		pObj.name=name
		pObj.goal=goal
		pObj.description=description
		pObj.timeToFund=timeToFund
		try:
			pObj.save()
		except:
			return None
		return pObj
	@staticmethod
	def set_Project(pID, initiator, name, goal, description, timeToFund):
		project=Project.create(pID=pID, initiator=initiator, name=name, goal=goal, description=description, timeToFund=timeToFund)
		return project

	def __unicode__(self):
		return u'%s %s %s %s %s' %(self.pID, self.initiator, self.name, self.goal, self.timeToFund)

	def __str__(self):
		return '%s %s %s %s %s' %(self.pID, self.initiator, self.name, self.goal, self.timeToFund)


