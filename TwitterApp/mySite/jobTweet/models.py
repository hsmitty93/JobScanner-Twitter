# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Tweet(models.Model):
	name = models.CharField(max_length=30)
	created = models.DateField()
	location = models.CharField(max_length=30)
	where = models.URLField()
	text = models.CharField(max_length=280)

	class Meta:
		ordering = ["-created"]

	def __unicode__(self):
		return self.text

