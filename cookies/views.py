from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Cookie

import requests

# test comment
@csrf_exempt
def get_github_url(request):

    print("inside get_github_url")

    cookie = Cookie.objects.all().reverse()[0].cookie_text
    print("cookie", cookie)

    headers = {

        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cookie": cookie,
        "referer": "http://localhost:8080/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    url = 'https://github.com/login/oauth/authorize?client_id=d83ac1ef7822f3087e4b&redirect_uri=http://localhost:8080/login&scope=user'

    r = requests.get(url, headers= headers, allow_redirects=True)
    print("printing url", r.url)
    return HttpResponse(r.url)
