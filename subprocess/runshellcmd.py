#!/usr/bin/env python
# coding=utf-8

import subprocess

def runcmd(cmd):
    print("cmd:%s" % cmd)
    p1=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p1.wait()
    out=p1.stdout.readlines()
    err=p1.stderr.readlines()
    if(p1.poll()==0):
        print(out)
    else:
        print("Failed:" ,err)
    return out,err

def saveout(out, err):
    file_log = open("log", "a")
    file_err = open("err", "a")
    print >> file_log, out
    print >> file_err, err
    file_log.close()
    file_err.close()

if __name__ == "__main__"    :
    out,err = runcmd("ls /")
    saveout(out, err)
    out,err = runcmd("ls abc")
    saveout(out, err)
    out,err = runcmd("exit 1")
    saveout(out, err)
    out,err = runcmd("java -version")
    saveout(out, err)
