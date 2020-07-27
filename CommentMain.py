from ViewMain import *
from createChangeMainKey import *


def ListViewPassword(fileName):
    file = open(fileName, "r")
    temps = file.readlines()
    file.close()
    ListTemp = []
    i = 1
    print(temps[1])
    while i < len(temps):
        temp = temps[i].replace("\n", "")
        temp = temp.split(" ")
        ListTemp.append(temp)
        i += 1
    poz = ViewList(ListTemp)
    key = checkPassword(ListTemp, poz)
    return key, ListTemp[int(poz)]


def CreateNewPassword():
    tr = True
    while tr:
        a = CreatePasswordMain(True)
        b = CreatePasswordMain(False)
        if a == b:
            return a
        else:
            ErrorKey()
            return ""


def ChangePasswordMain():
    if checkMainKeys(Logon()):
        key = CreateNewPassword()
        if key != "":
            ChangeMainKeysSave(key)


def CreateNewKey(fileName):
    NewKey()
    i = CreatePasswordMain(1)
    ii = CreatePasswordMain(0)
    if i == ii:
        CreateMainKeysSave(ii, fileName)
    else:
        ErrorKey()
