import uuid
import base64

from django.db import models
from django.core.validators import URLValidator


HOST = 'http://localhost:8000'


class Url(models.Model):
    url = models.CharField(max_length=256, validators=[URLValidator()])
    url_hash = models.CharField(db_index=True, max_length=10, unique=True, blank=True, null=True)
    url_short = models.CharField(max_length=256, validators=[URLValidator()], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_hash(self):
        hash = base64.urlsafe_b64encode(uuid.uuid1().bytes)[:6]
        # hash_exist = Url.objects.filter()
        return hash.decode('utf-8')

    def generate_short_url(self):
        return f'{HOST}/links/s/{self.url_hash}'

    def save(self, *args, **kwargs):
        self.url_hash = self.generate_hash()
        self.url_short = self.generate_short_url()
        super().save(*args, **kwargs)

