import codecs
import os
import os.path
import shutil
import stat
import sys
import time

path = r'C:\Users\PC\Desktop\PythonLab\chmod\chmod_test'

# remove read only
for parent, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        dir_full_path = os.path.join(parent, dirname)
        os.chmod(dir_full_path, stat.S_IWRITE)
    for filename in filenames:
        file_full_path = os.path.join(parent, filename)
        os.chmod(file_full_path, stat.S_IWRITE)

# if os.path.exists(path):
#     shutil.rmtree(path)

# if not os.path.exists(path):
#     os.mkdir(path)
