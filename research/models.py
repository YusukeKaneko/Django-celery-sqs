import uuid

from django.contrib.auth.models import User
from django.db import models


class Translations(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    translated_text = models.TextField(blank=True)
    finished_at = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)
