#!/usr/bin/python3

import os
from fabric.api import *
from datetime import datetime


env.hosts = ['34.232.65.47', '34.202.158.94']


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
    action = local("tar -vczf {} web_static".format(filename))
    if action.succeeded:
        return (filename)
    else:
        return None


def do_deploy(archive_path):
    """Deploys an archive to the web servers"""
    name = archive_path.split("/")[1]
    if not os.path.exists(archive_path):
        return False

    action = put(archive_path, "/tmp/")
    if action.failed:
        return False

    run("mkdir -p /data/web_static/releases/{}".format(name[:-4]))

    cmd = "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(name,
                                                                    name[:-4])
    action = run(cmd)
    if action.failed:
        return False

    action = run("rm /tmp/{}".format(name))
    if action.failed:
        return False

    run("cp -rp /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(name[:-4], name[:-4]))

    run("rm -rf /data/web_static/releases/{}/web_static/".format(name[:-4]))
    action = run("rm /data/web_static/current")
    if action.failed:
        return False

    path = "/data/web_static/releases/{}".format(name[:-4])
    cmd = "ln -sf {} /data/web_static/current".format(path)
    action = run(cmd)
    if action.failed:
        return False
    return True
