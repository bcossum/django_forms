from django.db import models
from django.core.exceptions import ValidationError
from django import forms
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def validate_length(value):
  if len(value) < 3:
    raise ValidationError(
      '{} must be longer than: 2'.format(value)
  )

def validate_email(value):
  if not EMAIL_REGEX.match(value):
    raise ValidationError(
    '{} must be in proper email format "example@example.com"'.format(value)
  )
  


class User(models.Model):
  first_name = models.CharField(max_length=255, validators=[validate_length])
  last_name = models.CharField(max_length=255, validators=[validate_length])
  email = models.CharField(max_length=255, validators=[validate_email])
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
