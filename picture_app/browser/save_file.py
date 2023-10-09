import os
from datetime import datetime

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.datastructures import MultiValueDict

from picture_app.models import Picture


def save_file(files:  MultiValueDict, address, shot_time) -> (int, str):
    try:
        for file in files.values():
            picture = Picture()
            picture.title = file.name.split('.')[0]
            picture.address = address
            picture.file = file
            picture.shot_time = shot_time
            picture.save()
        code = 0
        msg = 'success'
    except Exception as e:
        code = 1
        msg = 'fail'
        print(e.args)

    return code, msg