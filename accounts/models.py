from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        """
            Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        #user.is_staff = is_staff
        user.is_active = is_active
        user.is_admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
            Creates and saves a staffuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
            Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(_('full_name'), max_length=255, blank=True)
    first_name = models.CharField(_('first_name'), max_length=255, blank=True)
    last_name = models.CharField(_('last_name'), max_length=255, blank=True)
    phone = models.CharField(_('phone_number'), max_length=30, blank=True)

    #date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []#'date_of_birth']

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin