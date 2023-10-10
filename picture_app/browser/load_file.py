from picture_app.models import Picture

province_dict = {
    "安徽": "Anhui",
    "北京": "Beijing",
    "重庆": "Chongqing",
    "福建": "Fujian",
    "甘肃": "Gansu",
    "广东": "Guangdong",
    "广西": "Guangxi",
    "贵州": "Guizhou",
    "海南": "Hainan",
    "河北": "Hebei",
    "河南": "Henan",
    "黑龙江": "Heilongjiang",
    "湖北": "Hubei",
    "湖南": "Hunan",
    "江苏": "Jiangsu",
    "江西": "Jiangxi",
    "吉林": "Jilin",
    "辽宁": "Liaoning",
    "内蒙古": "Inner Mongolia",
    "宁夏": "Ningxia",
    "青海": "Qinghai",
    "山东": "Shandong",
    "山西": "Shanxi",
    "陕西": "Shaanxi",
    "上海": "Shanghai",
    "四川": "Sichuan",
    "天津": "Tianjin",
    "西藏": "Tibet",
    "新疆": "Xinjiang",
    "云南": "Yunnan",
    "浙江": "Zhejiang",
    "香港": "Hong Kong",
    "澳门": "Macau",
    "台湾": "Taiwan",
}


def get_cities() -> list:
    cities = []
    for each in province_dict.values():
        cities.append(each)
    return cities


def get_all_pictures() -> list:
    all_images = Picture.objects.all()
    pictures = []
    for each in all_images:
        file_path = each.file.path
        p = '/'+'/'.join(file_path.split('\\')[-3:])
        image = {
            "title": each.title,
            "shot_time": each.shot_time.strftime("%Y-%m-%d"),
            "address": each.address,
            "path": p
        }
        pictures.append(image)
    return pictures
