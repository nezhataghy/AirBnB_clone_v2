#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the"""
from fabric.api import sudo, env, put, local, task
from datetime import datetime


@task
def do_pack():
    """Function To Compress File Using tar"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        folder_to_save = "versions"
        local(f"mkdir -p {folder_to_save}")
        file_name_generated = f"web_static_{current_time}.tgz"
        local(f"tar -cvzf {folder_to_save}/{file_name_generated} web_static")
        return f"{folder_to_save}/{file_name_generated}"
    except Exception:
        return None


def get_ip_address(domain):
    """Function To Get IP Address"""
    import socket
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return False


env.hosts = ['34.232.65.47', '34.202.158.94']

env.user = 'ubuntu'
env.key_filename = '~/alx/aicha_key'


def do_deploy(archive_path):
    """Function To Deploy File"""
    """
    fab -f 2-do_deploy_web_static.py
    do_deploy:archive_path=versions/web_static_20231009012456.tgz
    -i ./alx -u root
    """
    import os
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")

        folder_to_save = "/data/web_static/releases"
        file_name_generated = archive_path.split(".")[0]
        file_name_generated = file_name_generated.split("/")[-1]

        server_archive_path = f"/tmp/{file_name_generated}.tgz"
        sudo(f"mkdir -p {folder_to_save}/{file_name_generated}")
        sudo(f"tar -xzf /tmp/{file_name_generated}.tgz "
             f"-C {folder_to_save}/{file_name_generated}")

        sudo(f"rm {server_archive_path}")
        sudo(f"mv {folder_to_save}/{file_name_generated}/web_static/*"
             f" {folder_to_save}/{file_name_generated}/")
        sudo(f"rm -rf {folder_to_save}/{file_name_generated}/web_static")

        try:
            sudo('rm -rf /data/web_static/current')
        except BaseException:
            pass
        sudo(f"ln -s {folder_to_save}/{file_name_generated}"
             f" /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False


@task
def deploy():
    """full deployment"""
    try:
        path = do_pack()
        if path is None:
            return False
        return do_deploy(path)
    except Exception:
        return False


@task
def install_bash_script(path):
    """install bash script"""
    import os
    env.hosts = ['34.232.65.47', '34.202.158.94']
    if not os.path.exists(path):
        return False
    try:
        for host in env.hosts:
            if not host:
                continue
            env.host_string = host
            put(path, "/tmp/")
            sudo(f"chmod +x /tmp/{path}")
            sudo(f"bash /tmp/{path}")
            print("Script Finished")
        return True
    except Exception:
        return False
