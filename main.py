import os
import time
import math

######################
import ViewMain
import Creater
import createChangeMainKey
from CommentMain import *
from ViewMain import *

################################

adresFile = "date"


def yn(bools):
    if "True" == bools:
        return 1
    else:
        return 0


def openConfigFile():
    file = open("configuration.conf", "a+")
    file.seek(0)
    temp_ = file.readline()
    if len(temp_) <= 0:
        fileName = "config"
        sizeKey = 10
        viewWelcome = True
        mustKey = True
        encrypt = True
        file.write(fileName + " " + str(sizeKey) + " " + str(viewWelcome) + " " + str(mustKey) + " " + str(encrypt))
        file.close()
    else:
        _temp = temp_.split(" ")
        fileName = _temp[0]
        sizeKey = int(_temp[1])
        viewWelcome = bool(yn(_temp[2]))
        mustKey = bool(yn(_temp[3]))
        encrypt = bool(yn(_temp[4]))

    return fileName, sizeKey, viewWelcome, mustKey, encrypt


def MenuW(configMain):
    a = ViewMain.MainView()
    if a == "1":
        Editor(configMain[0], configMain[1], configMain[4])
    else:
        if a == "2":
            ViewPasswordEdg()
        else:
            if a == "4":
                ChangePasswordMain()
            else:
                if a == "x":
                    configMain = configName(configMain[0], configMain[1], configMain[2], configMain[3], configMain[4])

    if a == "q":
        return 1
    return 0, configMain


################################

try:
    file = open(openConfigFile()[0], "r")
    file.close()
except FileNotFoundError:
    CreateNewKey(openConfigFile()[0])

# ViewMain.welcome()
i = 0
T = True
ii = 0
startRun = True
while T:
    temp = openConfigFile()
    if startRun and temp[2]:
        ViewMain.rys()
        ViewMain.welcome()
    KeyOK = True
    while temp[3] and startRun and KeyOK:
        if checkMainKeys(Logon(), temp[0]):
            T = True
            break
        if ii > 2:
            KeyOK = False
            T = False
        ii += 1

    if KeyOK:
        startRun = False
        configuration = MenuW(temp)
        if configuration[0]:
            T = False

os.system("cls")
