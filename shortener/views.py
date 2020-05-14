from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect

from .models import Url


class UrlHandler(APIView):
    def post(self, request):
        url, _ = Url.objects.get_or_create(url=request.POST['original_url'])
        short_url = url.url_short
        return Response({'short_url': short_url})


def get_original_url(request, hash):
    url = Url.objects.filter(url_hash=hash).first()
    return HttpResponseRedirect(url.url)
