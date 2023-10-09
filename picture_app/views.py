from django.http import JsonResponse
from django.shortcuts import render

from picture_app.browser.save_file import save_file
from picture_app.models import Picture


# Create your views here.

def page(request):
    # 城市
    cities = []

    # 照片数据
    pictures = []

    code = 0
    msg = "success"
    data = {"pictures": pictures, "cities": cities}
    ret = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return render(request, template_name="index.html", context=ret)


def test(request):
    return render(request, template_name='test.html')


def upload(request):
    files = request.FILES
    address = request.POST.get('location')
    shot_time = request.POST.get('time')

    (code, msg) = save_file(files, address, shot_time)

    ret = {
        "code": code,
        "msg": msg
    }
    response = JsonResponse(ret)
    return response