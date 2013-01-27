"application views"

# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_odesk.core.clients import RequestClient


@login_required
def index(request):
    cli = RequestClient(request)
    token, user_details = cli.auth.check_token()
    # import ipdb; ipdb.set_trace()
    # return HttpResponse('OK')
    return render(request, 'index.html', user_details)
