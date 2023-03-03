from django.db import models
from django.contrib.auth.models import User
from main.models import BaseModel

# 편지
class Letter(BaseModel):
    content = models.TextField(
        max_length=100,
    )
    writer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.id
