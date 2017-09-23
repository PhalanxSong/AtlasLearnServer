import os
import os.path
import codecs
import random

fafa = r'C:\Users\PC\Desktop\PythonLab\haha.txt'
fafa2 = r'C:\Users\PC\Desktop\PythonLab\hahalog.txt'
fafa3 = r'C:\Users\PC\Desktop\PythonLab\hah232.txt'

file_object = codecs.open(fafa, 'rb')
text = file_object.read().decode('utf-8')
file_object.close()

text = text.replace('\r', '')
text = text.replace('\n', ',')
text = text.replace('\t', '')
text = text.replace(' ', '')

print(text)
file_object = codecs.open(fafa3, 'w', encoding='utf-8')
file_object.write(text)
file_object.close()

arr = text.split(',')

log = ""

for i in range((int)(len(arr) / 2)):
    if arr[i * 2] == arr[i * 2 + 1]:
        log += (str)(i) + "\n"
        log += arr[i * 2] + " : " + arr[i * 2 + 1] + "\n"

file_object = codecs.open(fafa2, 'w', encoding='utf-8')
file_object.write(log)
file_object.close()