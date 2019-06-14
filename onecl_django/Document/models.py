from django.db import models
from User.models import CustomUser
from Club.models import Club

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=3000)
    date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20)
    owner = models.ForeignKey(CustomUser, related_name='documents', on_delete=models.CASCADE)
    club = models.ForeignKey(Club, related_name='documents', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date', 'title', 'content', 'owner__name']