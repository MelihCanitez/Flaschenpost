from django.db import models
import uuid

# Create your models here.
class Forklift(models.Model):

    serial_no = models.CharField(max_length=30, unique=True)

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    max_load = models.IntegerField(default=800)
    hours_run = models.FloatField(default=0)
    next_check = models.DateField(null=True, blank=True, default=None)

    can_operate = models.BooleanField(default=True)
    allowed_operators = models.JSONField(default=list)

    def __str__(self):
        return f'{self.serial_no}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Forklift'
        verbose_name_plural = 'Forklifts'

class Partner(models.Model):
    pid = models.TextField(primary_key=True, default = uuid.uuid4)
    name = models.TextField(null=True)
    email = models.TextField(null=True)

class Reparatur(models.Model):
    rid = models.TextField(primary_key=True, default = uuid.uuid4)
    schadeneintritt = models.TextField()
    fertigstellung = models.TextField()
    standort = models.TextField()
    forkliftid = models.ForeignKey(Forklift, on_delete=models.CASCADE, null=True)
    partnerid = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)