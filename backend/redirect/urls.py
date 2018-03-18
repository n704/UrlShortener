from django.conf.urls import url
from views import RedirectUrlView
urlpatterns = [
    url(r'^(?P<pk>[0-9a-z]+)$', RedirectUrlView.as_view())
]