from django.db import models
from main.models import BaseModel

# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# 버킷
class Bucket(BaseModel):
    name = models.CharField(max_length=20, null=True)
    content = models.TextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
