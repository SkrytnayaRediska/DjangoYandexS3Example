from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='courses/')

    def __str__(self):
        return self.name

