from django.test import TestCase
from .models import Room, Student

class RoomModelTest(TestCase):
    def test_room_creation(self):
        room = Room.objects.create(room_number="101", capacity=2)
        self.assertEqual(room.room_number, "101")
        self.assertEqual(room.capacity, 2)

class StudentModelTest(TestCase):
    def test_student_registration(self):
        room = Room.objects.create(room_number="102", capacity=2)
        student = Student.objects.create(name="John Doe", roll_number="TCE123", room=room)
        self.assertEqual(student.name, "John Doe")
        self.assertEqual(student.room.room_number, "102")
