from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('作者',max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = '作者'

class Book(models.Model):
    title = models.CharField('书名',max_length=50)
    authors = models.ManyToManyField(Author,verbose_name='作者')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = '图书'