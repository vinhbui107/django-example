import logging
import time

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        run_time = round((time.time() - start_time) * 1000, 2)  # ms

        method = str(getattr(request, "method", "")).upper()
        status_code = str(getattr(response, "status_code", ""))
        request_path = str(getattr(request, "path", ""))

        log_data = {
            "remote_address": request.META["REMOTE_ADDR"],
            "method": method,
            "path": request_path,
            "response_time": str(run_time) + " ms",
            "status_code": status_code,
        }
        logger.info(log_data)

        return response
