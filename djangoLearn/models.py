from django.db import models


class Work(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='images')
    tech_stack = models.TextField()
    days = models.IntegerField()
