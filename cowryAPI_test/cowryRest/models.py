from django.db import models
import uuid

# Create your models here.


class RandomUUID(models.Model):
    cowrytest_name = models.CharField(max_length=50, default='A name')
    timestamp = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Randomly generated")
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return self.cowrytest_name



