
import os
import json
from apikey.models import ApiKey
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, FileResponse, HttpResponseForbidden, HttpResponseBadRequest


def file_manager(http_request: HttpRequest):
    key = http_request.headers.get('Key')
    if not key:
        return HttpResponseForbidden()
    if not ApiKey.objects.filter(key_value=key):
        return HttpResponseForbidden()
    try:
        request_body = json.loads(http_request.body.decode())
    except:
        return HttpResponseBadRequest()
    action = request_body.get('action')
    file_path = request_body.get('file_path')
    file_data = request_body.get('file_data')
    if not action or not file_path:
        return HttpResponseBadRequest()
    file_path = '/srv/' + file_path
    base_path = os.path.dirname(file_path)
    if action == "GET":
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        else:
            return HttpResponseNotFound()
    elif action == "POST":
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        with open(file_path, 'wb') as f:
            f.write(file_data)
        return HttpResponse('ok'.encode())
    else:
        return HttpResponseBadRequest()
