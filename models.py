from django.db import models

# Create your models here.
class Company(models.Model):
    KIND = (
            (0, "Corporate"),
            (1, "Start Up"),
            )
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    kind = models.IntegerField(default=0, choices=KIND)


class Job(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
