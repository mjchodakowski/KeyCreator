import ViewMain
import os
import datetime
import math
import random
import time
import random


def scriptedIn(key, pres):
    alf = "6]?qXsi3JI(y%*t!)E1#=O5eM.~<S$0&7PomQWLFuHY^vap|+b,V:_rCdl@2KUhA;}Z>wT-`9{BNk[zn8DGRxfj/gc4"
    alfT = ""
    """
    i = 0
    while len(alfT) > i:
        rand = random.randint(0, len(alfT)-1)
        alf += alfT[rand]
        alfT = alfT.replace(alfT[rand], "")
    print(alf)
    """
    pres = int(pres)

    if pres == 0:
        now = datetime.datetime.now()
        h = int(now.strftime("%H"))
        m = int(now.strftime("%M"))
        pres = m * h

    keyTemp = ""
    i = 0

    while len(key) > i:
        poz = alf.index(key[i])
        poz += pres
        poz = poz % len(alf)
        keyTemp += alf[poz]
        i += 1
    return keyTemp, pres


def scriptedOut(keyTemp, pres):
    alf = "6]?qXsi3JI(y%*t!)E1#=O5eM.~<S$0&7PomQWLFuHY^vap|+b,V:_rCdl@2KUhA;}Z>wT-`9{BNk[zn8DGRxfj/gc4"
    key = ""
    pres=int(pres)
    i = 0
    while len(keyTemp) > i:
        poz = alf.index(keyTemp[i])
        poz -= pres
        poz = poz % len(alf)
        key += alf[poz]
        i += 1
    """
    print(pres)
    jj = 0
    while jj < len(key):
        i = 0
        while len(alf) > i:
            if key[jj] == alf[i]:
                print(i)
                print("key     : " + str(jj) + " - " + key[jj] + " --- " + str(alf.index(key[jj])-alf.index(keyTemp[jj])) + " ---- "+ str((pres - poz) % len(alf)))
                print("keyTemp : " + str(jj) + " - " + keyTemp[jj] + " --- " + str(alf.index(keyTemp[jj])-alf.index(key[jj])) + " ---- " + str((abs( pres + 1)) % len(alf)))
            i += 1
        jj += 1
    """
    return key


def CreateMainKeysSave(key, fileName):
    pres = 0
    temp = scriptedIn(key, pres)
    file = open(fileName, "w+")
    file.seek(0, 0)
    file.tell()
    file.write(temp[0] + " " + str(temp[1]))
    file.write('\r')
    ViewMain.SaveKey()
    file.close()


def ChangeMainKeysSave(key, fileName):
    file = open(fileName, "r+")
    file.seek(0, 0)
    file.tell()
    temp_2 = file.readline()
    temp_2 = temp_2.split(" ")
    temp = scriptedIn(key, int(temp_2[1]))
    file.seek(0, 0)
    file.tell()
    file.write(temp[0] + " " + str(temp[1]))
    file.write('\r')
    ViewMain.SaveKey()
    file.close()


def checkMainKeys(passwd, fileName):
    file = open(fileName, "r")
    temp = file.readline()
    file.close()
    if len(temp) != 0:
        temp = temp.replace("\n", "")
        keyTemp = temp.split(" ")
        key = scriptedOut(keyTemp[0], int(keyTemp[1]))
        if key == passwd:
            ViewMain.Access()
            return True
        else:
            ViewMain.ErrorPaswd()
            return False
    else:
        ViewMain.errorFile()


def checkPassword(List, poz, fileName):
    file = open(fileName, "r")
    temp = file.readline()
    file.close()
    temp = temp.replace("\n", "")
    keyTemp = temp.split(" ")
    key = scriptedOut(List[int(poz)][2], int(keyTemp[1]))
    return key


def editPassword(fileName, position, sizeKey):
    file = open(fileName, "r")
    temps = file.readlines()
    file.close()
    ListTemp = []
    i = 0
    while i < len(temps):
        temp = temps[i].replace("\n", "")
        temp = temp.split(" ")
        ListTemp.append(temp)
        i += 1
    ViewMain.munuEditPassword(fileName, ListTemp, position, sizeKey)


def removePassword(position, fileName):
    file = open(fileName, "r")
    temps = file.readlines()
    file.close()
    ListTemp = []
    i = 0
    while i < len(temps):
        temp = temps[i].replace("\n", "")
        temp = temp.split(" ")
        ListTemp.append(temp)
        i += 1
    find = False
    i = 1

    while i < len(ListTemp):
        if int(ListTemp[i][0]) == int(position):
            ListTemp.remove(ListTemp[i])
            find = True
        i += 1

    i = 1
    file = open(fileName, "w+")
    file.write(ListTemp[0][0] + " " + ListTemp[0][1])
    while i < len(ListTemp):
        file.write("\n" + ListTemp[i][0] + " " + ListTemp[i][1] + " " + ListTemp[i][2])
        i += 1
    file.close()
    return find


def removeAllPassword(fileName):
    file = open(fileName, "r")
    temp = file.readline()
    temp = temp.replace("\n", "")
    file.close()
    file = open(fileName, "w+")
    file.write(temp)
    file.close()


def genPassword(size):
    log = "abcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*"
    i = 0
    temp = ""
    while i < int(size):
        temp += log[random.randint(0, len(log) - 1)]
        i += 1
    return temp


def yesOrNo(temp):
    if temp:
        return "TAK"
    else:
        return "NIE"


def configName(adresFile, sizeKey, mustWelcome, mustKey, encrypt):
    T = True
    while T:
        file = open("configuration.conf", "r")
        temps = file.readlines()
        file.close()
        ListTemp = []
        i = 0
        while i < len(temps):
            temp = temps[i].replace("\n", "")
            temp = temp.split(" ")
            ListTemp.append(temp)
            i += 1
        ol = ""

        print("")
        i = 0
        zm = ""
        List = ListTemp

        file = open(adresFile, "r")
        temps2 = file.readlines()
        file.close()
        ListTem = []
        i = 0

        while i < len(temps2):
            temps1 = temps2[i].replace("\n", "")
            temps1 = temps1.split(" ")
            ListTem.append(temps1)
            i += 1
        while len(ListTem[0][0]) >= i:
            zm += "*"
            i += 1
        print(
            "                                                                                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(
            "                                                                                     ▒ save ▒  ZAPISZ     ▒")
        print(
            "                                                                                     ▒   q  ▒  WYJSCIE    ▒")
        print(
            "                                                                                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("")
        print(
            "         ██████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "         ███████                                                 █                                        █")
        print(
            "         █  1  █     NAZWA PLIKU Z DANYMI                        " + "█   {0:37s}".format(adresFile) + "█")
        print(
            "         ███████                                                 █                                        █")
        print("         █  2  █     DOMYŚLNA LICZBA ZNAKÓW W HASLE GENEROWANYM  " + "█   {0:37s}".format(
            str(sizeKey)) + "█")
        print(
            "         ███████                                                 █                                        █")
        print("         █  3  █     POKAZUJ OBRAZ POWITALNY                     " + "█   {0:37s}".format(
            yesOrNo(mustWelcome)) + "█")
        print(
            "         ███████                                                 █                                        █")
        print("         █  4  █     WYMAGAJ HASŁA PRZED URUCHOMIENIEM           " + "█   {0:37s}".format(
            yesOrNo(mustKey)) + "█")
        print(
            "         ███████                                                 █                                        █")
        print("         █  5  █     SZYFROWANIE                                 " + "█   {0:37s}".format(
            yesOrNo(encrypt)) + "█")
        print(
            "         ███████                                                 █                                        █")
        print("         █  6  █     ZMIANA HASŁA GŁÓWNEGO                       " + "█   {0:37s}".format(zm) + "█")
        print(
            "         ███████                                                 █                                        █")
        print(
            "         ██████████████████████████████████████████████████████████████████████████████████████████████████")
        print("")
        print('    %+90s' % ('Wprowadz znak komendy:  ',), end="")
        command = input()

        if command != "1" and command != "2" and command != "3" and command != "4" and command != "5" and command != "6" and command != "save" and "q" != command:
            print("")
            print("                           ███████████████████████████████████████████████████████████████")
            print("                           █                                                             █")
            print('                           █                    NIEPRAWIDŁOWA KOMENDA                    █')
            print('                           █  Prosze wybrać znak z listy  - 1, 2, 3, 4, 5, 6  save lub q █')
            print("                           █                                                             █")
            print("                           ███████████████████████████████████████████████████████████████")
            time.sleep(2)
            os.system("cls")

        if command == "q":
            os.system("cls")
            break
        else:
            if command == "1":
                print('    %+90s' % ('Wprowadz nazwe do pliku:  ',), end="")
                adresFileT = input()
                try:
                    file = open(adresFileT, "r")
                except:
                    if adresFileT != "":
                        print('    %+90s' % ('Plik nie istnieje czy chcesz go utworzyć? (y/n) : ',), end="")
                        n = input()
                        if n == 'y':
                            file = open(adresFileT, "w+")
                            temp_2 = file.readline()
                            print('    %+90s' % ('Wprowadz hasło główne: ',), end="")
                            p = input()
                            if encrypt:
                                file.seek(0, 0)
                                file.tell()
                                temp_2 = file.readline()
                                temp_2 = temp_2.split(" ")
                                p = scriptedIn(p, temp_2[1])
                            file.write(str(p[0]) + " " + str(p[1]))
                            adresFile = adresFileT

                        else:
                            print('    %+90s' % (' Nazwa nie moze być pusta! ',), end="")
                            time.sleep(3)
                        os.system("cls")
            else:
                if command == "5":
                    print('    %+90s' % ('Czy wyłączyć szyfrowanie? (y/n) : '), end="")
                    n = input()
                    if n == 'y':
                        encrypt = False
                    else:
                        encrypt = True
                    os.system("cls")
                else:
                    if command == "4":
                        print('    %+90s' % ('Czy wymagać hasła głównego? (y/n) : '), end="")
                        n = input()
                        if n == 'n':
                            mustKey = False
                        else:
                            mustKey = True
                        os.system("cls")
                    else:
                        if command == "3":
                            print('    %+90s' % ('Czy wyświetlać wiadomość powitalną? (y/n) : '), end="")
                            n = input()
                            if n == 'n':
                                mustWelcome = False
                            else:
                                mustWelcome = True
                            os.system("cls")
                        else:
                            if command == "2":
                                print('    %+90s' % ('Proszę podać domyślną ilość znaków generowych haseł: '), end="")
                                n = input()
                                while 40 < int(n) or int(n) < 0:
                                    print('    %+90s' % ('Przekroczona ilość znaków (0 do 40)'))
                                    time.sleep(1)
                                    print('    %+90s' % ('Proszę podać domyślną ilość znaków generowych haseł: '),
                                          end="")
                                    n = input()
                                if 40 > int(n) > 0:
                                    sizeKey = n
                                os.system("cls")
                            else:
                                if command == "save":
                                    file = open("configuration.conf", "w+")
                                    file.write(adresFile + " " + str(sizeKey) + " " + str(mustWelcome) + " " + str(
                                        mustKey) + " " + str(encrypt))
                                    file.close()
                                    ViewMain.operationSuccess()
                                    os.system("cls")
                                else:
                                    if command == "6":
                                        print('    %+90s' % ('Proszę podać nowe hasło: '),
                                              end="")
                                        n = input()
                                        print('    %+90s' % ('Proszę podać ponowenie nowe hasło: '),
                                              end="")
                                        nn = input()

                                        if nn != n:
                                            ViewMain.ErrorKey()
                                        else:
                                            file = open(adresFile, "r")
                                            temps = file.readlines()
                                            file.close()
                                            ListTemp = []
                                            i = 0

                                            while i < len(temps):
                                                temp = temps[i].replace("\n", "")
                                                temp = temp.split(" ")
                                                ListTemp.append(temp)
                                                i += 1

                                            ListTemp[0][0] = n
                                            file = open(adresFile, "w+")
                                            file.write(
                                                scriptedIn(ListTemp[0][0], ListTemp[0][1])[0] + " " + ListTemp[0][1])
                                            ii = 0
                                            while i < len(List):
                                                file.write(
                                                    "\n" + ListTemp[i][0] + " " + ListTemp[i][1] + " " + ListTemp[i][2])
                                                ii += 1
                                            file.close()
                                            ViewMain.operationSuccess()

                                            os.system("cls")

    return encrypt, mustKey, mustWelcome, sizeKey
