from django.contrib.auth.models import Group
from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def add_user_to_developer_group(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        developer_group, _ = Group.objects.get_or_create(name='developer')
        instance.groups.add(developer_group)
