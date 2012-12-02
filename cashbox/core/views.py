from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson

from smtplib import SMTP
from email.mime.text import MIMEText

import requests
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout


def index(request):
    context = {}

    if request.user.is_authenticated():
        return render(request, 'index.html', context)
    else:
        return render(request, 'home_login.html', context)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/hack/')

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

def ajax_email_ryan(request):

    msg = MIMEText("Daniel Piers paid $215 to the Ski Trip 2012 CashBox.")

    msg['Subject'] = 'You have received a payment on CashBox'
    msg['From'] = 'admin@cashbox.io'
    msg['To'] = 'ryan.marshalls@gmail.com'

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    smtp = SMTP()
    smtp.connect("cashbox.mailgun.org")
    smtp.login('admin@cashbox.mailgun.org', 'Qwasd1')
    smtp.sendmail("admin@cashbox.io", "ryan.marshalls@gmail.com", msg.as_string())
    smtp.quit()

    data = simplejson.dumps({
        'success': True,
        'msg': "Ajax - Email Ryan - Success",
        })

    return HttpResponse(data, mimetype='application/json')