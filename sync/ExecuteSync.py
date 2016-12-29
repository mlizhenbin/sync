#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess
import time


class ExecuteSync():
    def __init__(self, loadRemotefile):
        self.loadRemotefile = loadRemotefile
        pass

    def execute(self):
        fileName = self.loadRemotefile.getNewFileName()
        if len(fileName) <= 0:
            return;
        else:
            pass

        print "execute file name = ", fileName
        os.system("tar -xvf " + fileName + self.loadRemotefile.prefix)
        os.system("mv ./" + fileName + "/* .")
        os.system("rm  -rf ./bin/")
        os.system("rm  -rf " + fileName)
        os.system("rm  -rf /appData/deploy/" + self.loadRemotefile.projectFileName + "/lib/*")
        os.system("mv ./lib/*  /appData/deploy/" + self.loadRemotefile.projectFileName + "/lib/")
        os.system("rm  -rf ./lib/")

        subprocess.Popen("cd /appData/deploy/" + self.loadRemotefile.projectFileName + "/bin && pwd && ./stop.sh",
                         shell=True)
        time.sleep(15)
        subprocess.Popen("cd /appData/deploy/" + self.loadRemotefile.projectFileName + "/bin && pwd &&./start.sh",
                         shell=True)
        time.sleep(3)

        os.system("rm  -rf " + fileName + "*.jar")
