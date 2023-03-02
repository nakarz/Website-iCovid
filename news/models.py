from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    postDate = models.DateField()
    articleImage = models.TextField()
    body = models.TextField()
    summary = models.TextField()