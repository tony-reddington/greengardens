from django.db import models


class BlogPost(models.Model):
    """ Holds Blog posts """
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    author = models.CharField(max_length=100, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-publish_date']
