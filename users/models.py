from django.db import models
from materials.models import Course, Lesson
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import UserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone, city, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          phone=phone, city=city, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, city, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, phone, city, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'city']

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
