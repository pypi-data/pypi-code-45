import contextlib
import datetime
import beeline
from beeline.trace import unmarshal_trace_context
from django.db import connections

def _get_trace_context(request):
    trace_context = request.META.get('HTTP_X_HONEYCOMB_TRACE')
    beeline.internal.log("got trace context: %s", trace_context)
    if trace_context:
        try:
            return unmarshal_trace_context(trace_context)
        except Exception as e:
            beeline.internal.log('error attempting to extract trace context: %s', beeline.internal.stringify_exception(e))

    return None, None, None

class HoneyDBWrapper(object):

    def __call__(self, execute, sql, params, many, context):
        vendor = context['connection'].vendor
        trace_name = "django_%s_query" % vendor

        with beeline.tracer(trace_name):
            beeline.add_context({
                "type": "db",
                "db.query": sql,
                "db.query_args": params,
            })

            try:
                db_call_start = datetime.datetime.now()
                result = execute(sql, params, many, context)
                db_call_diff = datetime.datetime.now() - db_call_start
                beeline.add_context_field(
                    "db.duration", db_call_diff.total_seconds() * 1000)
            except Exception as e:
                beeline.add_context_field("db.error", str(type(e)))
                beeline.add_context_field("db.error_detail", beeline.internal.stringify_exception(e))
                raise
            else:
                return result
            finally:
                if vendor in ('postgresql', 'mysql'):
                    beeline.add_context({
                        "db.last_insert_id": context['cursor'].cursor.lastrowid,
                        "db.rows_affected": context['cursor'].cursor.rowcount,
                    })


class HoneyMiddlewareBase(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.create_http_event(request)
        return response

    def get_context_from_request(self, request):
        trace_name = "django_http_%s" % request.method.lower()
        return {
            "name": trace_name,
            "type": "http_server",
            "request.host": request.get_host(),
            "request.method": request.method,
            "request.path": request.path,
            "request.remote_addr": request.META.get('REMOTE_ADDR'),
            "request.content_length": request.META.get('CONTENT_LENGTH', 0),
            "request.user_agent": request.META.get('HTTP_USER_AGENT'),
            "request.scheme": request.scheme,
            "request.secure": request.is_secure(),
            "request.query": request.GET.dict(),
            "request.xhr": request.is_ajax(),
        }

    def get_context_from_response(self, request, response):
        return {
            "response.status_code": response.status_code,
        }

    def create_http_event(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        trace_id, parent_id, parent_context = _get_trace_context(request)

        request_context = self.get_context_from_request(request)

        trace = beeline.start_trace(context=request_context, trace_id=trace_id, parent_span_id=parent_id)

        if isinstance(parent_context, dict):
            for k, v in parent_context.items():
                beeline.add_trace_field(k, v)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        response_context = self.get_context_from_response(request, response)
        beeline.add_context(response_context)
        beeline.finish_trace(trace)

        return response

    def process_exception(self, request, exception):
        beeline.add_context_field("request.error_detail", beeline.internal.stringify_exception(exception))

    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            beeline.add_context_field("django.view_func", view_func.__name__)
        except AttributeError:
            pass

class HoneyMiddlewareHttp(HoneyMiddlewareBase):
    pass


class HoneyMiddleware(HoneyMiddlewareBase):
    def __call__(self, request):
        try:
            db_wrapper = HoneyDBWrapper()
            # db instrumentation is only present in Django > 2.0
            with contextlib.ExitStack() as stack:
                for connection in connections.all():
                    stack.enter_context(connection.execute_wrapper(db_wrapper))
                response = self.create_http_event(request)
        except AttributeError:
            response = self.create_http_event(request)

        return response

class HoneyMiddlewareWithPOST(HoneyMiddleware):
    ''' HoneyMiddlewareWithPOST is a subclass of HoneyMiddleware. The only difference is that
    the `request.post` field is instrumented. This was removed from the base implementation in 2.8.0
    due to conflicts with other middleware. See https://github.com/honeycombio/beeline-python/issues/74.'''
    def get_context_from_request(self, request):
        trace_name = "django_http_%s" % request.method.lower()
        return {
            "name": trace_name,
            "type": "http_server",
            "request.host": request.get_host(),
            "request.method": request.method,
            "request.path": request.path,
            "request.remote_addr": request.META.get('REMOTE_ADDR'),
            "request.content_length": request.META.get('CONTENT_LENGTH', 0),
            "request.user_agent": request.META.get('HTTP_USER_AGENT'),
            "request.scheme": request.scheme,
            "request.secure": request.is_secure(),
            "request.query": request.GET.dict(),
            "request.xhr": request.is_ajax(),
            "request.post": request.POST.dict(),
        }
