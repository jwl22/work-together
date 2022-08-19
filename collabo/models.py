from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    work_list = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Collaborator(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField()
