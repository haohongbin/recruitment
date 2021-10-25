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

