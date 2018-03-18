from rest_framework import serializers

class ShortenerSerializer(serializers.Serializer):
    url = serializers.URLField()
    shortcode = serializers.CharField(max_length=8, allow_blank=True, required=False)