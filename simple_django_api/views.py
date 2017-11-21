from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# api_view is DRF’s built in decorator - it specifies which HTTP methods the view can respond to and wraps normal HTTP request/response objects to provide a more uniform interface to work with HTTP data
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
       'users': reverse('users:user-list', request=request, format=format),
       'todos': reverse('todos:todo-list', request=request, format=format),
})
