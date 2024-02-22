from django.db import models
from materials.models import Course, Lesson
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'city', 'avatar']

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(
        User, related_name='payments', on_delete=models.CASCADE)
    payment_date = models.DateField()
    course = models.ForeignKey(
        Course, related_name='payments', on_delete=models.CASCADE, null=True)
    lesson = models.ForeignKey(
        Lesson, related_name='payments', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]
    payment_method = models.CharField(
        max_length=10, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"{self.user.email} - {self.payment_date}"
