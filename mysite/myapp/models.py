from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=45)
    number = models.IntegerField()

class MyModel2(models.Model):
    mymodel = models.ForeignKey(MyModel, on_delete=models.CASCADE)