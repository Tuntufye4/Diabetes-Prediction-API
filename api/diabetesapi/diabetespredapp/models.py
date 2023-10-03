from django.db import models

class Prediction(models.Model):
    age = models.FloatField()
    sex = models.FloatField()
    bmi = models.FloatField()
    bp = models.FloatField()
    s1 = models.FloatField()
    s2 = models.FloatField()
    s3 = models.FloatField()
    s4 = models.FloatField()
    s5 = models.FloatField()
    s6 = models.FloatField()

   
    predicted_value = models.FloatField()