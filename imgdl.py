import os
import re
import winsound

import requests
from retry import retry

path = ''  # 父文件夹


def getImg(url, title):
    os.chdir(path)
    isExists = os.path.exists(validateTitle(title) + ".jpg")
    url = str.replace(url, "product-other", "detail")
    imgurl = "https://www.suruga-ya.jp/database/pics_light/game/" + \
             re.findall(re.compile(r'detail/[A-Za-z0-9]+'), url)[0].split("/")[1].lower() + ".jpg"
    while not isExists:
        global img

        @retry(tries=1000, delay=4)
        def getImg0():
            global img
            img = requests.get(imgurl, timeout=4)

        getImg0()

        if img.status_code == 200:
            open(validateTitle(title) + ".jpg", 'wb').write(img.content)
            print("下载成功！")
        else:
            img = requests.get("https://www.suruga-ya.jp/database/images/no_photo.jpg", timeout=4)
            open(validateTitle(title) + ".jpg", 'wb').write(img.content)
            print("下载成功！")
            break
        isExists = os.path.exists(validateTitle(title) + ".jpg")
    duration = 1000
    freq = 440
    winsound.Beep(freq, duration)


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title
