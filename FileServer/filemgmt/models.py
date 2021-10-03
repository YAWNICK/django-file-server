from django.db import models
from django.conf import settings

# Create your models here.


def upload_path(instance, filename):
    return filename


class File(models.Model):

    file = models.FileField(upload_to=upload_path)

    def __str__(self) -> str:
        return self.file.name.split('/')[-1]