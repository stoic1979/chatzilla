from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext

from dashboard.forms import LoginForm

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@login_required
def home(request):
    data = {}
    return HttpResponse("Ticketzilla")


################################################
#                                              #
#               LOGIN/LOGOUT                   #
#                                              #
################################################
def login_page(request):
    message = error = None
    username = password = ''
    form = LoginForm()

    # default next page is index page
    next_page = "/"

    # getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        # a form bound to the post data
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"

                # redirect after post
                return HttpResponseRedirect(next_page)
            else:
                message = "Your account is not active, please contact the site admin."
                error = 1
        else:
            message = "Your username and/or password were incorrect."
            error = 1

    c = {'username': username, 'form': form, 'next': next_page}
    if message:
        c.update({"message": message})
    if error:
        c.update({"error": error})
    c.update(csrf(request))

    return render_to_response('login.html', c)


def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request': request})
