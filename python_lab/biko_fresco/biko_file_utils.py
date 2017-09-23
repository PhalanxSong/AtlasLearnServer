import os
import os.path
import codecs
import sys
import random


# 获取脚本路径
def GetScriptPath():
    script_full_path = os.path.split(os.path.realpath(sys.argv[0]))
    script_dir = script_full_path[0]
    return script_dir


def GetFilePathFromRootdirListWithExt(rootdirs, fileExt):
    #print("---------- Get File Path From Rootdir List With Ext ----------")

    fileNamePathList = []

    for rootdir in rootdirs:
        for parent, dirnames, filenames in os.walk(rootdir):
            #case 1:
            #for dirname in dirnames:
            #    print("parent folder is:" + parent)
            #    print("dirname is:" + dirname)
            #case 2
            for filename in filenames:
                if filename.endswith(fileExt):
                    fileNamePath = [
                        filename[0:-len(fileExt)],
                        os.path.join(parent, filename)
                    ]
                    fileNamePathList.append(fileNamePath)
    return fileNamePathList


def RemoveFileWithExt(fileNamePathList, fileExt):
    result = []
    for i in fileNamePathList:
        if not i[1].endswith(fileExt):
            result.append(i)
    return result


def RemoveFileWithPathStart(fileNamePathList, filePathStart):
    result = []
    for i in fileNamePathList:
        if not i[1].startswith(filePathStart):
            result.append(i)
    return result


def RemoveFileWithPathContain(fileNamePathList, containStr):
    result = []
    for i in fileNamePathList:
        if not containStr in i[1]:
            result.append(i)
    return result
