# API生成工具，通过此工具生成json文件的API

import os
import re
import datetime
import json


class direct:
    root = os.path.dirname(os.path.realpath(__file__))
    hardware = os.path.join(root, "hardware")
    cms = os.path.join(root, "cms")
    system = os.path.join(root, "system")
    common = os.path.join(root, "common")


def getType(dirpath):
    path = dirpath.replace(os.path.join(direct.root), "").lstrip('/')
    try:
        index = path.index("/")
        return path[:index]
    except ValueError:
        return path


result = []

walk_directorys = [direct.cms, direct.hardware, direct.system, direct.common]
for walk_direct in walk_directorys:
    for dirpath, dirnames, filenames in os.walk(walk_direct):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if fullpath.endswith(".py"):
                _fullpath = fullpath.replace(direct.root, "")
                typec = getType(dirpath)
                pattern = '/{}/(\w+)/'.format(typec)
                m = re.match(pattern, _fullpath)
                if m:
                    name = m.group(1)
                    # print(_fullpath)
                    timestamp = os.path.getmtime(fullpath)
                    date = datetime.datetime.fromtimestamp(timestamp)

                    _temp = {
                        "name": name,
                        "type": typec,
                        "filepath": _fullpath,
                        "time": date.strftime('%Y-%m-%d %H:%M:%S')
                    }
                    result.append(_temp)

with open("API.json", "w") as f:
    json.dump(result, f, indent=4)
