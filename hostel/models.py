from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.room_number

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
