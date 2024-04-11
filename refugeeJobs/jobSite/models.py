from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField("Biography", blank=True)
    skills = models.CharField(max_length=255, blank=True)
    language = models.CharField("Languages Spoken", max_length=255, blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience = models.TextField("Work Experience", blank=True)

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    requirements = models.TextField()
    salary = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    qualifications = models.CharField(max_length=100)


    def __str__(self):
        return self.title

