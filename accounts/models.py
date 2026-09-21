from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

import uuid



import secrets
import string

def generate_referral_code():
    characters = string.ascii_uppercase + string.digits
    return "QB" + "".join(secrets.choice(characters) for _ in range(8))

class User(AbstractUser):
    referral_code = models.CharField(max_length=10 , default=generate_referral_code, unique=True , editable=False)
    referred_by = models.ForeignKey("self", on_delete=models.SET_NULL,null=True,
        blank=True,
        related_name="referrals")
    position = models.CharField(max_length=10,
        choices=[
            ("left", "Left"),
            ("right", "Right"),
        ],
        null=True,
        blank=True,
    )