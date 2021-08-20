from django.contrib import admin

from app.pkg.shortener.models import ShortenedUrl


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'shortened_url',)
    search_fields = ('url',)
