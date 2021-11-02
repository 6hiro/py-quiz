import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE, RestrictedError
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Study(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('タイトル', max_length=120)
    content = MarkdownxField('テキスト')
    preview_content = models.TextField('プレビュー', blank=True, null=True)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=CASCADE)
    tags = models.ManyToManyField(
        Tag, blank=True, related_name='stydy_tags')
    liked = models.ManyToManyField(
        get_user_model(), blank=True, related_name='study')
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return f"{self.title}-{self.category}"

    def get_text_markdownx(self):
        return mark_safe(markdownify(self.content))

    def get_preview_content(self):
        return self.preview_content[:200]
