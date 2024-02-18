from django.db import models
import uuid
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
now = timezone.now()
naive_datetime = datetime.datetime.now()
aware_datetime = timezone.make_aware(naive_datetime, timezone=timezone.utc)

class Notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(null=True)
    is_public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.author_id:
            self.author = kwargs.pop('request', None).user
        self.updated_at = aware_datetime
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or ''