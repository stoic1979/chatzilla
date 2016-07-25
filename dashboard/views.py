from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

from dashboard.utils import *


@login_required
def home(request):
    data = {'users': get_all_logged_in_users()}
    return render_to_response('index.html', data, context_instance=RequestContext(request))


