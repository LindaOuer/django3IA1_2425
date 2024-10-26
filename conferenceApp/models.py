from django.db import models
from categoryApp.models import Category
from django.core.validators import MaxValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError
from datetime import date
def validate_date(value):
    if value < date.today():
        raise ValidationError("The start date must be in the future")
# Create your models here.
class Conference(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    price=models.FloatField()
    capacity = models.IntegerField(validators=[MaxValueValidator (limit_value = 1000, message = "capacity cannot exceed 1000")])
    program = models.FileField(upload_to='files/', validators = [
        FileExtensionValidator(allowed_extensions = ['pdf', 'png', 'jpeg', 'jpg'])
    ])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="conferences")
    
    def clean (self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be set after start date")
        
    