#!/usr/bin/python3
"""Creating an archive with the file in web_static folder"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compresses File"""
    current = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(current.year,
                                                             current.month,
                                                             current.day,
                                                             current.hour,
                                                             current.minute,
                                                             current.second)
    print("Packing web_static to versions/{}".format(filename))
    local("mkdir -p versions")
    compress = local("tar -vczf {} web_static".format(filename))
    if compress.succeeded:
        return (filename)
    else:
        return None
