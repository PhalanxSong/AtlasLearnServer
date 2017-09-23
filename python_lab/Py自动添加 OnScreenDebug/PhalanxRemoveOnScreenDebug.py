import os  
import os.path  
import codecs

print("---------- Get Cpp File Path ----------")

rootdir = r"."  
fileNameList = []
cppList = []
for parent,dirnames,filenames in os.walk(rootdir):  
    for filename in filenames:
        if filename.endswith(".cpp"):
            cppList.append(os.path.join(parent,filename))

print("---------- Print Cpp File Path ----------")

for i in cppList:
    print(i)

print("---------- Delete All AddOnScreenDebugMessage ----------")

for i in range(len(cppList)):
    file_object = codecs.open(cppList[i],'rb')
    all_the_text = file_object.read().decode('utf-8')
    file_object.close()
    pos = 1
    modified = 0
    while pos > 0 :
        pos = all_the_text.find("GEngine->AddOnScreenDebugMessage(")
        if pos > 0 :
            modified = 1
            cpp_sec_1 = all_the_text[0:pos]
            cpp_sec_2 = all_the_text[pos:]
            pos2 = cpp_sec_2.find(";")
            cpp_sec_2 = cpp_sec_2[pos2+1:]
            cpp_sec_2 = cpp_sec_2.strip()
            all_the_text = cpp_sec_1 + cpp_sec_2
    if modified > 0 :
        all_the_text = all_the_text + "\n"
        all_the_text.encode("utf-8")
        file_object = codecs.open(cppList[i],'w',encoding='utf-8')
        file_object.write(all_the_text)
        file_object.close()

pause = input("Enter anything to end...")
