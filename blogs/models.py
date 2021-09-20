from django.db import models

class BlogPost(models.Model):
    """A blogpost that will be displayed in the website."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        """Return a string representation of the model for the admin"""
        return self.title
