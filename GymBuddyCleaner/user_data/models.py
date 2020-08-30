from django.db import models
from django.contrib.auth.models import User

# Create your models here.
goal_choices = ( 
    ("Bulk", "Bulk"), 
    ("Cut", "Cut"),
    ("Tone", "Tone"),
    
)

experience_choices = (
    ("beginner", "beginner"), 
    ("intermediate", "intermediate"), 
    ("advanced", "advanced"), 
)

sex_choices = (
    ("male", "male"),
    ("female", "female")
)

city_choices = (
    ('San Luis Obispo', 'San Luis Obispo'),
    ('Atascadero', 'Atascadero')
)

gym_choices = (
    ('ASI Recreation Center', 'ASI Recreation Center'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

class user_data(models.Model):
    name = models.CharField(max_length=30, default="", primary_key=True)
    age = models.IntegerField(default=0)
    goal = models.CharField(max_length=30,choices=goal_choices, default="")
    experience = models.CharField(max_length=30,choices=experience_choices, default="")
    city = models.CharField(max_length=30, choices=city_choices, default="")
    gym_membership = models.CharField(max_length=30, choices=gym_choices, default="")
    sex = models.CharField(max_length=30,choices=sex_choices, default="")

    mapDict = {
    'beginner': 1,
    'intermediate': 2,
    'expert': 3,
    'bulk': 3,
    'cut': 2,
    'tone': 1
  }

    def __str__(self):
        return 'Name: ' + self.name + ' Age: ' + str(self.age)

    def __lt__(self, other):
        return self.score < other.score

    def user_uniqueScore(self):
        self.score = self.age + self.mapDict[self.exp] + self.mapDict[self.goal]
        return self.score

class SendMessage(models.Model):
    author = models.OneToOneField(user_data, on_delete=models.CASCADE, related_name="author", default="",  primary_key=True)
    message = models.CharField(max_length=30, default="")