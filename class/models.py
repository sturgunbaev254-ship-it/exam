from django.db import models


class Teacher(models.Model):
    DIRECTIONS = [
        ('backend', 'Back-End'),
        ('frontend', 'Front-End'),
        ('smm', 'SMM'),
    ]

    name = models.CharField(max_length=200)
    direction = models.CharField(
        max_length=20,
        choices=DIRECTIONS
    )

    def str(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    mentor = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='groups'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    avatar = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='students'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class StudentMark(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks'
    )
    mark = models.PositiveIntegerField()
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.student.name} - {self.mark}'
