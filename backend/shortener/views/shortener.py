# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import ShortenerSerializer
from ..models import ShortenUrl
# Create your views here.
class ShortenerListView(APIView):
    serializer_class = ShortenerSerializer

    def get(self, request, format='json'):
        shorten_urls_query = ShortenUrl.objects.all()
        paginator = Paginator(shorten_urls_query, 10)
        page = request.GET.get('page')
        
        try:
            shorten_urls = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            shorten_urls = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            shorten_urls = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        serializer = ShortenerSerializer(shorten_urls, many=True)
        # return Response(serializer.data)
        return JsonResponse({
                "data": serializer.data,
                "pagination": {
                    "count": paginator.num_pages,
                    "page": page,
                    }
                })

    def post(self, request, format='json'):
        serializer = ShortenerSerializer(data=request.data)
        if serializer.is_valid():
            data = ShortenUrl.objects.create(**serializer.data)
            output = serializer.data
            output['shortcode'] = data.shortcode
            return JsonResponse({ "data": output})
        else:
            return JsonResponse(serializer.errors)

        # return Response(serializer.data)