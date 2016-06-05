from django.db import models


class Aircraft(models.Model):
    name = models.CharField(max_length=100)


class Container(models.Model):
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)


class Parachute(models.Model):
    name = models.CharField(max_length=50)
    size = models.SmallIntegerField()


class Rig(models.Model):
    container = models.ForeignKey(Container)
    main_canopy = models.ForeignKey(Parachute, related_name='+')
    reserve = models.ForeignKey(Parachute, related_name='+', null=True, blank=True)


class Jump(models.Model):
    number = models.IntegerField(primary_key=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True, blank=True)
    equipment = models.ForeignKey(Rig, on_delete=models.SET_NULL, null=True, blank=True)
    exit_altitude = models.DecimalField(max_digits=4, decimal_places=1, default=12.5, blank=True)
    pull_altitude = models.DecimalField(max_digits=3, decimal_places=1, default=4.5, blank=True)
    notes = models.TextField()
    
    # returns seconds
    # assumes altitude in thousands of feet
    # assumes belly fly (lol)
    def estimate_freefall(self):
        fall_distance = float(self.exit_altitude) - float(self.pull_altitude)
        fall_time = 12.0 + (fall_distance-1) * 6.0 if fall_distance > 1 else fall_distance * 12.0
        return int(fall_time)

    freefall_time = property(estimate_freefall)
