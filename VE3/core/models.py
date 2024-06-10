from django.db import models

class Titanic(models.Model):
    PassengerId = models.IntegerField(primary_key=True)
    Survived = models.BooleanField()
    Pclass = models.IntegerField()
    Name = models.CharField(max_length=100)
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    Sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    Age = models.FloatField(null=True, blank=True)
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Ticket = models.CharField(max_length=100)
    Fare = models.FloatField(null=True, blank=True)
    Cabin = models.CharField(max_length=100, null=True, blank=True)
    EMBARKED_CHOICES = [
        ('C', 'Cherbourg'),
        ('Q', 'Queenstown'),
        ('S', 'Southampton'),
    ]
    Embarked = models.CharField(max_length=1, choices=EMBARKED_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.Name} ({'Survived' if self.Survived else 'Did not survive'})"
