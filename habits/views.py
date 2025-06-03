from django.shortcuts import get_object_or_404
from rest_framework import generics


from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer, PublicHabitSerializer
from habits.services import create_replacements, make_replacements
from users.permissions import IsUser


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = PublicHabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsUser,)
