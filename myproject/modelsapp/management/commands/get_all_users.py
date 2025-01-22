from django.core.management.base import BaseCommand
from modelsapp.models import User


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')