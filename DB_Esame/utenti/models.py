from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UtenteManager(BaseUserManager):
    def create_user(self, email, nome, cognome, password=None):
        if not email:
            raise ValueError('L\'email è obbligatoria')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, cognome=cognome)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cognome, password):
       user = self.create_user(email, nome, cognome, password)
       user.is_staff=True
       user.is_superuser=True
       user.save(using=self._db)
       return user
   
class Utente(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtenteManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cognome']

    def __str__(self):
        return f"{self.nome} {self.cognome} <{self.email}>"