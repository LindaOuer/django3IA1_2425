from django.db import models
import re
from django.core.validators import ValidationError

# Create your models here.
def validate_title (value):
    if not re.match(r'^[A-Za-z\s]+$', value):
        raise ValidationError('This field should only contain letters')
class Category(models.Model):
    title=models.CharField(max_length=255, validators = [validate_title])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    class Meta: 
        verbose_name_plural = "categories"