from django.core.management import BaseCommand

from profiles.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create profile to superuser')
        profile, created = Profile.objects.get_or_create(
            fullName='Robert',
            email='admin@admin.com',
            phone='89056219865',
            user_id=1
        )
        self.stdout.write(self.style.SUCCESS('Profile created!'))


