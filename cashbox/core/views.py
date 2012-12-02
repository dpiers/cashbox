from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson
import requests


def index(request):
    context = {}
    return render(request, 'index.html', context)

def landing(request):
    context = {}
    return render(request, 'landing.html', context)

def ajax_beta_mailing_list_signup(request):
    email = request.POST.get('email')

    try:
        response = requests.post(
                    "https://api.mailgun.net/v2/lists/beta@cashbox.mailgun.org/members",
                    auth=('api', 'key-1ff5nchvhyewmpvkg1v9xo3qq-bbr7z1'),
                    data={'subscribed': True,
                          'address': email
                          })

    except Exception, e:
        data = simplejson.dumps({
            'success': False,
            'msg': str(e),
            'email': request.POST.get('email'),
        })

        return HttpResponse(data, mimetype='application/json')

    data = simplejson.dumps({
        'success': True,
        'msg': "Ajax - Beta MailingList Signup - Success",
        'email': email
        })

    return HttpResponse(data, mimetype='application/json')