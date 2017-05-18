import os, sys, glob
import subprocess as sp
import signal as sig
from shutil import copy2

curPath = "pycrust>: ";
str = input(curPath);
dirStack = list();
fileStack = list();
while(True):

    cmd = str.split(" ");
    if(cmd[0] == "exit"):
        print("Exited with status " + cmd[1]);
        stat = int(cmd[1]);
        sys.exit(stat);

    #Change directory
    elif(cmd[0] == "cd"):
        fullWord = "";
        for i in range(1, len(cmd)):
            if(i > 1):
                fullWord += " ";
            fullWord += cmd[i];
        try:
            os.chdir(fullWord);
        except Exception:
            print("Can't move there");

    #List files in current directory
    elif(cmd[0] == "ls"):
        listDir = os.listdir(os.getcwd());
        for i in range(len(listDir)):
            print(listDir[i]);

    #Create directory
    elif(cmd[0] == "mkdir"):
        try:
            fullWord = "";
            for i in range(1, len(cmd)):
                if(i > 1):
                    fullWord += " ";
                fullWord += cmd[i];
            os.mkdir(fullWord);
        except Exception:
            print("Path already exists");

    #Remove directory
    elif(cmd[0] == "rmdir"):
        try:
            os.rmdir(cmd[1]);
        except Exception:
            print("Path does not exist");

    #Current location
    elif(cmd[0] == "wh"):
        print(os.getcwd());

    #Clear screen
    elif(cmd[0] == "cls"):
        clrScrn = sp.call('cls', shell=True);

    #Push directory onto directory stack
    elif(cmd[0] == "pushd"):
        fullWord = "";
        for i in range(1, len(cmd)):
            if(i > 1):
                fullWord += " ";
            fullWord += cmd[i];
        dirStack.append(fullWord);

    #Pop directory and navigate to it
    elif(cmd[0] == "popd"):
        try:
            os.chdir(dirStack.pop());
        except Exception:
            print("Path does not exist");

    #List directory stack contents
    elif(cmd[0] == "dst"):
        print(dirStack[0:]);

    #Push file onto file  stack
    elif(cmd[0] == "pushf"):
        if(not cmd[1].startswith("*")):
            fileStack.append(os.getcwd() + "\\" + cmd[1]);
        else:
            for file in glob.glob(cmd[1]):
                fileStack.append(os.getcwd() + "\\" + file);

    #Pop file off and copy it to the current directory
    elif(cmd[0] == "popf"):
        copy2(fileStack.pop(), os.getcwd());

    #Check contents of file stack
    elif(cmd[0] == "fst"):
        print(fileStack[0:]);

    #Copy all files on the stack to the current directory
    elif(cmd[0] == "flushf"):
        for i in range(len(fileStack)):
            copy2(fileStack.pop(), os.getcwd());

    elif(cmd[0] == "delf"):
        try:
            ans = input("Are you sure you want to delete this file: " + cmd[1] + " y/n: ");
            if(ans == "y"):
                os.remove(cmd[1]);
            else:
                print("Nothing was deleted");
        except Exception:
            print("Could not find the specified file or path");

    curPath = "pycrust>: ";
    str = input(curPath);
