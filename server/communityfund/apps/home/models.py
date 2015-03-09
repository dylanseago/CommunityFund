from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.urlresolvers import reverse


class DatedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Community(DatedModel):
    creator = models.ForeignKey(User, related_name="communities_created")
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    subscribers = models.ManyToManyField(User, related_name="subscriptions")

    def get_absolute_url(self):
        return reverse('community', args=[str(self.id)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Communities"

class Project(DatedModel):
    initiator = models.ForeignKey(User, related_name="projects_created")
    community = models.ForeignKey(Community, related_name="projects")
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    goal = models.PositiveIntegerField()
    amount_funded = models.PositiveIntegerField()
    time_to_fund = models.DateTimeField()

    @property
    def percent_funded(self):
        return round((self.amount_funded / self.goal) * 100)

    @property
    def goal_reached(self):
        return self.amount_funded >= self.goal

    @property
    def over(self):
        return datetime.now() > self.time_to_fund

    def get_absolute_url(self):
        return reverse('project', args=[str(self.id)])

    def __str__(self):
        return self.name


