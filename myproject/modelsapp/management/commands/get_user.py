from django.core.management.base import BaseCommand
from modelsapp.models import User


class Command(BaseCommand):
    help = "Get user by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
