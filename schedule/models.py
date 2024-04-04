from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')


class Trainer(models.Model):
    objects = None
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='trainer_profile')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    gyms = models.ManyToManyField('Gym', related_name='trainers')

    def __str__(self):
        return self.user.get_full_name()


class Gym(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    objects = None
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='schedules')
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.trainer.user.get_full_name()}-{self.day_of_week}{self.start_time}-{self.end_time}at{self.gym.name}"
