#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

from config.SyncConfig import *
from sync.ExecuteSync import ExecuteSync
from sync.LoadRemoteFile import LoadRemoteFile


class SyncThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        fileName = ""
        while (True):
            print "Starting " + self.name + time.ctime(time.time())
            wget_jenkins = LoadRemoteFile(WGET_FILE_SUFFIX,
                                          WGET_FILE_PREFIX,
                                          WGET_PROJECT)
            newFile = wget_jenkins.getNewFileName()
            wget_jenkins.wgetRemoteFile()
            # if newFile != fileName:
            #     execute_sync = ExecuteSync(wget_jenkins)
            #     execute_sync.execute()
            #     fileName = newFile
            # else:
            #     pass
            # time.sleep(5)


# # 创建新线程
# thread1 = SyncThread("Thread-SYNC")
#
# # 开启线程
# thread1.start()

if __name__ == "__main__":
    wget_jenkins = LoadRemoteFile(WGET_FILE_SUFFIX,
                                  WGET_FILE_PREFIX,
                                  WGET_PROJECT)
    wget_jenkins.wgetRemoteFile()
    # execute_sync = ExecuteSync(wget_jenkins)
    # execute_sync.execute()
