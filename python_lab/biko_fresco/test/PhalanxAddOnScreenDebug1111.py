import os
import os.path
import codecs
import random

colors = [
    "Red", "Green", "Blue", "Yellow", "Cyan", "Magenta", "Orange", "Purple",
    "Turquoise", "Silver"
]


def GetColor(colorIndex):
    realId = colorIndex % len(colors)
    return colors[realId]

rootdirs = [r"C:\xBuild\Plugins", r"C:\xBuild\Source"]

def GetCppPathFromRootdirList(rootdirs):
    print("---------- Get Cpp Path From Rootdir List ----------")

    cppFileNameList = []
    cppFullPathList = []

    for rootdir in rootdirs:
        for parent, dirnames, filenames in os.walk(rootdir):
            #case 1:
            #for dirname in dirnames:
            #    print("parent folder is:" + parent)
            #    print("dirname is:" + dirname)
            #case 2
            for filename in filenames:
                #print("parent folder is:" + parent)
                #print("filename with full path:"+ os.path.join(parent,filename))
                if filename.endswith(".cpp"):
                    #print(filename)
                    cppFileNameList.append(filename[0:-4])
                    cppFullPathList.append(os.path.join(parent, filename))

    #print("---------- Print Cpp File Path ----------")
    # for i in cppFileNameList:
    #     print(i)
    # for i in cppFullPathList:
    #     print(i)
    return (cppFileNameList, cppFullPathList)


# print("---------- Add AddOnScreenDebugMessage To HandleRequest ----------")
# for i in range(len(cppList)):
#     file_object = codecs.open(cppList[i],'rb')
#     all_the_text = file_object.read().decode('utf-8')
#     file_object.close()
#     pos = all_the_text.find("HandleRequest(FRequestPtr InOutRequest, FResponsePtr InOutResponse)")
#     if pos > 0 :
#         cppSec1 = all_the_text[0:pos]
#         cppSec2 = all_the_text[pos:]
#         pos2 = cppSec2.find("{")
#         cppSec21 = cppSec2[0:pos2+1]
#         cppSec22 = cppSec2[pos2+1:]
#         modify = "\n\tGEngine->AddOnScreenDebugMessage(-1, 6, FColor::" + GetColor(i) + ", \"" + fileNameList[i] + "::HandleRequest\", false);\n"
#         modifiedFile = cppSec1 + cppSec21 + modify + cppSec22
#         modifiedFile.encode("utf-8")
#         file_object = codecs.open(cppList[i],'w',encoding='utf-8')
#         file_object.write(modifiedFile)
#         file_object.close()
# pasue = input("Enter anything to end...")
