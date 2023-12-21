from pathlib import Path

from django.core.management.base import BaseCommand

from quizapp.models import User


BASE_DIR = str(Path(__file__).resolve().parent)+'/'


class Command(BaseCommand):
    help = 'Add a user to'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(BASE_DIR+options['filename'][0]) as file:
            content = file.readlines()
            for user in content:
                line = user.strip().split(" ")
                first_name = line[0]
                last_name = line[1]
                full_name = line[2]
                email = line[3]
                username = line[4]
                User.objects.create(first_name=first_name, last_name=last_name, email=email,
                                    username=username)

        self.stdout.write(
            self.style.SUCCESS('Successfully')
        )