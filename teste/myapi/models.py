from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=60)
    publisher = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name