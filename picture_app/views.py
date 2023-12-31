from django.http import JsonResponse
from django.shortcuts import render

from picture_app.browser.load_file import get_cities, get_all_pictures, city_choice
from picture_app.browser.save_file import save_file
from picture_app.models import Picture


# Create your views here.

def page(request):
    # 城市
    cities = get_cities()
    all_cities = city_choice()

    # 照片数据
    pictures = get_all_pictures()
    request.session['time-sort'] = 'descend'
    request.session['city-sort'] = 'all'

    code = 0
    msg = "success"
    data = {"pictures": pictures, "cities": cities, "all_cities": all_cities}
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

    ret = {
        "code": 0,
        "msg": 'success'
    }
    if sort_mode == request.session.get('time-sort'):
        response = JsonResponse(ret)
        return response

    response = JsonResponse(ret)
    return response


def time_sort(request):
    sort_mode = request.GET.get('sort')

    ret = {
        "code": '',
        "msg": ''
    }

    if sort_mode == request.session.get('city-sort'):
        response = JsonResponse(ret)
        return response

    response = JsonResponse(ret)
    return response


def delete(request):
    picture_id = request.GET.get('id')
    try:
        Picture.objects.get(id=picture_id).delete()
        code = 0
        msg = 'success'
    except Exception as e:
        print(e.args)
        code = 1
        msg = 'fail'

    ret = {
        "code": code,
        "msg": msg
    }
    response = JsonResponse(ret)
    return response