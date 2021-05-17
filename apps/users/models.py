from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from utils.uploads import upload_instance


class UserManager(BaseUserManager):
    """
        This is a manager for Account class
    """
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an Email address")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email),
                                password=password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
      Custom user class inheriting AbstractBaseUser class
    """
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    middle_name = models.CharField(verbose_name='Отчество',
                                   max_length=255,
                                   null=True,
                                   blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона',
                                    max_length=20)
    avatar = models.ImageField(verbose_name='Фото', upload_to=upload_instance)
    email = models.EmailField(verbose_name='Почта', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Последний вход',
                                      auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
