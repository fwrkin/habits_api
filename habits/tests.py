# habits/tests.py
from django.test import TestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@example.com", password="testpass123")
        Habit.objects.create(
            user=self.user,
            place="Home",
            time="12:00:00",
            action="Drink water",
            is_pleasant=False,
        )

    def test_habit_creation(self):
        habit = Habit.objects.get(action="Drink water")
        self.assertEqual(habit.place, "Home")
        self.assertEqual(habit.time.strftime("%H:%M:%S"), "12:00:00")
