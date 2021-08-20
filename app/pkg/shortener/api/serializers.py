from rest_framework import serializers

from app.pkg.shortener.models import ShortenedUrl
from app.pkg.shortener.services import ShortedUrlService


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = ('url', 'shortened_url')
        read_only_fields = ('shortened_url',)
        extra_kwargs = {
            'url': {'write_only': True},
        }

    def create(self, validated_data):
        return ShortedUrlService.create_shorted_url(validated_data.get('url'))


class ShortenedCountSerializer(serializers.Serializer):
    shortened_urls_count = serializers.SerializerMethodField()

    def get_shortened_urls_count(self, obj):
        return ShortenedUrl.objects.all().count()


class MostPopularSerializer(serializers.Serializer):
    domain = serializers.CharField()
