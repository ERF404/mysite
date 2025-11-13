from django.db import models

# Create your models here.

class Post(models.Model):
    
    # author
    # img
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_view = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title