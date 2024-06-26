from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


# Custom user manager
class MyAccountManager(BaseUserManager):
    # Function to create a new user
    def create_user(self, email, username, password=None):
        # Validate email and username
        if not email:
            raise ValueError('Users must have an email address.')
        if not username:
            raise ValueError('Users must have a username.')

        # Create new user instance
        user = self.model(
            # make characters lowercase
            email=self.normalize_email(email),
            username=username,
        )

        # Set password and save user
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Function to create a new superuser
    def create_superuser(self, email, username, password):
        # Create new user instance
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        # Set user as admin, staff, and superuser
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Function to define profile image filepath
def get_profile_image_filepath(self):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'


# Function to define default profile image
def get_default_profile_image():
    return "images/dummy_image.png"


# Custom user model
class Account(AbstractBaseUser):
    # Fields
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    profile_image   = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
    hide_email      = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    # Default return value when you don't access any fields
    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

