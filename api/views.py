from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# View che accetta GET (hello)
def hello_world(request):
    return JsonResponse({'message': 'Hello World!'})

# View che accetta solo POST (hello2)
@csrf_exempt  # Solo per testing! In produzione usa il CSRF token
@require_http_methods(["POST"])
@csrf_exempt
@require_http_methods(["POST"])
def hello_world_post(request):
    return JsonResponse({
        'message': 'Hello from POST!',
        'timestamp': datetime.now().isoformat()
    })