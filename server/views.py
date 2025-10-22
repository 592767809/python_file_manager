
import os
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound, FileResponse, HttpResponseForbidden
from apikey.models import ApiKey


def file_manager(http_request: HttpRequest):
    key = http_request.headers.get('Key')
    if not key:
        return HttpResponseForbidden()
    if not ApiKey.objects.filter(key_value=key):
        return HttpResponseForbidden()
    file_path = http_request.get_full_path()[6:]
    if '..' in file_path:
        return HttpResponseNotFound()
    file_path = '/srv/' + file_path
    if http_request.method == "GET":
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        else:
            return HttpResponseNotFound()
    elif http_request.method == "POST":
        base_path = os.path.dirname(file_path)
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        with open(file_path, 'wb') as f:
            f.write(http_request.body)
        return HttpResponse('ok'.encode())
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
