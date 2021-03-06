from django.db import models
from django.conf import settings
from .validators import validate_content




class Tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[validate_content])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str("Content of the tweet: " + self.content)



# Create your models here.
