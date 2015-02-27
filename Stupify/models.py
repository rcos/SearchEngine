from django.db import models


class Phrase(models.Model):

    """docstring for Phrase"""
    originalPhrase = models.CharField(max_length=256, blank=False)
    newPhrase = models.CharField(max_length=256, blank=False)
    votes = models.IntegerField(default=0)
