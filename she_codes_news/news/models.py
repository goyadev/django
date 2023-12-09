from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # Changed this from .DateTimeField to .DateField to remove the time on articles. Needed to remember to makemigrations
    pub_date = models.DateField()
    content = models.TextField()
    image = models.URLField(null=True, blank=True)
    