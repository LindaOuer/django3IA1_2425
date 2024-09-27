from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Participant(AbstractUser):
    cin=models.CharField(primary_key=True, max_length=8)
    email=models.EmailField(unique=True,max_length=255)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username=models.CharField(unique=True,max_length=255)
    USERNAME_FIELD='username'
    CHOIX= (
        ('ETUDIANT','ETUDIANT'),
        ('CHERCHEUR','CHERCHEUR'),
        ('ENSEIGNANT','ENSEIGNANT'),
        ('DOCTEUR','DOCTEUR'),
    )
    participant_category=models.CharField('participant_category',choices= CHOIX, max_length=255)
