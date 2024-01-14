#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives """
# from fabric.api import *
from fabric.api import env, run, local


env.hosts = ['34.232.65.47', '34.202.158.94']
env.user = "ubuntu"


def do_clean(number=0):
    """ comment """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
