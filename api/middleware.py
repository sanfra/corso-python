import logging

logger = logging.getLogger(__name__)

class RequestLoggerMiddleware:
    """
    Middleware che logga ogni request in arrivo
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Logga la request prima di processarla
        logger.info(f"REQUEST: {request.method} {request.path}")
        
        # Processa la request
        response = self.get_response(request)
        
        # Logga la response
        logger.info(f"RESPONSE: {response.status_code} for {request.path}")
        
        return response
