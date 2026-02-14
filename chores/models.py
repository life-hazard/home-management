from django.db import models

# Create your models here: database layout and metadata


class Manager(models.Model):
    name = models.CharField(max_length=50)


class Chore(models.Model):
    chore_name = models.CharField(max_length=200)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ["chore_name"]

    def __str__(self):
        return self.chore_name


class Day(models.Model):
    date = models.DateField()
    chores = models.ManyToManyField(Chore, blank=True, default=None)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return str(self.date)

