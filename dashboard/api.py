from dashboard.serializers import *
from dashboard.utils import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth.models import User

from dashboard.models import Message


def get_logged_users(request):
    """
    api to return all logged in users
    """
    serializer = UserSerializer(get_all_logged_in_users(), many=True)
    return JSONResponse(serializer.data)


@csrf_exempt
def send_message(request):
    """
    api to send message from one user to another
    """
    try:
        sender = request.POST.get('sender')
        senderUser = User.objects.get(username=sender)

        receiver = request.POST.get('receiver')
        receiverUser = User.objects.get(username=receiver)

        content = request.POST.get('content')
        msg = Message(content=content, sender=senderUser, receiver=receiverUser)
        msg.save()
        return JSONResponse({'err': 0, 'msg_id': msg.id})
    except Exception as e:
        return JSONResponse({'err': 1, 'status': 'failed to send msg with exception: %s' % e})

@csrf_exempt
def get_user_messages(request):
    """
    api to get messages from given user
    """
    try:
        username = request.POST.get('username')
        user = User.objects.get(username=username)

        last_msg_id = request.POST.get('last_msg_id')

        msgs = Message.objects.filter(Q(sender=user) | Q(receiver=user), id__gt=last_msg_id)
        serializer = MessageSerializer(msgs, many=True)
        return JSONResponse(serializer.data)
    except Exception as e:
        print "get_user_messages exp :: %s" %e
        return JSONResponse({'err': 1, 'status': 'failed to get msgs with exception: %s' % e})
