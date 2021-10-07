from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """A blogpost that will be displayed in the website."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model for the admin"""
        return self.title
