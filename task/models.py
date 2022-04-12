from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def save_user(self, email, password, **kwargs):

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs['is_superuser'] = False
        kwargs['is_staff'] = False
        return self.save_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)

        if not kwargs.get('is_superuser'):
            raise ValueError('is_superuser should be true')
        kwargs['is_staff'] = True
        return self.save_user(email=email, password=password, **kwargs)

    def create_staffuser(self, email, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = False

        return self.save_user(email, password, **kwargs)


class DateTracker(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser):
    email = models.EmailField(max_length=150, unique=True)

    fullname = models.CharField(max_length=150, blank=True, null=True)
    USERNAME_FIELD = "email"
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()


class Task(DateTracker):
    title = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    schedule_time = models.TimeField()
    user = models.ForeignKey(User, related_name="tasks",
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
