from dashboard.serializers import *
from dashboard.utils import *


def get_users(request):
    """
    api to return all logged in users
    """
    serializer = UserSerializer(get_all_logged_in_users(), context={'request': request}, many=True)
    return JSONResponse(serializer.data)
