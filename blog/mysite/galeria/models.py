from django.db import models
from django.utils import timezone


class Galeria(models.Model):

    foto = models.ImageField()
    create_on = models.DateTimeField(auto_now_add=True, editable=False)
    publicate_on = models.DateTimeField()

    def publicate(self):
        now = timezone.now()
        return now > self.publicate_on

    def __str__(self):
        return f"{self.foto} (id:{self.id})"