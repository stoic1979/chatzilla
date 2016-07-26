from dashboard.serializers import *
from dashboard.utils import *
from django.views.decorators.csrf import csrf_exempt

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
        return JSONResponse({'err': 0, msg_id: msg.id})
    except:
        return JSONResponse({'err': 1, 'status': 'failed to send msg'})
