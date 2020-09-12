from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    image = models.ImageField(default='default.JPG', upload_to='profile_pics')
    first_name = models.CharField(max_length=30, default="",  blank=False)
    last_name = models.CharField(max_length=30, default="", blank=False)
    age = models.IntegerField(default=18)
    goal = models.CharField(max_length=30, choices=goal_choices, default="")
    experience = models.CharField(max_length=30, choices=experience_choices, default="")
    city = models.CharField(max_length=30, choices=city_choices, default="")
    gym_membership = models.CharField(max_length=30, choices=gym_choices, default="")
    sex = models.CharField(max_length=30, choices=sex_choices, default="")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()