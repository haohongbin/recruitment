import time
import logging

logger = logging.getLogger(__name__)

# 中间件用函数实现
def performance_logger_middleware(get_response):
    def middleware(request):
        """
        记录用户访问的url,用户传递的参数，以及耗费的时间
        :param request:
        :return:
        """
        start_time = time.time()
        response = get_response(request)
        duration = time.time() - start_time
        response["X-Page-Duration-ms"] = int(duration * 1000) # 耗时通过response的头返回出去
        logger.info("%s %s %s", duration, request.path, request.GET.dict() )
        return response

    return middleware


class PerformanceAndExceptionLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        response["X-Page-Duration-ms"] = int(duration * 1000)
        logger.info("duration:%s url:%s parameters:%s", duration, request.path, request.GET.dict())

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        if exception:
            message = "url:{url} ** msg:{error} ````{tb}````".format(
                url=request.build_absolute_uri(),
                error=repr(exception),
                tb=traceback.format_exc()
            )

            logger.warning(message)

            # send dingtalk message
            dingtalk.send(message)

            # capture exception to sentry:
            capture_exception(exception)

        return HttpResponse("Error processing the request, please contact the system administrator.", status=500)