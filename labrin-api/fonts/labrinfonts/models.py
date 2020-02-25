from django.conf import settings
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_admin=False, is_staff= False, is_active = True ):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users: must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not full_name:
            raise ValueError('Users must have a full name')    
        user = self.model(
            email=self.normalize_email(email),
            full_name = full_name,
        )

        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, full_name, password = None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.staff = True
        user.admin = False
        user.active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password = None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    full_name = models.CharField(verbose_name = 'full name', max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):         
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
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin



    def get_absolute_url(self):
        return reverse("index")    
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class FontFamily(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")    

class Font(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey('FontFamily', on_delete=models.CASCADE)
    font_file = models.FileField(upload_to = 'font_files')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index")      