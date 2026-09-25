from django.db.models.signals import post_save, post_delete
from .models import Student
from django.dispatch import receiver

@receiver(post_save, sender=Student)
def creat_student(sender,instance,created,**kwargs):
    if created:
        print(f'Студент{instance.name} успешно создан!!!')
    else:
        print(f"Обновлён{instance.name} успешно обновлён!!!")

@receiver(post_delete, sender=Student)
def delete_student(sender,instance,**kwargs):
        print(f'Удалён{instance.name}студент!!!')