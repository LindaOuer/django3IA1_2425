from django.db import models
from categoryApp.models import Category

# Create your models here.
class Conference(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    price=models.FloatField()
    capacity = models.IntegerField()
    program = models.FileField(upload_to='files/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="conferences")