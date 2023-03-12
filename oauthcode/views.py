from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404 # JsonResponse and HttpResponseRedirect may be used in other APIs
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Ocode

import json
# import requests

# Get the balance of a user
@require_http_methods(['GET'])
@csrf_exempt
def get_code(request):
    print("code before try")
    code = Ocode.objects.all()[0].oauth_code
    print(code)
    # return JsonResponse({"code": code})
    return HttpResponse(code)

    # try:
    #     code = Ocode.objects.filter(id=1).values()
        
    #     # code = Ocode.objects.get(id=1)
    #     print("code")
    #     print(code)
    #     return JsonResponse({"code": code})
    # except Ocode.DoesNotExist:
    #     raise Http404("Unknown Error")