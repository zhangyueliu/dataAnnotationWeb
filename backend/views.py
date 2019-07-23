from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token


def index(request):
    data = [
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },
    ]

    return JsonResponse(data, safe=False)


def get_all_data(request):
    data = [
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },
        {
            "date": '2016-05-02',
            "name": '王小虎',
            "sex": '男'
        },

    ]

    return JsonResponse(data, safe=False)


@ensure_csrf_cookie
def add_data(request):
    get_token(request)
    if request.method != "POST":
        return HttpResponse()
    print('aaa')
    success = True

    return HttpResponse(success, safe=False)


