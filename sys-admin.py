#import os
import subprocess

# os.system("ls")
# subprocess.run(["ls", "-l", "README.md"])
# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])


# command="ps"
# commandArgument="-x"
# print(f'Gathering active process information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])


# command="df"
# commandArgument="-h"
# print(f'Gathering disk information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])


sudo="sudo"
command="fdisk"
commandArgument="-l"
print(f'Gathering partition information with command: {sudo} {command} {commandArgument}')
#subprocess.run([sudo,command,commandArgument])

try:
    subprocess.run([sudo,command,commandArgument])
except:
    print("Unexpected error:")

