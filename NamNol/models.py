from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    