from datetime import datetime
from django.utils.datastructures import MultiValueDict

from picture_app.models import Picture


def save_file(files:  MultiValueDict, address: str, shot_time: str, title: str) -> (int, str):
    i = 0
    try:
        for file in files.values():
            picture = Picture()
            if title == '':
                title = file.name.split('.')[0]
                picture.title = title
            elif len(files) > 1:
                picture.title = title + ' - ' + str(i+1)
            else:
                picture.title = title
            picture.address = address
            picture.file = file
            picture.shot_time = datetime.strptime(shot_time, "%m/%d/%Y")
            picture.save()
            i += 1
        code = 0
        msg = 'success'
    except Exception as e:
        code = 1
        msg = 'fail'
        print(e.args)

    return code, msg