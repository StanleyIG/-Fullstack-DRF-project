from django.core.management.base import BaseCommand
from toDoapp.models import Project, ToDo
from authapp.models import User
import random


class Command(BaseCommand):
    help = 'Создать 20 проектов с случайными пользователями в колличестве до 3-х на проект'

    def handle(self, *args, **options):
        all_users = User.objects.order_by('?')[:20]
        for i in range(20):
            project_users = random.sample(list(all_users), k=random.randint(1, 3))
            project = Project.objects.create(name=f'Project Name{i}', repository_link=f'https://example{i}.com')
            project.users.set(project_users)
            project.save()

        self.stdout.write(self.style.SUCCESS('Проекты созданы'))