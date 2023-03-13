from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404 # JsonResponse and HttpResponseRedirect may be used in other APIs
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Cookie

import json
import requests

# # Get the balance of a user
# @require_http_methods(['GET'])
# @csrf_exempt
# def get_code(request):
#     print("code before try")
    
#     code = Ocode.objects.all().reverse()[0].oauth_code
#     print(code)
#     # return JsonResponse({"code": code})
#     return HttpResponse(code)

# Create your views here.
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
