from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.utils import timezone

class University(models.Model):
    university_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    decryption = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Housing(models.Model):
    housing_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=5)
    university = models.ForeignKey(University, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Institute(models.Model):
    institute_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    decryption = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    decryption = models.CharField(max_length=200)
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=10)
    decryption = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    

class User(AbstractUser):
    middle_name = models.CharField(max_length=150)

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    monitor = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE, blank = True, null = True)
    start_semestr = models.DateField()
    end_semestr = models.DateField()

    def __str__(self):
        return self.title


class shedule(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lesson = models.CharField(max_length=50)
    teacher = models.CharField(max_length=100, blank=True)
    classroom = models.CharField(max_length=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    type_lesson = models.PositiveSmallIntegerField()
    parity_week = models.PositiveSmallIntegerField()
    day_week = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.lesson