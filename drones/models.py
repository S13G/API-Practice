from django.db import models

# Create your models here.


class DroneCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Drone(models.Model):
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(DroneCategory, on_delete=models.CASCADE, related_name="drones")
    manufacturing_date = models.DateTimeField()
    has_it_completed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    name = models.CharField(max_length=150, default='')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Competition(models.Model):
    pilot = models.ForeignKey(Pilot, related_name="competitions", on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()

    class Meta:
        # order by distance in descending order
        ordering = ('-distance_in_feet',)