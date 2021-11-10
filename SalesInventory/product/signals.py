# from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Category

@receiver(post_save, sender=Category)
def create_category(sender, instance, created, **kwargs):
    
    if created:
        print("Category signals")
        # Profile.objects.create(user=instance)

@receiver(post_save, sender=Category)
def save_category(sender, instance, **kwargs):
    print(instance)
    print("\n\nsave is calling....!\n\n" )
    print(kwargs.keys())
    print(kwargs['created'])
    # print(sender)
    print(kwargs['using'])
    print(kwargs['raw'])
    # instance.profile.save()

@receiver(post_delete, sender=Category)
def delete_category(sender, instance, **kwargs):
    print("\n\ndelete is calling....!\n\n" )