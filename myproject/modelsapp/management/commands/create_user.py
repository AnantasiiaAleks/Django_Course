from django.core.management.base import BaseCommand
from modelsapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(
        #     name='John',
        #     email='john@example.com',
        #     password='secret',
        #     age=25
        # )
        # user = User(
        #     name='Neo',
        #     email='neo@example.com',
        #     password='secret2',
        #     age=58
        # )
        user = User(
            name='Jack',
            email='capitan@example.com',
            password='secret3',
            age=45
        )
        ...
        user.save()
        self.stdout.write(f'{user}')