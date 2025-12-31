import uuid
from django.db import models
from django.conf import settings

class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                                related_name='profile',)
    bio= models.TextField(blank=True)




class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description= models.TextField(blank=True,null=True)
    pdf_file = models.FileField(upload_to='BOOKS/', null=True, blank=False)
    num_pages = models.PositiveIntegerField(null=True)
    year_written = models.PositiveIntegerField(null=True)
    upload_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title


