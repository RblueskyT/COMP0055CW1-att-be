from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404 # JsonResponse and HttpResponseRedirect may be used in other APIs
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .models import Ocode

import json
import requests

# Get the balance of a user
@require_http_methods(['GET'])
@csrf_exempt
def get_code(request):
    print("code before try")
    
    code = Ocode.objects.all().reverse()[0].oauth_code
    print(code)
    # return JsonResponse({"code": code})
    return HttpResponse(code)

@require_http_methods(['GET'])
@csrf_exempt
def get_github_url(request):

    print("inside get_github_url")

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "_octo=GH1.1.1696782673.1665767748; _device_id=5ad35520b79020860883d0baba9be8b4; amp_d915a9=iQIRaEJJ0JoocxZdIYOjvj.b2VobDNDcVc4UVJBUUVLODYxQ0g5RDlYS3JMMg==..1ggffmt8s.1ggffmtgt.0.2.2; user_session=Ed0PZDpaefw_xcc1gO0otu2qy20azry-aQWfOf1KPVjRM6SO; logged_in=yes; dotcom_user=ArwaMAlhazmi; color_mode=%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FRiyadh; amp_adc4c4=_U0BQO6I_nSZxgx4GdSIp8...1grbgpv1l.1grbgpv1l.0.0.0; has_recent_activity=1; _gh_sess=bN0MnZBp8%2B7QPDVXqBjfn7QmmpYK2ZmRBZTugMc89KMgWEK3pRtqaCbp21MvYgoXLxOFEAczclEcGHmuEtRv%2FQPf9lBOqAbgdIdkbhtaWqy3P%2FS7R%2Bgrc20v4rFNTqpR6SlaQWd0brI5CViD2rEx3XzhwxObDxijZFPDlpx0WfI3vY9jUaNBdp9jhGmSBClyxliKOsqJZ%2FEzf1sTAImJyx9jWyfeT3a3fJTUc60dp4Y5IMT374OflBEJQSIS8hZEl11e0LzkzgN%2F0HddSp7q3TzD5h0LFmgv%2BjONTfXXlQAqi78nkDefo%2BTfSwkhv1CRsTlLuVGtz3tDOIIxqkBgBEzAVn%2BUXLtzjFRj4DOYcqD3xO867PtJvleTe5dQofcoI8ObQeSbcKpyted4jdYZkP0BZeyZYp0NP2gKxzAaJgDDYL5urPWBaap9fkcrfXKqwiduRrfq0yCjFGr9WQIGpc5UXvKeOu4vkI28JjHasxf3ISZpxHYulzHQSZUW%2F4DAhbYu204xmAVY--TeDTifnOohQB47Kh--MWDnNbw8zELdovHzLgMU7g%3D%3D",
        "referer": "http://localhost:8080/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    url = 'https://github.com/login/oauth/authorize?client_id=d83ac1ef7822f3087e4b&redirect_uri=http://localhost:8080/login&scope=user'

    r = requests.get(url, headers= headers, allow_redirects=True)
    print("printing url", r.url)
    return HttpResponse(r.url)


    # try:
    #     code = Ocode.objects.filter(id=1).values()
        
    #     # code = Ocode.objects.get(id=1)
    #     print("code")
    #     print(code)
    #     return JsonResponse({"code": code})
    # except Ocode.DoesNotExist:
    #     raise Http404("Unknown Error")