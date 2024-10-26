from django.db import models
from django.contrib.auth.models import AbstractUser
from conferenceApp.models import Conference
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

def email_validator(value):
    if not value.endswith("@esprit.tn"):
        raise ValidationError('Invalid email address, only @esprit.tn are allowed!')

class Participant(AbstractUser):
    cin_validator = RegexValidator(
        regex = r'^\d{8}$',
        message="This field must contain exactly 8 digits"
    )
    cin=models.CharField(primary_key=True, max_length=8, validators=[cin_validator])
    email=models.EmailField(unique=True,max_length=255, validators=[email_validator])
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
    reservations = models.ManyToManyField(Conference, through='Reservation', related_name='reservations')


class Reservation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    def clean(self):
        if self.conference.start_date < self.reservation_date :
            raise ValidationError("You can only reserve an upcoming conference")
        
    class Meta:
        verbose_name_plural = 'Reservations'
        unique_together = ('conference', 'participant')