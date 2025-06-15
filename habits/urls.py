from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("public-habits", PublicHabitListAPIView.as_view(), name="public-habit-list"),
    path("habits", HabitListAPIView.as_view(), name="habit-list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("habits/<int:pk>/update", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("habits/<int:pk>/delete", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
