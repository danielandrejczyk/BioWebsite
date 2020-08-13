from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    publish_date = models.DateTimeField('date published')
    #TO-DO: Add tags