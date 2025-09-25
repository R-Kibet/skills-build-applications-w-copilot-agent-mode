from djongo import models

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    dummy = models.CharField(max_length=1, default='X')  # Dummy field for migration detection
    def __str__(self):
        return self.name

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    dummy = models.CharField(max_length=1, default='X')
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    dummy = models.CharField(max_length=1, default='X')
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    dummy = models.CharField(max_length=1, default='X')
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    dummy = models.CharField(max_length=1, default='X')
    def __str__(self):
        return f"{self.team.name}: {self.points}"
