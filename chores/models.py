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
    date = models.DateField(unique=True)
    busy = models.BooleanField(default=False)
    chores = models.ManyToManyField(Chore,through="ChoreAssignment", related_name="days")

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return str(self.date)

# through model
class ChoreAssignment(models.Model):
    chore = models.ForeignKey(Chore, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    class Meta:
        # unique_together = ("chore", "day")  # same chore cannot be assigned to the same day twice, but chore can appear on other days
        constraints = [
            models.UniqueConstraint(
                fields=["chore", "day"],
                name="unique_chore_in_day"
            )
        ]
