from django.db import models

class WeatherData(models.Model):
    year=models.IntegerField()
    jan=models.FloatField()
    feb=models.FloatField()
    mar=models.FloatField()
    apr=models.FloatField()
    may=models.FloatField()
    jun=models.FloatField()
    jul=models.FloatField()
    aug=models.FloatField()
    sep=models.FloatField()
    oct=models.FloatField()
    nov=models.FloatField()
    dec=models.FloatField()
    winter=models.FloatField()
    spring=models.FloatField()
    summer=models.FloatField()
    autumn=models.FloatField()
    annual=models.FloatField()

    def __str__(self) :
        return str(self.year)
