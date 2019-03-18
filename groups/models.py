from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.name)


class User(models.Model):
    username = models.CharField(max_length=250)
    created = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.username, self.group.name)
