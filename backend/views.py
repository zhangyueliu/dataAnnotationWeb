from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

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

def getAllData(request):
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
