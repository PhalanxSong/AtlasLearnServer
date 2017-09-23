import codecs
import os
import os.path
import random
import sys


# 获取脚本路径
def GetScriptPath():
    script_full_path = os.path.split(os.path.realpath(sys.argv[0]))
    script_dir = script_full_path[0]
    return script_dir


rootdir = os.path.join(GetScriptPath(), "Example")
copydir = os.path.join(GetScriptPath(), "Replaced")
#print(rootdir)
#print(copydir)

if not os._exists(copydir):
    os.mkdir(copydir)

replace_dir_list = []
replace_file_list = []

target = "GameBeginStage"
replace = "WaitForPlayerStage"

for parent, dirnames, filenames in os.walk(rootdir):
    #case 1:
    for dirname in dirnames:
        replace_dir_list.append(os.path.join(parent, dirname))
    #case 2
    for filename in filenames:
        if filename.endswith(".txt"):
            replace_file_list.append(os.path.join(parent, filename))
        if filename.endswith(".cpp"):
            replace_file_list.append(os.path.join(parent, filename))
        if filename.endswith(".h"):
            replace_file_list.append(os.path.join(parent, filename))
        if filename.endswith(".hpp"):
            replace_file_list.append(os.path.join(parent, filename))

# Replace 全部目录
for i in replace_dir_list:
    #print(i)
    modifyed_dir = i.replace(rootdir, copydir)
    modifyed_dir = modifyed_dir.replace(target, replace)
    os.mkdir(modifyed_dir)

# Replace 全部文件
for i in replace_file_list:
    file_object = codecs.open(i, 'rb')
    file_text = file_object.read().decode('utf-8')
    file_object.close()
    modify_file_text = file_text.replace(target, replace)
    modify_file_full_path = i.replace(rootdir, copydir)
    modify_file_full_path = modify_file_full_path.replace(target, replace)
    file_object = codecs.open(modify_file_full_path, 'w', encoding='utf-8')
    file_object.write(modify_file_text)
    file_object.close()

pasue = input("Enter anything to end...")
