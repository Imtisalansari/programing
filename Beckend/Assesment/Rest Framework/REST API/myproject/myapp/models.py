from django.db import models

class Comment(models.Model):
    postId = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} ({self.email})"
