import subprocess
import os

#Delete old build
buildPath = os.getcwd() + "\\build\\"
if(os.path.isfile(buildPath+"main.exe")):
    print("Removed old build.")
    os.remove(buildPath + "main.exe")

#Base command
command = ["g++", "-o", "./build/main.exe", "main.cpp"]
#Header files
command.append("-Iinclude")

#Libraries
command.append("-Llib")
command.append("-lmingw32")
command.append("-lSDL2main")
command.append("-lSDL2")

subprocess.Popen(command)

print("---------------------------------")
print(*command)
print("---------------------------------")

print("Building complete.")

os.chdir(buildPath)

#Ensure windows recognizes there's a new build
while not (os.path.isfile(os.getcwd() + "\\main.exe")):
    pass