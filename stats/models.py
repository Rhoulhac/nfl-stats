from django.db import models

class Location(models.Model):

    STATES = {
        ('MN', 'Minnesota'),
        ('FL', 'Florida'),
        ('TX', 'Texas'),
        ('GA', 'Georgia'),
        ('MO', 'Missouri')
    }

    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2, choices=STATES)

    def __str__(self):
        return self.city

    def __repr__(self):
        return '{} {}'.format(self.city, self.state)


class Team(models.Model):

    name = models.CharField(max_length=200)
    mascot = models.CharField(max_length=200)
    location = models.ForeignKey(Location)

    def __repr__(self):
        return self.name


class Quaterback(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)
