#!/usr/bin/env python
# coding=utf-8

import subprocess

def runcmd(cmd):
    print("cmd:%s" % cmd)
    p1=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.wait()
    if(p1.poll()==0):
        out=p1.stdout.readlines()
        print(out)
    else:
        err=p1.stderr.readlines()
        print("Failed:" ,err)

if __name__ == "__main__"    :
    runcmd("ls /")
    runcmd("ls abc")
    runcmd("exit 1")
    runcmd("java -version")
