from django.db import models
from django.utils import timezone

# 여기 커플 정보를 저장하고 다른 앱들에서 import해서 일괄적으로 사용하도록 해야할지?
# 예를 들면 처음만난날

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True,
        self.deleted_at = timezone.now()
        self.save()
