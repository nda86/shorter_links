from django.urls import path, re_path
from .views import UrlHandler, get_original_url


urlpatterns = [
    path('post', UrlHandler.as_view()),
    re_path('s/(?P<hash>.+)$', get_original_url)
]