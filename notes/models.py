from django.db import models
import uuid
# Create your models here.
class Notes(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
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