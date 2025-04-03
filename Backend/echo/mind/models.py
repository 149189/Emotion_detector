from django.db import models

class AudioFile(models.Model):
    file = models.FileField(upload_to='audio/')
    created_at = models.DateTimeField(auto_now_add=True)