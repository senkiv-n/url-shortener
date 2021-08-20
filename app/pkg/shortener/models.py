from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from urllib.parse import urlparse


class ShortenedUrl(models.Model):
    url = models.URLField(_('original url'), max_length=512)
    short_path = models.CharField(_('short url'), max_length=15, db_index=True, unique=True)
    domain = models.CharField(_('domain from url'), max_length=50)

    class Meta:
        verbose_name = _('Shortened Url')
        verbose_name_plural = _('Shortened Urls')

    def __str__(self):
        return self.shortened_url + _(' from ') + self.url

    def _shortened_url(self):
        return Site.objects.get_current().domain + str(self.short_path)

    shortened_url = property(_shortened_url)

    def save(self, *args, **kwargs):
        self.domain = urlparse(self.url).netloc
        super().save(*args, **kwargs)
