from django.db import models
import uuid
import datetime
# Create your models here.
class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or ''