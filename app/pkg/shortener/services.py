from string import ascii_letters, digits

from django.conf import settings
from django.utils.crypto import get_random_string

from app.pkg.shortener.models import ShortenedUrl


class ShortedUrlService:
    @classmethod
    def _generate_short_path(cls):
        ALLOWED_CHARS = ascii_letters + digits

        short_path = get_random_string(
            length=settings.SHORT_URL_LENGTH, allowed_chars=ALLOWED_CHARS
        )

        if ShortenedUrl.objects.filter(short_path=short_path).exists():
            return cls._generate_short_path()

        return short_path

    @classmethod
    def create_shorted_url(cls, url):
        short_path = cls._generate_short_path()
        obj, _ = ShortenedUrl.objects.get_or_create(url=url, short_path=short_path)

        return obj
