from django.db import models
from django.contrib.auth.models import AbstractUser

# defining custom User model provides ability to easily edit the user model later while still retaining the same features as the default Django User
class User(AbstractUser):
    pass
