#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


class LoadRemoteFile():
    def __init__(self, suffix, prefix, projectFileName):
        self.suffix = suffix
        self.prefix = prefix
        self.projectFileName = projectFileName

    def wgetRemoteFile(self):
        popen = os.popen("pwd")
        pwd = popen.read()
        pwdDir = pwd.rstrip("\n")
        listdir = os.listdir(pwdDir)

        projectFiles = []
        if len(listdir) > 0:
            for fileName in listdir:
                find = fileName.find(self.projectFileName)
                if find == 0:
                    projectFiles.append(fileName)
                else:
                    pass
        else:
            pass;

        version = 0
        if len(projectFiles) > 0:
            for projectFile in projectFiles:
                splits = projectFile.split("-")
                if len(splits) <= 0:
                    break
                else:
                    pass

                sfile_version = splits[-1]
                file_versions = sfile_version.split(".")
                if len(file_versions) <= 0:
                    break
                else:
                    pass

                file_version = file_versions[3]
                if self.isNumber(file_version):
                    v = int(file_version)
                    if v > version:
                        version = v
                else:
                    pass
        else:
            pass

        isSuccess = False
        if version > 0:
            version = version + 1
            wurl = "wget " + self.suffix + str(version) + self.prefix
            print "Get resource url = ", wurl
            vflag = os.system(wurl)
            if vflag == 0:
                isSuccess = True
            else:
                pass
        else:
            while (True):
                wurl = "wget " + self.suffix + str(version) + self.prefix;
                print "Get resource url = ", wurl
                wgetFlag = os.system(wurl)
                version = version + 1
                if wgetFlag == 0:
                    break
                else:
                    pass

                if version > 10:
                    print "error wget " + self.projectFileName + " more the " + str(version)
                    break

        if len(projectFiles) > 0 and isSuccess:
            print "delete all old file, %s", projectFiles
            for oldFileName in projectFiles:
                os.system("rm -rf " + oldFileName)

    def getNewFileName(self):
        popen = os.popen("pwd")
        pwd = popen.read()
        pwdDir = pwd.rstrip("\n")
        listdir = os.listdir(pwdDir)

        if len(listdir):
            for fileName in listdir:
                find = fileName.find(self.projectFileName)
                if find == 0:
                    sfileNames = fileName.split(".")
                    if len(sfileNames) <= 2:
                        return ""
                    else:
                        newFileName = ""
                        for index in range(len(sfileNames) - 2):
                            newFileName = newFileName + sfileNames[index] + "."
                        print "new file = %s", newFileName[0: len(newFileName) - 1]
                        return newFileName[0: len(newFileName) - 1]
                else:
                    pass
        else:
            pass

    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False
