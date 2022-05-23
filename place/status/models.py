from django.db import models
from django.forms import ModelForm

class Information(models.Model):
    ssc_p=models.FloatField()
    hsc_p=models.FloatField()
    degree_p=models.FloatField()
    workex=models.IntegerField()
    etest_p=models.FloatField()
    specialisation=models.IntegerField()

class InformationForm(ModelForm):
    class Meta:
        model=Information
        fields=['ssc_p', 'hsc_p', 'degree_p', 'workex', 'etest_p', 'specialisation']
# Create your models here.
