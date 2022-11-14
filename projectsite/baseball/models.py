from django.db import models

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

class Person(BaseModel):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5, null=True)

class Club(BaseModel):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Person, on_delete=models.CASCADE)
    dorm_latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    dorm_longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)

class Play(BaseModel):
    player = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Club, on_delete=models.CASCADE)
    string_no = models.CharField(max_length=100)
    pos = models.ForeignKey(Position, on_delete=models.CASCADE)