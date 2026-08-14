from django.db import models


class Teacher(models.Model):
    DIRECTIONS = [
        ('backend', 'Back-End'),
        ('frontend', 'Front-End'),
        ('smm', 'SMM'),
    ]

    name = models.CharField(max_length=200, verbose_name='Имя')
    direction = models.CharField(max_length=20, choices=DIRECTIONS, verbose_name='Направление')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название группы')
    mentor = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='groups',
        verbose_name='Ментор'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    avatar = models.ImageField(upload_to='students/', blank=True, null=True, verbose_name='Аватар')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='Группа'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name


class StudentMark(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks',
        verbose_name='Студент'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='marks',
        verbose_name='Учитель'
    )
    subject = models.CharField(max_length=100, verbose_name='Предмет')
    mark = models.PositiveIntegerField(verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'{self.student.name} — {self.subject}: {self.mark}'
