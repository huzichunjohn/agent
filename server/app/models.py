from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    repo = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

class Version(models.Model):
    name = models.CharField(max_length=100)
    application = models.ForeignKey(Application)
