from django.db import models


# 카테고리
class Category(models.Model):
    title = models.CharField(
        max_length=20,
        help_text="Enter the title of the bucket",
    )

    def __str__(self):
        return self.title

# 버킷
class Bucket(models.Model):
    title = models.CharField(
        max_length=20,
        help_text="Enter the title of the bucket",
    )
    content = models.TextField(
        max_length=100,
        help_text="Enter a brief content",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )
