import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from address.models import Address

class UserManager(BaseUserManager):

    def _create_user(self, name, email, password, is_superuser, **extra_fields):
        now = timezone.now()

        if not name:
            raise ValueError(_('The given username must be set'))

        email = self.normalize_email(email)

        user = self.model(name=name, email=email, is_active=True, is_superuser=is_superuser, last_login=now, created_at=now, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user


    def create_user(self, name, email=None, password=None, **extra_fields):

        return self._create_user(name, email, password, False, **extra_fields)


    def create_superuser(self, name, email, password, **extra_fields):

        user=self._create_user(name, email, password, True, **extra_fields)

        user.is_active=True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    GENDER_CHOICES = [
        (0, 'MAN'),
        (1, 'WOMAN'),
        (2, 'NOT_BINARY'),
        (3, 'OTHER')
    ]

    USER_TYPE = [
        (0, 'DEAF'),
        (1, 'INTERPRETER'),
        (2, 'HOSPITAL_STAFF'),
    ]

    name = models.CharField(_('name'), max_length=30)

    email = models.EmailField(_('email address'), max_length=255, unique=True)
    born_date = models.DateField(_('born_date'), null=True)
    gender = models.IntegerField(
        choices=GENDER_CHOICES,
        default=0
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=0)

    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))

    is_mail_confirmed= models.BooleanField(_('email confirmed'), default=False, help_text=_('Designates whether this user has confirmed his account.'))


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def getStringType(self):

        stringType = ""

        if self.user_type == 0:
            "Deaf"

        elif self. user_type == 1:
            "Interpreter"

        elif self.user_type == 2:
            "Hospital Staff"
            
        return stringType

    def getFirstName(self):
        return self.name.split()[0]

    def getGender(self):
        gender = {
            0: "Masculino",
            1: "Feminino",
            2: "N??o binario",
            3: "Outro"
        }
        return gender[self.gender]