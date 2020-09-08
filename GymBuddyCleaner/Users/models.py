from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):

    goal_choices = [
        ('bulk', 'Bulk'),
        ('cut', 'Cut'),
        ('tone', 'Tone')
    ]

    experience_choices = [
        ('beginner', 'Beginner'), 
        ('intermediate', 'Intermediate'), 
        ('advanced', 'Advanced'), 
    ]

    sex_choices = [
        ("male", "Male"),
        ("female", "Female")
    ]

    city_choices = [
        ('san luis obispo', 'San Luis Obispo'),
        ('atascadero', 'Atascadero')
    ]

    gym_choices = [
        ('ASI Recreation Center', 'ASI Recreation Center'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE )
    image = models.ImageField(default='default.JPG', upload_to='profile_pics')

    first_name = models.CharField(max_length=30, default="", primary_key=True, blank=False)
    last_name = models.CharField(max_length=30, default="", blank=False)
    age = models.IntegerField(default=18)
    goal = models.CharField(max_length=30,choices=goal_choices, default="")
    experience = models.CharField(max_length=30,choices=experience_choices, default="")
    city = models.CharField(max_length=30, choices=city_choices, default="")
    gym_membership = models.CharField(max_length=30, choices=gym_choices, default="")
    sex = models.CharField(max_length=30,choices=sex_choices, default="")

    def __str__(self):
        return f'{self.user.username} Profile'
