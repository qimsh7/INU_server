import os
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4

# 포스트(데이트)
class Post(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Enter the title of the post",
    )
    content = models.TextField(
        max_length=200,
        help_text="Enter a brief content",
    )
    writer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    # location

    def upload_to_func(instance, filename):
        prefix = timezone.now().strftime("%Y/%m/%d")
        file_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출
        return "/".join(
            [prefix, file_name, extension, ]
        )
    photo = models.ImageField(
        upload_to=upload_to_func,
        blank=True,
    )

    def __str__(self):
        return self.name
