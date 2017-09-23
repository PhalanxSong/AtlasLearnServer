# encoding: UTF-8

import codecs
import os
import os.path
import sys
import time
import json


# 获取脚本路径
def GetScriptPath():
    script_full_path = os.path.split(os.path.realpath(sys.argv[0]))
    script_dir = script_full_path[0]
    return script_dir


# save string to file
def SaveStringToFile(full_path, save_string):
    file_object = codecs.open(full_path, 'w', encoding='utf-8')
    file_object.write(save_string)
    file_object.close()


# 获取 log 文件路径
def GetLogFilePath(index):
    log_root_path = GetScriptPath() + '/deepoon_log'
    return log_root_path + '/' + (str)(index) + '/log'


# 计算两个形如 XX:XX:XX 的时间的间隔时间
def GetDuration(time1, time2):
    splited_time_1 = time1.split(':')
    if not len(splited_time_1) == 3:
        return -1
    time_1_sec = (int)(splited_time_1[0]) * 3600 + (
        int)(splited_time_1[1]) * 60 + (int)(splited_time_1[2])

    splited_time_2 = time2.split(':')
    if not len(splited_time_2) == 3:
        return -1
    time_2_sec = (int)(splited_time_2[0]) * 3600 + (
        int)(splited_time_2[1]) * 60 + (int)(splited_time_2[2])

    return abs(time_2_sec - time_1_sec)


def GetBuildPerson(analyzer, line):
    if not analyzer.build_person == 'nan':
        return
    feature = 'Started by user'
    if line.find(feature) > 0:
        splited = line.split(feature)
        if len(splited) > 1:
            analyzer.build_person = splited[1].strip()


def GetAnchorModulesStart(analyzer, line):
    if not analyzer.anchor_modules_start == 'nan':
        return
    feature = 'Begin anchor'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.anchor_modules_start = splited[0].strip()


def GetAnchorModulesEnd(analyzer, line):
    if not analyzer.anchor_modules_end == 'nan':
        return
    feature = 'End anchor'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.anchor_modules_end = splited[0].strip()
        analyzer.progress_start = splited[0].strip()


def GetCompileJsStart(analyzer, line):
    if not analyzer.compile_js_start == 'nan':
        return
    feature = '+ sh Scripts/compile_js'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.compile_js_start = splited[0].strip()


def GetCompileJsEnd(analyzer, line):
    if not analyzer.compile_js_end == 'nan':
        return
    feature = 'Finish Compile HTML-Menu'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.compile_js_end = splited[0].strip()


def GetCookParm(analyzer, line):
    if not analyzer.cook_parm == 'nan':
        return
    feature = 'cook_parm:'
    if line.find(feature) > 0:
        splited = line.split(feature)
        if len(splited) > 1:
            analyzer.cook_parm = splited[1].strip()


def GetBuildCmdStart(analyzer, line):
    if not analyzer.build_cmd_start == 'nan':
        return
    feature = 'Project.Build: ********** BUILD COMMAND STARTED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.build_cmd_start = splited[0].strip()


def GetBuildCmdEnd(analyzer, line):
    if not analyzer.build_cmd_end == 'nan':
        return
    feature = 'Project.Build: ********** BUILD COMMAND COMPLETED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.build_cmd_end = splited[0].strip()


def GetCookCmdStart(analyzer, line):
    if not analyzer.cook_cmd_start == 'nan':
        return
    feature = 'Project.Cook: ********** COOK COMMAND STARTED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.cook_cmd_start = splited[0].strip()


def GetCookCmdEnd(analyzer, line):
    if not analyzer.cook_cmd_end == 'nan':
        return
    feature = 'Project.Cook: ********** COOK COMMAND COMPLETED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.cook_cmd_end = splited[0].strip()


def GetStageCmdStart(analyzer, line):
    if not analyzer.stage_cmd_start == 'nan':
        return
    feature = 'Project.CopyBuildToStagingDirectory: ********** STAGE COMMAND STARTED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.stage_cmd_start = splited[0].strip()


def GetStageCmdEnd(analyzer, line):
    if not analyzer.stage_cmd_end == 'nan':
        return
    feature = 'Project.CopyBuildToStagingDirectory: ********** STAGE COMMAND COMPLETED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.stage_cmd_end = splited[0].strip()


def GetFinalCopyStart(analyzer, line):
    if not analyzer.final_copy_start == 'nan':
        return
    feature = ' Project.Archive: ********** ARCHIVE COMMAND COMPLETED'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.final_copy_start = splited[0].strip()


def GetFinalCopyEnd(analyzer, line):
    if not analyzer.final_copy_end == 'nan':
        return
    feature = ' E:\\xBrowserDpn>EXIT'
    if line.find(feature) > 0:
        splited = line.split(feature)
        analyzer.final_copy_end = splited[0].strip()


def GetBuildResult(analyzer, line):
    if not analyzer.build_result == 'nan':
        return
    feature = ' Finished: '
    if line.find(feature) > 0:
        splited = line.split(feature)
        if len(splited) > 1:
            analyzer.build_result = splited[1].strip()


class LogAnalyzer:
    def __init__(self):
        self.build_id = '0'
        self.build_person = 'nan'
        self.anchor_modules_start = 'nan'
        self.anchor_modules_end = 'nan'
        self.anchor_modules_time = 'nan'
        self.compile_js_start = 'nan'
        self.compile_js_end = 'nan'
        self.compile_js_time = 'nan'
        self.cook_parm = 'nan'
        self.progress_start = 'nan'
        self.progress_end = 'nan'
        self.progress_time = 'nan'
        self.build_cmd_start = 'nan'
        self.build_cmd_end = 'nan'
        self.build_cmd_time = 'nan'
        self.cook_cmd_start = 'nan'
        self.cook_cmd_end = 'nan'
        self.cook_cmd_time = 'nan'
        self.stage_cmd_start = 'nan'
        self.stage_cmd_end = 'nan'
        self.stage_cmd_time = 'nan'
        self.final_copy_start = 'nan'
        self.final_copy_end = 'nan'
        self.final_copy_time = 'nan'
        self.build_result = 'nan'
        self.build_full_time = 'nan'

    def GetTimeDuration(self):
        self.anchor_modules_time = (str)(
            GetDuration(self.anchor_modules_start, self.anchor_modules_end))
        self.compile_js_time = (
            str)(GetDuration(self.compile_js_start, self.compile_js_end))
        self.progress_time = (
            str)(GetDuration(self.progress_start, self.progress_end))
        self.build_cmd_time = (
            str)(GetDuration(self.build_cmd_start, self.build_cmd_end))
        self.cook_cmd_time = (
            str)(GetDuration(self.cook_cmd_start, self.cook_cmd_end))
        self.stage_cmd_time = (
            str)(GetDuration(self.stage_cmd_start, self.stage_cmd_end))
        self.final_copy_time = (
            str)(GetDuration(self.final_copy_start, self.final_copy_end))

    def GetFullTime(self):
        self.build_full_time = (
            str)(GetDuration(self.anchor_modules_start, self.final_copy_end))

    def GetCsvTitleSimple():
        rst = ''
        rst += 'build_id,'
        rst += 'build_person,'
        rst += 'build_result,'
        rst += 'anchor_modules_time,'
        rst += 'compile_js_time,'
        rst += 'progress_time,'
        rst += 'build_cmd_time,'
        rst += 'cook_parm,'
        rst += 'cook_cmd_time,'
        rst += 'stage_cmd_time,'
        rst += 'final_copy_time,'
        rst += 'build_full_time,'
        return rst

    def GetCsvTitleSimpleCh():
        rst = ''
        rst += 'ID,'
        rst += '构建人,'
        rst += '构建结果,'
        rst += '拉取代码,'
        rst += 'Js 编译,'
        rst += 'Editor 编译,'
        rst += 'Package 编译,'
        rst += 'Cook 参数检测,'
        rst += 'Cook 资源烘焙时间,'
        rst += 'Stage 命令时间,'
        rst += 'Copy 复制工程时间,'
        rst += 'Build 总时间,'
        return rst

    def GetCsvInfoSimple(self):
        rst = ''
        rst += (str)(self.build_id) + ','
        rst += (str)(self.build_person) + ','
        rst += (str)(self.build_result) + ','
        rst += (str)(self.anchor_modules_time) + ','
        rst += (str)(self.compile_js_time) + ','
        rst += (str)(self.progress_time) + ','
        rst += (str)(self.build_cmd_time) + ','
        rst += (str)(self.cook_parm) + ','
        rst += (str)(self.cook_cmd_time) + ','
        rst += (str)(self.stage_cmd_time) + ','
        rst += (str)(self.final_copy_time) + ','
        rst += (str)(self.build_full_time) + ','
        return rst

    def GetCsvTitleFull():
        rst = ''
        rst += 'build_id,'
        rst += 'build_person,'
        rst += 'anchor_modules_start,'
        rst += 'anchor_modules_end,'
        rst += 'anchor_modules_time,'
        rst += 'compile_js_start,'
        rst += 'compile_js_end,'
        rst += 'compile_js_time,'
        rst += 'cook_parm,'
        rst += 'progress_start,'
        rst += 'progress_end,'
        rst += 'progress_time,'
        rst += 'build_cmd_start,'
        rst += 'build_cmd_end,'
        rst += 'build_cmd_time,'
        rst += 'cook_cmd_start,'
        rst += 'cook_cmd_end,'
        rst += 'cook_cmd_time,'
        rst += 'stage_cmd_start,'
        rst += 'stage_cmd_end,'
        rst += 'stage_cmd_time,'
        rst += 'final_copy_start,'
        rst += 'final_copy_end,'
        rst += 'final_copy_time,'
        rst += 'build_result,'
        rst += 'build_full_time,'
        return rst

    def GetCsvInfoFull(self):
        rst = ''
        rst += (str)(self.build_id) + ','
        rst += (str)(self.build_person) + ','
        rst += (str)(self.anchor_modules_start) + ','
        rst += (str)(self.anchor_modules_end) + ','
        rst += (str)(self.anchor_modules_time) + ','
        rst += (str)(self.compile_js_start) + ','
        rst += (str)(self.compile_js_end) + ','
        rst += (str)(self.compile_js_time) + ','
        rst += (str)(self.cook_parm) + ','
        rst += (str)(self.progress_start) + ','
        rst += (str)(self.progress_end) + ','
        rst += (str)(self.progress_time) + ','
        rst += (str)(self.build_cmd_start) + ','
        rst += (str)(self.build_cmd_end) + ','
        rst += (str)(self.build_cmd_time) + ','
        rst += (str)(self.cook_cmd_start) + ','
        rst += (str)(self.cook_cmd_end) + ','
        rst += (str)(self.cook_cmd_time) + ','
        rst += (str)(self.stage_cmd_start) + ','
        rst += (str)(self.stage_cmd_end) + ','
        rst += (str)(self.stage_cmd_time) + ','
        rst += (str)(self.final_copy_start) + ','
        rst += (str)(self.final_copy_end) + ','
        rst += (str)(self.final_copy_time) + ','
        rst += (str)(self.build_result) + ','
        rst += (str)(self.build_full_time) + ','
        return rst

    def PrintLogAnalyzerInfo1(self):
        print('************** build analyzer 1 start **************')
        print('build_id               :   ' + self.build_id)
        print('build_person           :   ' + self.build_person)
        print('anchor_modules_start   :   ' + self.anchor_modules_start)
        print('anchor_modules_end     :   ' + self.anchor_modules_end)
        print('compile_js_start       :   ' + self.compile_js_start)
        print('compile_js_end         :   ' + self.compile_js_end)
        print('cook_parm              :   ' + self.cook_parm)
        print('progress_start         :   ' + self.progress_start)
        print('progress_end           :   ' + self.progress_end)
        print('build_cmd_start        :   ' + self.build_cmd_start)
        print('build_cmd_end          :   ' + self.build_cmd_end)
        print('cook_cmd_start         :   ' + self.cook_cmd_start)
        print('cook_cmd_end           :   ' + self.cook_cmd_end)
        print('stage_cmd_start        :   ' + self.stage_cmd_start)
        print('stage_cmd_end          :   ' + self.stage_cmd_end)
        print('final_copy_start       :   ' + self.final_copy_start)
        print('final_copy_end         :   ' + self.final_copy_end)
        print('build_result           :   ' + self.build_result)
        print('************** build analyzer 1 end **************')
        print('')

    def PrintLogAnalyzerInfo2(self):
        print('************** build analyzer 2 start **************')
        print('build_id               :   ' + self.build_id)
        print('build_person           :   ' + self.build_person)
        print('cook_parm              :   ' + self.cook_parm)
        print('anchor_modules_time    :   ' + self.anchor_modules_time)
        print('compile_js_time        :   ' + self.compile_js_time)
        print('progress_time          :   ' + self.progress_time)
        print('build_cmd_time         :   ' + self.build_cmd_time)
        print('cook_cmd_time          :   ' + self.cook_cmd_time)
        print('stage_cmd_time         :   ' + self.stage_cmd_time)
        print('final_copy_time        :   ' + self.final_copy_time)
        print('build_result           :   ' + self.build_result)
        print('************** build analyzer 2 end **************')
        print('')


check_log_index_array = range(1, 1300)
available_log_index_array = []

result = ''
result += LogAnalyzer.GetCsvTitleSimple() + '\r\n'
result += LogAnalyzer.GetCsvTitleSimpleCh() + '\r\n'

# 获取有效的 Log Index
for check_log_index in check_log_index_array:
    full_log_paht = GetLogFilePath(check_log_index)
    print(full_log_paht)
    if os.path.exists(full_log_paht):
        available_log_index_array.append(check_log_index)
        print('exist')
    else:
        print('not exist')
print(available_log_index_array)

log_analyzer_array = []
for index in available_log_index_array:
    full_log_paht = GetLogFilePath(index)
    analyzer = LogAnalyzer()

    # 记录 build_id
    analyzer.build_id = (str)(index)
    log_file = codecs.open(full_log_paht, 'rb')

    # 遍历 line
    lines = log_file.readlines()
    for line in lines:
        decode_line = line.decode('utf-8', 'ignore')

        # 检测特征
        GetBuildPerson(analyzer, decode_line)
        GetAnchorModulesStart(analyzer, decode_line)
        GetAnchorModulesEnd(analyzer, decode_line)
        GetCompileJsStart(analyzer, decode_line)
        GetCompileJsEnd(analyzer, decode_line)
        GetCookParm(analyzer, decode_line)
        GetBuildCmdStart(analyzer, decode_line)
        GetBuildCmdEnd(analyzer, decode_line)
        GetCookCmdStart(analyzer, decode_line)
        GetCookCmdEnd(analyzer, decode_line)
        GetStageCmdStart(analyzer, decode_line)
        GetStageCmdEnd(analyzer, decode_line)
        GetStageCmdStart(analyzer, decode_line)
        GetStageCmdEnd(analyzer, decode_line)
        GetFinalCopyStart(analyzer, decode_line)
        GetFinalCopyEnd(analyzer, decode_line)
        GetBuildResult(analyzer, decode_line)

    # 补完中间时段
    # 1.analyzer.progress_start 在 GetAnchorModulesEnd 中补完
    # 2.analyzer.progress_end 用 analyzer.build_cmd_start 代替
    analyzer.progress_end = analyzer.build_cmd_start

    # 计算 Duration
    analyzer.GetTimeDuration()
    analyzer.GetFullTime()

    # 输出检测信息
    analyzer.PrintLogAnalyzerInfo1()
    analyzer.PrintLogAnalyzerInfo2()

    # 添加信息至输出文本
    result += analyzer.GetCsvInfoSimple() + '\r\n'

# 保存检测信息 Csv 文件
SaveStringToFile(GetScriptPath() + '/deepoon_analyze_log_simple_csv.csv',
                 result)
print('Finish analyze logs!')

pause = input('Enter anything to exit...')
