from django.db import models

class BlogPost(models.Model):
    """ Holds Blog posts """
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date']
