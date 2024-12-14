from django.contrib import admin

from core.models import TextModel


class TextModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "text"]


admin.site.register(TextModel, TextModelAdmin)
