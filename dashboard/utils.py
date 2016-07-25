from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.renderers import JSONRenderer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def get_all_logged_in_users():
    # query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)
