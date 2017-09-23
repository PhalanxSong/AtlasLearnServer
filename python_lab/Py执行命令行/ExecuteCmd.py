import os  
import os.path  
import subprocess

cwd = os.getcwd()
bat_file_path = cwd + "\\" + "sam.bat"

cmd = ""
cmd += "cmd.exe /c "
cmd += bat_file_path

cmd_with_parm = cmd + " parm_1 parm_2 parm_3"

print("Command : "+ cmd_with_parm)

p = subprocess.Popen(cmd_with_parm, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

curline = p.stdout.readline()
while(curline != b''):
    print(curline)
    curline = p.stdout.readline()
     
p.wait()
print("Command Exit Code : " + (str)(p.returncode))

pause = input("Enter anything to end...")
