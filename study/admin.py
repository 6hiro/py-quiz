from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import (
    Category,
    Tag,
    Study
)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Study, MarkdownxModelAdmin)
