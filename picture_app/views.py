from django.http import JsonResponse
from django.shortcuts import render

from picture_app.browser.load_file import get_cities, get_all_pictures
from picture_app.browser.save_file import save_file
from picture_app.models import Picture


# Create your views here.

def page(request):
    # 城市
    cities = get_cities()

    # 照片数据
    pictures = get_all_pictures()

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
    shot_time = request.POST.get('shot-date')
    title = request.POST.get('title')

    (code, msg) = save_file(files, address, shot_time, title)

    ret = {
        "code": code,
        "msg": msg
    }
    response = JsonResponse(ret)
    return response


def city_sort(request):
    sort_mode = request.GET.get('sort')
    print(sort_mode)
    pass


def time_sort(request):
    pass
