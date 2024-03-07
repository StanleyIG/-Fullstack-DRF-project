import json
import random
import string
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from authapp.models import User


class Command(BaseCommand):
       help = 'Создать 20 тестовых пользователей'

       def handle(self, *args, **kwargs):
           for i in range(1, 21):
               username = f'User{i}'
               password = ''.join(random.choices(string.ascii_letters, k=8))
               email = f'{username.lower()}@example.com'
               hashed_password = make_password(password)
               user = User.objects.create(username=username, email=email, is_active=True, is_staff=True)
               user.set_password(hashed_password)
               user.save()
             
           self.stdout.write(self.style.SUCCESS('Пользователи созданы'))