from ..models import ShortenUrl
from django.http import JsonResponse
from rest_framework.views import APIView

class ShortenerByID(APIView):
    def delete(self, request, pk, format='json'):
        obj = ShortenUrl.objects.get(pk=pk)
        if obj:
            obj.delete()
        return JsonResponse({ "data": "delete"})
    
    def get(self, request, pk, format='json'):
        try:
            obj = ShortenUrl.objects.get(pk=pk)
        except Exception as e:
            obj = None
        if obj:
            return JsonResponse({
                "data": {
                    "url": obj.url,
                    "shortcode": obj.shortcode,
                }
            })
        return JsonResponse({
            "data": "No such shortcode"
})
