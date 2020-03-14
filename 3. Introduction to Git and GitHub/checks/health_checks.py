#!/usr/bin/python3
import shutil
import psutil


def check_disk_usage(disk):
    """Returns True if there is enough free disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR!')
else:
    print('Everything is OK!')
