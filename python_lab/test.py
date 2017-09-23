import codecs
import os
import os.path
import shutil
import sys
import time


# 获取文件修改时间
def GetModifyTime(full_path):
    return os.stat(full_path).st_mtime


# save string to file
def SaveStringToFile(full_path, save_string):
    file_object = codecs.open(full_path, 'w', encoding='utf-8')
    file_object.write(save_string)
    file_object.close()


prj_root_dir = os.getcwd()
save_file_path = prj_root_dir + '/biubiubiu.txt'
save_str = r'hahahahasdad...'

SaveStringToFile(save_file_path, save_str)
