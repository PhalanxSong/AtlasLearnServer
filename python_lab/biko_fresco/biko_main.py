import codecs
import os
import os.path
import random
import operator
import json

import re

import str_utils as strUtils
import biko_file_utils as bikoFileUtils
import log_utils as logUtils
import biko_path as bikoPath

log = logUtils.Logger()

######## step 1 : 获取全部需要遍历的 .h .cpp 文件信息 ########

#### FileNamePath ( fileName , filePath )

# 全部 .cpp
cppFileNamePathList = bikoFileUtils.GetFilePathFromRootdirListWithExt(
    bikoPath.xBuilderRootdirs, '.cpp')

# 获取 有效的 .cpp
for i in bikoPath.ignoreCppExt:
    cppFileNamePathList = bikoFileUtils.RemoveFileWithExt(
        cppFileNamePathList, i)
for i in bikoPath.ignorePathContain:
    cppFileNamePathList = bikoFileUtils.RemoveFileWithPathContain(
        cppFileNamePathList, i)
for i in bikoPath.ignorePluginDir:
    cppFileNamePathList = bikoFileUtils.RemoveFileWithPathStart(
        cppFileNamePathList, bikoPath.xBuilderPluginRoot + i)
for i in bikoPath.ignoreSourceDir:
    cppFileNamePathList = bikoFileUtils.RemoveFileWithPathStart(
        cppFileNamePathList, bikoPath.xBuilderSourceRoot + i)

log.LogDebug('cursory .cpp file count : ' + (str)(len(cppFileNamePathList)))

# 全部 .h
hFileNamePathList = bikoFileUtils.GetFilePathFromRootdirListWithExt(
    bikoPath.xBuilderRootdirs, '.h')

# 获取 有效的 .h
for i in bikoPath.ignoreHeaderExt:
    hFileNamePathList = bikoFileUtils.RemoveFileWithExt(hFileNamePathList, i)
for i in bikoPath.ignorePathContain:
    hFileNamePathList = bikoFileUtils.RemoveFileWithPathContain(
        hFileNamePathList, i)
for i in bikoPath.ignorePluginDir:
    hFileNamePathList = bikoFileUtils.RemoveFileWithPathStart(
        hFileNamePathList, bikoPath.xBuilderPluginRoot + i)
for i in bikoPath.ignoreSourceDir:
    hFileNamePathList = bikoFileUtils.RemoveFileWithPathStart(
        hFileNamePathList, bikoPath.xBuilderSourceRoot + i)

log.LogDebug('cursory .h file count : ' + (str)(len(hFileNamePathList)))

noHeaderFileNamePathList = []
effectiveListTemp = []
for i in cppFileNamePathList:
    if i[0] not in [x[0] for x in hFileNamePathList]:
        noHeaderFileNamePathList.append(i)
    else:
        effectiveListTemp.append(i)
cppFileNamePathList = effectiveListTemp

for i in noHeaderFileNamePathList:
    log.LogWarn('no .h file : ' + i[1])

noCppFileNamePathList = []
effectiveListTemp = []
for i in hFileNamePathList:
    if i[0] not in [x[0] for x in cppFileNamePathList]:
        noCppFileNamePathList.append(i)
    else:
        effectiveListTemp.append(i)
hFileNamePathList = effectiveListTemp

for i in noCppFileNamePathList:
    log.LogWarn('no .cpp file : ' + i[1])

log.LogDebug('after remove .cpp file count : ' +
             (str)(len(cppFileNamePathList)))
log.LogDebug('after remove .h file count : ' + (str)(len(hFileNamePathList)))

######## step 2 : utf-8 check ########

allFile = cppFileNamePathList + hFileNamePathList
notUtf8File = []

for i in (allFile):
    try:
        fileObject = codecs.open(i[1], 'rb')
        text = fileObject.read().decode('utf-8')
        fileObject.close()
    except:
        notUtf8File.append(i)
        continue

if len(notUtf8File) > 0:
    log.LogError('have not utf-8 file')
    for i in notUtf8File:
        log.LogError('not utf-8 file : ' + i[1])
    raise Exception('have not utf-8 file')
else:
    log.LogDebug('all file are utf-8')

######## step 3 : combine .h .cpp file ########

allHeadCppList = []

for i in hFileNamePathList:
    for j in cppFileNamePathList:
        if i[0] == j[0]:
            allHeadCppList.append([i[0], i[1], j[1]])
            break
log.LogDebug('head cpp list count : ' + (str)(len(allHeadCppList)))

######## step 4 : find all system ########

abstractSystems = []
compSystems = []
requestHandlerSystems = []

patternAbstractSystem = re.compile(r'\s+(\w+)\s*:\s*public\s+AbstractSystem')
patternCompSystem = re.compile(r'\s+(\w+)\s*:\s*public\s+ACompSystem')
patternRequestHandlerSystem = re.compile(
    r'\s+(\w+)\s*:\s*public\s+ARequestHandlerSystem')

for i in allHeadCppList:
    fileObject = codecs.open(i[1], 'rb')
    text = fileObject.read().decode('utf-8')
    fileObject.close()
    match1 = patternAbstractSystem.search(text)
    if match1:
        abstractSystems.append(i)
    else:
        match1 = patternCompSystem.search(text)
        if match1:
            compSystems.append(i)
        else:
            match1 = patternRequestHandlerSystem.search(text)
            if match1:
                requestHandlerSystems.append(i)
    if match1:
        systemName = match1.group(1)
        if not systemName.startswith('A'):
            log.LogWarn('not start with A system : ' + systemName)
        i.append(systemName)

log.LogDebug('AbstractSystem count : ' + (str)(len(abstractSystems)))
log.LogDebug('ACompSystem count : ' + (str)(len(compSystems)))
log.LogDebug('ARequestHandlerSystem count : ' +
             (str)(len(requestHandlerSystems)))

######## step 5 : check system name and file name ########

allSystem = abstractSystems + compSystems + requestHandlerSystems
for i in allSystem:
    nameTemp = i[3]
    if nameTemp.startswith('A'):
        nameTemp = nameTemp[1:]
    if i[0] != nameTemp:
        log.LogWarn('system name != file name : ' + i[0] + ' ' + nameTemp)

######## step : get handle request path ########

getReqHandlerPathSystem = []
patternGetHandlePath1 = re.compile(
    r'\s*FString\s+\w+::GetHandlePath[(][)]\s+const\s*[{]([\s\S]+?;)\s*[}]')
patternGetHandlePath2 = re.compile(r'return\s+([\s\S]+?)\s*;')
getHandledReqCount = 0
for i in allSystem:
    fileObject = codecs.open(i[2], 'rb')
    text = fileObject.read().decode('utf-8')
    fileObject.close()
    req = ''
    match1 = patternGetHandlePath1.search(text)
    if match1:
        getReqHandlerPathSystem.append(i)
        temp = match1.group(1)
        # print('------------')
        # print(match1.group(1))
        match2 = patternGetHandlePath2.search(temp)
        if match2:
            req = match2.group(1)
            getHandledReqCount += 1
            if not '::' in req:
                if '"' in req:
                    #log.LogWarn('hard code handle path : ' + i[0] + ' ' + req)
                    pass
                else:
                    #log.LogWarn('local handle path : ' + i[0] + ' ' + req)
                    req = i[3] + '::' + req
        else:
            log.LogError('error handle path : ' + i[0] + ' ' + temp)
    req = strUtils.CleanStr(req)
    if req == 'CommonConst::String_Empty':
        log.LogError('an empty handled req system : ' + i[3])
    i.append(req)
log.LogDebug('get handled request system count : ' + (str)(getHandledReqCount))

check = True
for i in requestHandlerSystems:
    if not i[0] in [x[0] for x in getReqHandlerPathSystem]:
        check = False
        log.LogError('can not find handled req for system ' + i[0])
if check == False:
    raise Exception('some request handler system can not find handled req')

######## step : get registerd request path ########

patternRegisterRequestCheck = re.compile(r'RegisterRequest\s*?[(]')
patternRegisterRequest = re.compile(
    r'\s*RegisterRequest\s*?[(]([\s\S]+?)[)]\s*;')
for i in allSystem:
    fileObject = codecs.open(i[2], 'rb')
    text = fileObject.read().decode('utf-8')
    fileObject.close()
    registerReqCheckArray = patternRegisterRequestCheck.findall(text)
    registerReqArray = patternRegisterRequest.findall(text)
    if len(registerReqCheckArray) != len(registerReqArray):
        log.LogError('RegisterRequest cpp has some strange : ' + i[0])
    for x in registerReqArray:
        if not '::' in x and not '"' in x:
            log.LogError('RegisterRequest is not valid : ' + i[0] + ' ' + x)
    temp = []
    for x in registerReqArray:
        temp.append(strUtils.CleanStr(x))
    registerReqArray = temp
    i.append(registerReqArray)

######## step 6 : find UnitRegisterInterface ########

unitRegisters = []

patternUnitRegister = re.compile(
    r'\s+(\w+)\s*:\s*public\s+UnitRegisterInterface')
for i in allHeadCppList:
    fileObject = codecs.open(i[1], 'rb')
    text = fileObject.read().decode('utf-8')
    fileObject.close()
    match1 = patternUnitRegister.search(text)
    if match1:
        unitRegisters.append(i)
        unitRegisterName = match1.group(1)
        i.append(unitRegisterName)

log.LogDebug('UnitRegister count : ' + (str)(len(unitRegisters)))

######## step 7 : find all registered system and get message list ########

registeredSystemName = []

patternRegisterSystem = re.compile(
    r'\s+RegisterSystem[(]\s*(\w+)::Creator[(][)]')
# patternRegisterMessage = re.compile(
#     r'\s+MessageRouter::Instance[(][)].Register[(]\s*(\w[\s\S]+\w)\s*,\s*(\w[\s\S]+\w)\s*,\s*(\w[\s\S]+\w)\s*,\s*(\w[\s\S]+\w)\s*[)];'
# )
patternRegisterMessage = re.compile(
    r'\s+MessageRouter::Instance[(][)].Register[(]([\s\S]+?)[)];')
for i in unitRegisters:
    fileObject = codecs.open(i[2], 'rb')
    text = fileObject.read().decode('utf-8')
    fileObject.close()
    registerSystemArray = patternRegisterSystem.findall(text)
    i.append(registerSystemArray)
    if len(registerSystemArray) == 0:
        log.LogDebug('no registered system UnitRegister : ' + i[3])
    registeredSystemName += registerSystemArray
    registerMessageArray = patternRegisterMessage.findall(text)
    i.append(registerMessageArray)
    #print(len(registerMessageArray))

log.LogDebug('all registered system count : ' +
             (str)(len(registeredSystemName)))

for i in unitRegisters:
    for j in range(len(i[5])):
        temp = i[5][j]
        temp = strUtils.CleanStr(temp)
        temp = temp.replace('FDeviceControlState::Any()', '')
        temp = temp.replace('SystemMessageAction::System()', '')
        if '"' in temp:
            log.LogWarn('hard code in message : ' + i[3])
        i[5][j] = temp

messageList = []
for i in unitRegisters:
    for j in i[5]:
        temp = j
        splitTemp = temp.split(',')
        req = splitTemp[-1]
        msg = [splitTemp[0], splitTemp[1]]
        msgPath = splitTemp[2:-1]
        exist = False
        for x in messageList:
            if operator.eq(x[0], msg):
                x[1].append(msgPath)
                x[2].append(req)
                exist = True
                break
        if not exist:
            messageList.append([msg, msgPath, [req]])

log.LogDebug('all different message count : ' + (str)(len(messageList)))

# for i in messageList:
#     print('message : ' + i[0] + ' to req count : ' + (str)(len(i[1])))

# for i in messageList:
#     print(i)

######## step : gather msg and req ########

allHandledReq = []
for i in allSystem:
    handledReq = i[4]
    if handledReq != '':
        if handledReq in allHandledReq:
            raise Exception('a req has been handled by multi system : ' +
                            handledReq)
        allHandledReq.append(handledReq)
log.LogDebug('all handled request count : ' + (str)(len(allHandledReq)))

allSysSendReq = []
for i in allSystem:
    registerdReq = i[5]
    for x in registerdReq:
        if not x in allSysSendReq:
            allSysSendReq.append(x)
log.LogDebug('all system send request count : ' + (str)(len(allSysSendReq)))

allMsgSendReq = []
for i in messageList:
    for j in i[2]:
        if not j in allMsgSendReq:
            allMsgSendReq.append(j)
log.LogDebug('all message send request count : ' + (str)(len(allMsgSendReq)))

allExistReq = []
allExistReq += allHandledReq
for i in allHandledReq:
    if not i in allExistReq:
        allExistReq.append(i)
for i in allMsgSendReq:
    if not i in allExistReq:
        allExistReq.append(i)
log.LogDebug('all exist request count : ' + (str)(len(allExistReq)))

noHandledReq = []
for i in allExistReq:
    if not i in allHandledReq:
        noHandledReq.append(i)
log.LogWarn('no handled request count : ' + (str)(len(noHandledReq)))
for i in noHandledReq:
    log.LogWarn('no handled request : ' + i)

######## step : get req which not send by msg and req ########

reqNotSendByReqMsg = []
for i in allExistReq:
    if not i in allSysSendReq and not i in allMsgSendReq:
        reqNotSendByReqMsg.append(i)
log.LogDebug('req which not send by msg and req count : ' +
             (str)(len(reqNotSendByReqMsg)))

handledReqNotSendByReqMsg = []
for i in reqNotSendByReqMsg:
    if i in allHandledReq:
        handledReqNotSendByReqMsg.append(i)
log.LogDebug('handled req which not send by msg and req count : ' +
             (str)(len(handledReqNotSendByReqMsg)))

######## step :  ########

# for i in handledReqNotSendByReqMsg:
#     print('top req : ' + i)


def GetFrescoFromReqRecur(req, parentCache, allSystem, messageList):
    root = {}
    reqTag = 'Req-- ' + req
    root['name'] = reqTag
    if reqTag in parentCache:
        root['name'] += " --Loop"
        return root
    for i in allSystem:
        if i[4] == req:
            registerdReq = i[5]
            if len(registerdReq) > 0:
                children = []
                newParentCache = parentCache + [reqTag]
                for j in registerdReq:
                    child = GetFrescoFromReqRecur(j, newParentCache, allSystem,
                                                  messageList)
                    children.append(child)
                root['children'] = children
            else:
                root['name'] += " --Final"
    return root


def GetFrescoFromMsgRecur(msgId, parentCache, allSystem, messageList):
    root = {}
    msgTag = "Msg-- " + msgId[0] + '--' + msgId[1]
    root['name'] = msgTag
    if msgTag in parentCache:
        root['name'] += " --Loop"
        return root
    for i in messageList:
        if operator.eq(msgId, i[0]):
            msg = i
            msgSendReqs = msg[2]
            if len(msgSendReqs) > 0:
                children = []
                newParentCache = parentCache + [msgTag]
                for j in msgSendReqs:
                    child = GetFrescoFromReqRecur(j, newParentCache, allSystem,
                                                  messageList)
                    children.append(child)
                root['children'] = children
            else:
                root['name'] += " --MsgFinal"
    return root


def GetFrescoEntr(allSystem, messageList, handledReqNotSendByReqMsg):
    root = {}
    root['name'] = 'root'
    children = []
    parentCache = []
    for i in handledReqNotSendByReqMsg:
        child = GetFrescoFromReqRecur(i, parentCache, allSystem, messageList)
        children.append(child)
    for i in messageList:
        child = GetFrescoFromMsgRecur(i[0], parentCache, allSystem,
                                      messageList)
        children.append(child)
    if len(children) > 0:
        root['children'] = children
    return root


root = GetFrescoEntr(allSystem, messageList, handledReqNotSendByReqMsg)
jsonOutput = json.dumps(root)

fileOutput = bikoFileUtils.GetScriptPath(
) + bikoPath.outputDir + r'\biko_fresco.json'
log.LogDebug('output file : ' + fileOutput)

fileObject = codecs.open(fileOutput, 'w', encoding='utf-8')
fileObject.write(jsonOutput)
fileObject.close()

fileLogOutput = bikoFileUtils.GetScriptPath(
) + bikoPath.outputDir + r'\biko_fresco_log.txt'
log.LogDebug('output log file : ' + fileLogOutput)
log.LogOutput(fileLogOutput)
