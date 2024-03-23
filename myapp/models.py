from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class dates(models.Model):
    date = models.DateTimeField()

    def __str__(self):
        return str(self.date)
    
class KissMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kiss_messages')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Kiss from {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class NudeImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nude_images')
    image = models.ImageField(upload_to='nude_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nude Image from {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"

