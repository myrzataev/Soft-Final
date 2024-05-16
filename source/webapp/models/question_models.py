from django.db import models
from .test_models import TestSet


class Question(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def clean(self):
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


