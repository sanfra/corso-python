from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['GET'])
def hello_world(request):
    """Endpoint GET /api/hello/"""
    data = {
        'message': 'Hello from PWW API!',
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def hello_post(request):
    """Endpoint POST /api/helloPost/"""
    data = {
        'message': 'Hello from POST!',
        'timestamp': datetime.now().isoformat(),
        'method': request.method,
        'path': request.path,
    }
    return Response(data, status=status.HTTP_200_OK)
