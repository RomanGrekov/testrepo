#!/usr/bin/python3

import subprocess
import re
import sys
import os

class Metrics():
    def __init__(self):
        pass

    def get_cpu(self):
        stdout = subprocess.check_output(["cat", "/proc/cpuinfo"])
        res = re.findall(r".*cpu\s+MHz\s+:\s+([0-9]+)\.+.+", stdout.decode("utf-8"))
        return res
    
    def get_mem(self):
        stdout = subprocess.check_output(["free", "-m"])
        res = re.findall(r".*Mem:\s+([0-9]+)\s+.*", stdout.decode("utf-8"))
        return res[0]


def test_echo():
    return "test echo"


if __name__ == "__main__":
    metrics = Metrics()
    cpu_mhz = metrics.get_cpu()
    print(cpu_mhz)
    mem_free = metrics.get_mem()
    print(mem_free)
