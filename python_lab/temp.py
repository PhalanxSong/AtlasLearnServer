import os
import os.path
import subprocess

test = ""
test += os.getcwd()
test += "cmd.exe /c "
test += "bat_file_path"

print("Command : " + test)

pause_var = input("Enter anything to end 1...")
print(pause_var)
pause_var = input("Enter anything to end 2...")
print(pause_var)
