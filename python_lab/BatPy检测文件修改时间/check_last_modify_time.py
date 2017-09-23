import codecs
import os
import os.path
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


# 检测根目录
check_root_dir = os.getcwd() + '\ExampleFolder'
# 忽略目录
ignore_dir = check_root_dir + '\IgnoreFolder'
# 记录文件存储目录
save_file_root = os.getcwd() + '\TempPy'

# 如果 记录文件存储目录 不存在 则 创建
if not os.path.exists(save_file_root):
    os.mkdir(save_file_root)

# 最后修改时间 文件
save_file_modify_time = save_file_root + '\modify_time.txt'
# 修改标志 文件
save_file_signal = save_file_root + '\signal.txt'
# 详细修改检测信息 文件
save_file_detail = save_file_root + '\detail.txt'

# 获取 记录中的 最后修改时间
record_modify_time = "0"
if os.path.exists(save_file_modify_time):
    file_object = codecs.open(save_file_modify_time, 'rb')
    record_modify_time = file_object.read().decode('utf-8')
    file_object.close()

#print(len(sys.argv))
# if len(sys.argv) > 1:
#     check_root_dir = sys.argv[1]
#     record_modify_time = sys.argv[2]

# 开始检测
latest_modify_time = 0
latest_modify_file = ""

# 1.获取 检测目录 的 修改时间
modify_time = GetModifyTime(check_root_dir)
if modify_time > latest_modify_time:
    latest_modify_time = modify_time
    latest_modify_file = check_root_dir

for parent, dirnames, filenames in os.walk(check_root_dir):
    # 跳过 ignore_dir
    if parent == ignore_dir:
        continue
    # 2.获取 子目录 的 修改时间
    for dirname in dirnames:
        dir_full_path = os.path.join(parent, dirname)
        modify_time = GetModifyTime(dir_full_path)
        # 跳过 ignore_dir
        if dir_full_path == ignore_dir:
            continue
        if modify_time > latest_modify_time:
            latest_modify_time = modify_time
            latest_modify_file = dir_full_path
    # 3.获取 子文件 的 修改时间
    for filename in filenames:
        file_full_path = os.path.join(parent, filename)
        modify_time = GetModifyTime(file_full_path)
        if modify_time > latest_modify_time:
            latest_modify_time = modify_time
            latest_modify_file = file_full_path

# 最后修改文件的详细信息
result_detail = ""
result_detail += "latest_modify_file : " + latest_modify_file + "\r\n"
result_detail += "latest_modify_time : " + (str)(latest_modify_time) + "\r\n"
result_detail += "latest_modify_time_pretty :" + (
    str)(time.localtime(latest_modify_time)) + "\r\n"

# 比较 latest_modify_time 和 record_modify_time 获取 修改标志
result_signal = ""
if (str)(latest_modify_time) == record_modify_time:
    result_signal = "nomodify"
else:
    result_signal = "modify"
print(result_signal)

# 将信息保存至文件
SaveStringToFile(save_file_modify_time, (str)(latest_modify_time))
SaveStringToFile(save_file_detail, result_detail)
SaveStringToFile(save_file_signal, result_signal)
