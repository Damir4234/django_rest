from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth import get_user_model
from users.models import Payment
from materials.models import Course, Lesson

User = get_user_model()


class Command(BaseCommand):
    help = 'Fill the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting all data...'))

        with transaction.atomic():
            Payment.objects.all().delete()
            User.objects.all().delete()
            Course.objects.all().delete()
            Lesson.objects.all().delete()

            self.stdout.write(self.style.SUCCESS(
                'All data deleted successfully.'))

            self.stdout.write(self.style.WARNING('Filling the database...'))

            user1 = User.objects.create(
                email='example@example.com', phone='1234567890', city='City', avatar='avatars/default.jpg')

            course1 = Course.objects.create(
                title='Sample Course 1', description='Description of Sample Course 1')
            course2 = Course.objects.create(
                title='Sample Course 2', description='Description of Sample Course 2')

            lesson1 = Lesson.objects.create(
                title='Sample Lesson 1', description='Description of Sample Lesson 1', course=course1)
            lesson2 = Lesson.objects.create(
                title='Sample Lesson 2', description='Description of Sample Lesson 2', course=course2)

            payment1 = Payment.objects.create(
                user=user1, payment_date='2024-02-22', course=course1, amount=100, payment_method='cash')

            self.stdout.write(self.style.SUCCESS(
                'Database filled successfully.'))
