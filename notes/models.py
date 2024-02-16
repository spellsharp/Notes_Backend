from django.db import models
import uuid
import datetime
from django.utils import timezone

now = timezone.now()
naive_datetime = datetime.datetime.now()
aware_datetime = timezone.make_aware(naive_datetime, timezone=timezone.utc)

class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.updated_at = aware_datetime
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or ''