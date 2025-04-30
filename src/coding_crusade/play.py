from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException

url_map = Map([Rule("/", endpoint="home")])


def request_dispatcher(request):
    urls = url_map.bind_to_environ(request.environ)
    try:
        endpoint, args = urls.match()
        # WIP : Dispatch logic to return the correct Response
    except HTTPException as e:
        return e


def application(environ, start_response):
    request = Request(environ)
    response = request_dispatcher(request)
    return response(environ, start_response)


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    run_simple("localhost, 5000, application, use_debugger=True, use_reloader=True")
