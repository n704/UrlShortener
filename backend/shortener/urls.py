from django.conf.urls import url
from shortener.views import ShortenerListView, ShortenerByID

urlpatterns = [
    url(r'^shortener/$', ShortenerListView.as_view()),
    url(r'^shortener/(?P<pk>[0-9a-z]+)$', ShortenerByID.as_view()),
]