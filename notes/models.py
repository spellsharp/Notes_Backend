from django.db import models
import uuid
import datetime
# Create your models here.
class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ForeignKey('Tags', related_name='notes', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or ''


class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    color = models.CharField(max_length=7, null=True)
    def __str__(self):
        return self.name or ''

