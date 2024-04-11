from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField("Biography", blank=True)
    skills = models.CharField(max_length=255, blank=True)
    language = models.CharField("Languages Spoken", max_length=255, blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience = models.TextField("Work Experience", blank=True)

