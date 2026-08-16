from django.db.models.signals import post_save

from .models import Student
from django.dispatch import receiver

@receiver(post_save, sender=Student)
def creat_phone(sender,instanse,created,**kwargs):
    if created:
        print(f'Продукт{instanse.name} успешно создан!!!')