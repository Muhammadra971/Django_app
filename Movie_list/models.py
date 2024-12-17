from django.db import models

# Create your models here.

class CensorInfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    cirtified_by=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.cirtified_by

class Directer(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Moviedata(models.Model):
    title=models.CharField(max_length=250)
    year=models.IntegerField(max_length=200)
    discription=models.TextField(null=True)
    images=models.ImageField(upload_to='media/',null=True)
    censor_details=models.OneToOneField(CensorInfo,
                                        on_delete=models.SET_NULL,
                                        related_name="movie",
                                        null=True)
    directer_by=models.ForeignKey(Directer,null=True,
                                  on_delete=models.CASCADE,
                                  related_name='directed_movie')
    acters=models.ManyToManyField(Actor,related_name='acted_movies')
