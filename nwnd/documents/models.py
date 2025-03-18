from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=2000, default='Без названия')
    file = models.FileField(upload_to='documents/')  # Путь, куда будут загружаться файлы
    category = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
