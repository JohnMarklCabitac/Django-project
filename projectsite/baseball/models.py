from django.db import models
from django.utils import timezone

#Create your models here.
# firstname = models.CharField(max_length=100)
# lastname = models.CharField(max_length=100)
# email = models.EmailField(null=True, blank=True, max_length=100)
# height = models.DecimalField(max_digits=10,decimal_places=5,null=True)
# latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
# isActive = models.BooleanField(default=False, verbose_name="Zoning Fee")
# birthdate = models.DateField(default=timezone.now, blank=True)
# coach = models.ForeignKey(Person, on_delete=models.CASCADE)

class BaseModel(models.Model):
    create_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Position(BaseModel):
    description = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.description}"


class Person(BaseModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    def __str__(self):
        return f"{self.lastname}, {self.firstname}"


class Club(BaseModel):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    dorm_latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    dorm_longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    team_pic = models.ImageField(default="defaultimg.png", null=True, blank=True, verbose_name="Team Image")
    
    def __str__(self):
        return f"{self.name}"


class Play(BaseModel):
    player = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Team")
    string_no = models.CharField(max_length=100)
    pos = models.ForeignKey(Position, on_delete=models.CASCADE)
    
class Match(BaseModel):
    team1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Team1")
    team2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Team2")
    score_t1 = models.IntegerField()
    score_t2 = models.IntegerField()
    winner = models.ForeignKey(Club, on_delete=models.CASCADE, related_name = "Winner")
    game_date = models.DateField(default=timezone.now, blank=True, verbose_name="Date of Issuance")

    def __str__(self):
        return f"{self.team1} vs {self.team2}"
