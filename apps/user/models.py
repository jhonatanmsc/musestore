from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.user.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(u'nome', max_length=100, null=True, blank=True)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(u'senha', max_length=250, null=True, blank=True)
    is_superuser = models.BooleanField(u'super usuário', default=False)
    is_staff = models.BooleanField(u'usuário do sistema', default=False)
    is_active = models.BooleanField(u'ativo', default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return f'{self.name}'
