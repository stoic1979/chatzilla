from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


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
