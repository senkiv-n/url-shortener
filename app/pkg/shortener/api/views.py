from django.utils.translation import ugettext_lazy as _
from django.http import Http404
from django.shortcuts import redirect
from django.views import View
from django.db.models import Count
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from app.pkg.shortener.api.serializers import ShortenerSerializer, ShortenedCountSerializer, MostPopularSerializer
from app.pkg.shortener.models import ShortenedUrl


class ShortenerView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ShortenedUrl.objects.all()
    serializer_class = ShortenerSerializer

    @action(detail=False, serializer_class=ShortenedCountSerializer)
    def urls_count(self, request):
        sz = self.get_serializer(request.data)
        return Response(sz.data)


class MostPopularView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MostPopularSerializer

    def get_queryset(self):
        qs = ShortenedUrl.objects.all().values('domain').annotate(domain_count=Count('*')).distinct()

        return qs.order_by('-domain_count')


class RedirectUrlView(View):
    def get(self, request, shortened_path):
        try:
            shortened_url = ShortenedUrl.objects.get(short_path=shortened_path)
        except ShortenedUrl.DoesNotExist:
            raise Http404(_('Invalid Url'))

        return redirect(shortened_url.url)
