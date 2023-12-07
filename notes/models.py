from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField('Tags', related_name='notes')
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=7)
    def __str__(self):
        return self.name