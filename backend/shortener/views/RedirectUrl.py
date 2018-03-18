from ..models import ShortenUrl
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView

class RedirectUrlView(APIView):
    def get(self, request, pk, format='json'):
        try:
            obj = ShortenUrl.objects.get(pk=pk)
        except Exception as e:
            obj = None
        if obj:
            return HttpResponseRedirect(obj.url)
        return JsonResponse({
            "data": "invalid short url"
        })