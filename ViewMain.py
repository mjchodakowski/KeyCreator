import os
import time
from createChangeMainKey import *


def welcome():
    print("")
    print("                              ██████████████████████████████████████████████████████████")
    print("                              █                                                        █")
    print('                              █      Witam serdecznie,                                 █')
    print('                              █      w aplikacji napisane w Pythonie służącej do       █')
    print('                              █      generowania psełdolosowych haseł w pełni          █')
    print('                              █      zróżnicowanych bespiecznych, aplikacja jest       █')
    print('                              █      także zabezpiczone przed niepowołanym dostępem,   █')
    print('                              █      dane są szyfrowane  bezpiecznym algorytmem.       █')
    print('                              █      Życze miłej pracy z aplikacją                     █')
    print('                              █      Pozdrawiam                                        █')
    print("                              █                                                        █")
    print("                              ██████████████████████████████████████████████████████████")
    time.sleep(7)
    os.system("cls")


def MainView():
    print("")
    print("                                                                                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("                                                                                     ▒ x ▒  Ustawienia   ▒")
    print("                                                                                     ▒ q ▒  Wyjdz        ▒")
    print("                                                                                     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("")
    print("        ██████████████████████████████████████████████████████████████████████████████████████████████████")
    print("        █                                                                                                █")
    print('        █        1                               - %+55s' % ('TWORZENIE I EDYCJA HASEŁ DOSTEPOWYCH █',))
    print('        █                                                                                                █')
    print('        █                                                                                                █')
    print("        █                                                                                                █")
    print("        █                                                                                                █")
    print("        █                                                                                                █")
    print("        ██████████████████████████████████████████████████████████████████████████████████████████████████")
    print("        ██████████████████████████████████████████████████████████████████████████████████████████████████")
    print("")
    p = input("                                        Aby uruchomić funkcje wprowadz odpowiednią liczbe z pozycji : ")
    time.sleep(0.3)
    os.system("cls")
    return p


def NewKey():
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █            Przed pierwszym uruchomieniem musi być         █')
    print('                           █                  wprowadzone hasło dostepowe              █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(4)


def CreatePasswordMain(part):
    tr = True
    while tr:
        if part:
            print("                                                                                        ")
            print("                                    Wprowadz hasło: ", end=' ')
            key = input()
            if len(key) < 3:
                print('                              |     Nieprawidłowe hasło - min - trzy znaki')
            else:
                tr = False
        else:
            print("                                                                                        ")
            print("                                    Wprowadz ponownie hasło: ", end=' ')
            key = input()
            if len(key) < 3:
                print('                              |     Nieprawidłowe hasło - min - trzy znaki')
            else:
                tr = False
    return key


def Logon():
    print("\n\n\n\n")
    print("")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("        ▒                                                                                                ▒")
    print('        ▒        1                               - %+55s' % ('TWORZENIE I EDYCJA HASEŁ DOSTEPOWYCH ▒',))
    print('        ▒                                                                                                ▒')
    print('        ▒                                                                                                ▒')
    print("        ▒                                                                                                ▒")
    print("        ▒                                                                                                ▒")
    print("        ▒                                                                                                ▒")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("")
    print("                             ████████████████████████████████████████████████████████")
    print("                             █                                                      █")
    print("                             █                                                      █")
    print('                                 %+35s ' % ('WPROWADZ HASŁO GŁÓWNE :',), end="")
    key = input()
    print("                             █______________________________________________________█")
    print("                             ████████████████████████████████████████████████████████")
    time.sleep(0.5)
    os.system("cls")
    return key


def SaveKey():
    print("")
    print("                             ████████████████████████████████████████████████████████")
    print("                             █                                                      █")
    print("                             █                 HASŁO ZOSTAŁO ZAPISANE               █")
    print("                             █                                                      █")
    print("                             ████████████████████████████████████████████████████████")
    print("")
    time.sleep(3)
    os.system("cls")


def operationSuccess():
    print("")
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █                    OPERACJA POWIODŁA SIĘ                  █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(3)
    os.system("cls")


def errorFile():
    print("")
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █                 BŁĄD DZIAŁANIA NA PLIKACH                 █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(3)
    os.system("cls")


def ERROR():
    print("")
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █                  BŁĄD KRYTYCZNY APLIKACJI                 █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(3)
    os.system("cls")


def ErrorKey():
    print("")
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █                  Hasła nie są równe sobie                 █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(3)
    os.system("cls")


def ErrorPaswd():
    print("\n\n\n\n\n")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("        ▒                                                                                                ▒")
    print('        ▒                ███████████████████████████████████████████████████████  YCJA HASEŁ DOSTEPOWYCH ▒')
    print("        ▒                █                                                     █                         ▒")
    print("        ▒                █               LOGOWANIE NIE POWIODŁO SIĘ            █                         ▒")
    print("        ▒                █                                                     █                         ▒")
    print("        ▒                ███████████████████████████████████████████████████████                         ▒")
    print('        ▒                                                                                                ▒')
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("")
    print("")
    time.sleep(3)
    os.system("cls")


def Access():
    print("\n\n\n\n\n")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("        ▒                                                                                                ▒")
    print('        ▒                ███████████████████████████████████████████████████████  YCJA HASEŁ DOSTEPOWYCH ▒')
    print('        ▒                █                                                     █                         ▒')
    print('        ▒                █                 Logowanie powiodło się!             █                         ▒')
    print("        ▒                █                                                     █                         ▒")
    print("        ▒                ███████████████████████████████████████████████████████                         ▒")
    print('        ▒                                                                                                ▒')
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("")
    time.sleep(2)
    os.system("cls")


def delAccept():
    print("")
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █                  POPRAWNIE USUNIĘTO WPIS                  █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(5)


def delFailure():
    print("")
    print("                           █████████████████████████████████████████████████████████████")
    print("                           █                                                           █")
    print('                           █             USUNIĘCIE WPISU NIE POWIODŁO SIE              █')
    print("                           █                                                           █")
    print("                           █████████████████████████████████████████████████████████████")
    time.sleep(2)


def LookingForPosition(pozycjeLookFor_):
    k = 0
    while len(pozycjeLookFor_) > k:
        if int(pozycjeLookFor_[k]) == position:
            return False
        k += 1
    return True


def Editor(fileName, sizeGen, encrypt):
    global position
    T = True
    while T:
        pozycjeLookFor = ""
        file = open(fileName, "r")
        temps = file.readlines()
        file.close()
        ListTemp = []
        i = 1
        lines = temp = temps[0].replace("\n", "")
        lines = lines.split(" ")

        while i < len(temps):
            temp = temps[i].replace("\n", "")
            temp = temp.split(" ")
            ListTemp.append(temp)

            i += 1
        print("")
        List = ListTemp
        print(
            "                                                                            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(
            "                                                                            ▒  a  ▒  DODAJ NOWE HASŁO      ▒")
        print(
            "                                                                            ▒  e  ▒  EDYTUJ HASŁO          ▒")
        print(
            "                                                                            ▒  d  ▒  USUŃ HASŁO            ▒")
        print(
            "                                                                            ▒ del ▒  USUŃ WSZYSTKIE HASŁA  ▒")
        print(
            "                                                                            ▒  q  ▒  WYJSCIE               ▒")
        print(
            "                                                                            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "        █                                      ZAPISANE HASŁA W BAZIE                                      █")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "        █ POZYCJA NR █               NAZWA                  █                    HASŁO                     █")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        i = 0
        if len(List) == 0:
            print(
                "        █                                                                                                  █")
            print(
                "        █                                   BRAK POZYCJI DO WYŚWIETLENIA                                   █")
            print(
                "        █                                                                                                  █")
        while i < len(List):
            pozycjeLookFor += List[i][0] + " "
            if encrypt:
                tempss = List[i][2]
            print("        █ {0:11s}".format(str(List[i][0])) + "█ {0:37s}".format(List[i][1]) + "█ {0:45s}".format(
                scriptedOut(List[i][2], lines[1])) + "█")
            i += 1
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("")
        print('    %+80s' % ('Wprowadz znak komendy:  ',), end="")
        command = input()

        if command != "a" and command != "e" and command != "d" and command != "del" and command != "q":
            print("")
            print("                           █████████████████████████████████████████████████████████████")
            print("                           █                                                           █")
            print('                           █                  Nieprawidłowa komenda                    █')
            print('                           █   Prosze wybrać znak z listy  - a,  e,  d,  del lub  q    █')
            print("                           █                                                           █")
            print("                           █████████████████████████████████████████████████████████████")
            time.sleep(3)
        else:
            if command != "q" and command != "del" and command != "a":
                print('    %+80s' % ('Wprowadz numer hasła:   ',), end="")
                position = input()
                try:
                    position = int(position)
                    pozycjeLookFor_ = pozycjeLookFor.split(" ")
                    if LookingForPosition(pozycjeLookFor_):
                        print("")
                        print(
                            "                           █████████████████████████████████████████████████████████████")
                        print(
                            "                           █                                                           █")
                        print(
                            "                           █         WPISANY NUMER NIE ZNAJDUJE SIE NA LIŚCIE          █")
                        print("                           █              %+20s" % (pozycjeLookFor) + "              █")
                        print(
                            "                           █                                                           █")
                        print(
                            "                           █████████████████████████████████████████████████████████████")
                        command = "ll"
                        time.sleep(3)
                except:
                    command = "error"
                    print("")
                    print("                           █████████████████████████████████████████████████████████████")
                    print("                           █                                                           █")
                    print('                           █                    NIEPRAWIDŁOWY ZNAK                     █')
                    print('                           █               PROSZE PODAĆ LICZBĘ DODATNIĄ                █')
                    print("                           █                                                           █")
                    print("                           █████████████████████████████████████████████████████████████")
                    time.sleep(1)

        if command == "q":
            os.system("cls")
            break
        else:
            if command == "a":
                os.system("cls")
                addNewPassword(List, fileName, sizeGen)
                os.system("cls")
            else:
                if command == "e":
                    os.system("cls")
                    editPassword(fileName, position, sizeGen)
                    os.system("cls")
                else:
                    if command == "d":
                        if AcceptDel():
                            if removePassword(position, fileName):
                                delAccept()
                            else:
                                delFailure()
                        os.system("cls")
                    else:
                        if command == "del":
                            if AcceptDel():
                                removeAllPassword(fileName)
                        else:
                            position = 0
                        os.system("cls")


def munuEditPassword(fileName, List, position, sizeKey):
    lose = True
    while lose:
        os.system("cls")
        print("")
        print(
            "                                                                            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(
            "                                                                            ▒  1  ▒  EDYCJA POZYCJI        ▒")
        print(
            "                                                                            ▒  2  ▒  EDYCJA NAZWY          ▒")
        print(
            "                                                                            ▒  3  ▒  EDYCJA HASŁA (manual) ▒")
        print(
            "                                                                            ▒  4  ▒  ZMIANA HASŁA (auto)   ▒")
        print(
            "                                                                            ▒  q  ▒  WYJSCIE               ▒")
        print(
            "                                                                            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "        █                                      EDYTOR WPISOW HASEŁ                                         █")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "        █ POZYCJA NR █               NAZWA                  █                    HASŁO                     █")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        i = 1
        positionList = 0
        while i < len(List):
            if int(int(List[i][0])) == int(position):
                print("        █  {0:8s}".format(str(List[i][0])) + "  █  {0:36s}".format(
                    List[i][1]) + "█  {0:44s}".format(scriptedOut(List[i][2], List[0][1])) + "█")
                positionList = i
            i += 1
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("")
        print("                                                     Proszę podać komende: ", end="")
        p = input()

        if p == "1":
            print("                                                     Proszę podać pozycje : ", end="")
            pp = input()
            if len(pp) == 0:
                print("")
                print("                           █████████████████████████████████████████████████████████████")
                print("                           █                                                           █")
                print('                           █             TEN OBSZAR NIE MOZE BYĆ PUSTY                 █')
                print("                           █                                                           █")
                print("                           █████████████████████████████████████████████████████████████")
                time.sleep(2)
                os.system("cls")
            else:
                liczba = False
                i = 0
                try:
                    position = int(pp)
                    liczba = True
                    List[positionList][0] = pp
                except:
                    print("")
                    print("                           █████████████████████████████████████████████████████████████")
                    print("                           █                                                           █")
                    print('                           █                    NIEPRAWIDŁOWY ZNAK                     █')
                    print('                           █               PROSZE PODAĆ LICZBĘ DODATNIĄ                █')
                    print("                           █                                                           █")
                    print("                           █████████████████████████████████████████████████████████████")
                    time.sleep(1)
            liczba = False


        else:
            if p == "2":
                print("                                                     Proszę podać nazwe : ", end="")
                pp = input()
                if len(pp) == 0:
                    print("")
                    print("                           █████████████████████████████████████████████████████████████")
                    print("                           █                                                           █")
                    print('                           █             TEN OBSZAR NIE MOZE BYĆ PUSTY                 █')
                    print("                           █                                                           █")
                    print("                           █████████████████████████████████████████████████████████████")
                    time.sleep(2)
                    os.system("cls")
                else:
                    liczba = False
                    List[positionList][1] = pp
                    os.system("cls")
            else:
                if p == "3":
                    print("                                                     Proszę podać hasło : ", end="")
                    pp = input()
                    liczba = False
                    i = 0
                    if len(pp) == 0:
                        print("")
                        print(
                            "                           █████████████████████████████████████████████████████████████")
                        print(
                            "                           █                                                           █")
                        print(
                            '                           █             TEN OBSZAR NIE MOZE BYĆ PUSTY                 █')
                        print(
                            "                           █                                                           █")
                        print(
                            "                           █████████████████████████████████████████████████████████████")
                        time.sleep(2)
                        os.system("cls")
                        liczba = False
                    else:
                        pp = scriptedIn(pp, List[0][1])
                        List[positionList][2] = pp[0]
                else:
                    if p == "q":
                        lose = False
                        os.system("cls")
                    else:
                        if p == "4":
                            List[int(positionList)][2] = genPassword(int(sizeKey))
                            os.system("cls")
                        else:
                            print("")
                            print(
                                "                           █████████████████████████████████████████████████████████████")
                            print(
                                "                           █                                                           █")
                            print(
                                '                           █                    Nieprawidłowy znak                     █')
                            print(
                                '                           █      Prosze wybrać znak z listy  - a,  b,  c lub  q       █')
                            print(
                                "                           █                                                           █")
                            print(
                                "                           █████████████████████████████████████████████████████████████")
                            time.sleep(2)
                            os.system("cls")
                            time.sleep(3)

        i = 1
        file = open(fileName, "w+")
        file.write(List[0][0] + " " + List[0][1])
        while i < len(List):
            file.write("\n" + List[i][0] + " " + List[i][1] + " " + List[i][2])
            position = List[positionList][0]
            i += 1

        file.close()


def addNewPassword(List, fileName, sizeKey):
    T = True
    poz = "0"
    name = ""
    key = "none"
    while T:
        print("")
        print(
            "                                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print(
            "                                                              ▒  0   ▒  EDYCJA NAZWY                      ▒")
        print(
            "                                                              ▒  1   ▒  WPROWADZ POZYCJE                  ▒")
        print(
            "                                                              ▒  2   ▒  WYGENERUJ HASŁO AuTOMATYCZNIE     ▒")
        print(
            "                                                              ▒  3   ▒  WPROWADZ HASŁO MANUALNIE          ▒")
        print(
            "                                                              ▒  4   ▒  WPROWADZ ILOSC ZNAKOW HASŁO AUTOM ▒")
        print(
            "                                                              ▒ save ▒  ZAPISZ                            ▒")
        print(
            "                                                              ▒  q   ▒  WYJSCIE                           ▒")
        print(
            "                                                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print(
            "        █                                              USTAWIENIA                                          █")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("        █  Numer pozycji                            █  {0:52s}".format(poz) + "█")
        print("        █  Nazwa                                    █  {0:52s}".format(name) + "█")
        print("        █  Ilosc znakow w hasle                     █  {0:52s}".format(str(sizeKey)) + "█")
        print("        █  Hasło                                    █  {0:52s}".format(key) + "█")
        print(
            "        █                                           █                                                      █")
        print(
            "        ████████████████████████████████████████████████████████████████████████████████████████████████████")
        print("")
        print("                                                        Wprowadz komende : ", end="")
        comand = input()
        if comand == "0":
            print("                                                        Wprowadz nazwe : ", end="")
            ok = input()
            if len(ok) < 37:
                name = ok
            else:
                print(
                    "                                                        Nazwa nie moze zawierac wiecej niz 36 znaków")
                time.sleep(3)
        else:
            if comand == "1":
                print("                                                        Wprowadz pozycje : ", end="")
                poz = input()
                try:
                    int(poz)
                    j = 0
                    while j < len(List):
                        if str(poz) == List[j][0]:
                            print("                                                        Pozycja " + str(
                                j) + "  jest juz zajęta")
                            time.sleep(3)
                            j = len(List)
                        j += 1
                    while j < len(List):
                        if int(poz) == j:
                            print("                                                        Pozycja   " + str(
                                j) + " jest juz zajęta")
                            time.sleep(3)
                except ValueError:
                    print("                                                        Podany znak nie jest liczba")
                    time.sleep(3)

            else:
                if comand == "2":
                    if int(sizeKey) > 0:
                        key = genPassword(sizeKey)
                    else:
                        print("")
                        print(
                            "                           █████████████████████████████████████████████████████████████")
                        print(
                            "                           █                                                           █")
                        print(
                            '                           █                   Nieprawidłowa liczba                    █')
                        print(
                            "                           █                                                           █")
                        print(
                            "                           █████████████████████████████████████████████████████████████")
                        time.sleep(3)

                else:
                    if comand == "3":
                        print("                                                        Wprowadz hasło : ", end="")
                        ok = input()
                        if len(ok) < 49:
                            key = ok
                        else:
                            print(
                                "                                                        Hasło nie moze zawierac wiecej niz 49 znaków")
                            time.sleep(3)
                    else:
                        if comand == "4":
                            print("                                                        Wprowadz liczbe: ", end="")
                            sizeKey = input()
                            try:
                                int(sizeKey)
                            except ValueError:
                                print(
                                    "                                                        Podany znak nie jest liczba")
                                time.sleep(3)

                        else:
                            if comand == "q":
                                T = False
                            else:
                                if comand == "save":
                                    if name != "" and poz != 0:
                                        file = open(fileName, "r")
                                        temps = file.readlines()
                                        file.close()
                                        ListTemp = []
                                        i = 0
                                        temp = []
                                        while i < len(temps):
                                            temp = temps[i].replace("\n", "")
                                            temp = temp.split(" ")
                                            ListTemp.append(temp)
                                            i += 1
                                        key = scriptedIn(key, ListTemp[0][1])
                                        Lista = [poz, name, key[0]]
                                        ListTemp.append(Lista)
                                        i = 1
                                        file = open(fileName, "w+")
                                        file.write(ListTemp[0][0] + " " + ListTemp[0][1])
                                        while i < len(ListTemp):
                                            file.write(
                                                "\n" + str(ListTemp[i][0]) + " " + str(ListTemp[i][1]) + " " + str(
                                                    ListTemp[i][2]))
                                            i += 1
                                        file.close()
                                        T = False
                                        SaveKey()
                                    else:
                                        if name == "":
                                            print(
                                                "                                                        Nazwa nie może być pusta")
                                            time.sleep(1)
                                        if int(poz) == 0:
                                            print(
                                                "                                                        Pozycja nie moze być 0")
                                            time.sleep(5)
                                else:
                                    print("                                                        NIEZNANA KOMENDA")
                                    time.sleep(3)

        os.system("cls")


def rys():
    print("")
    print("                                                              ██████")
    print("                                                            ██▓▓▓▓▓▓██")
    print("                                                          ██▓▓▓▓▒▒▒▒██")
    print("                                                          ██▓▓▒▒▒▒▒▒██")
    print("                                                        ██▓▓▓▓▒▒▒▒██")
    print("                                                        ██▓▓▒▒▒▒▒▒██")
    print("                                                      ██▓▓▓▓▒▒▒▒▒▒██")
    print("                                                      ████▒▒████▒▒██")
    print("                                                      ██▓▓▒▒▒▒▒▒▒▒██")
    print("                                                    ██    ▒▒    ▒▒██")
    print("                                                    ████  ▒▒██  ▒▒██")
    print("                                                    ██    ▒▒    ▒▒██")
    print("                                                    ██▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("                                                    ████████████▒▒▒▒██")
    print("                                                  ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("                                                ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██")
    print("                                              ██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
    print("                                            ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
    print("                                          ██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██")
    print("                                          ██▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██")
    print("                                          ██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██")
    print("                                            ████▐▌▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌▐▌████")
    print("                                              ██▐▌▐▌▌▌▌▌▌▌▌▌▐▌▐▌▐▌▐▌▌▌▐▌██")
    print("                                              ██▌▌▐▌▐▌▌▌▐▌▌▌▌▌▐▌▌▌▌▌▌▌▌▌██")
    print("                                                ██▌▌▐▌▐▌▐▌▐▌▐▌▐▌▐▌▌▌▌▌██")
    print("                                                ██▐▌▐▌▐▌████████▐▌▌▌▌▌██")
    print("                                                  ██▒▒██        ██▒▒██")
    print("                                                  ██████        ██████")
    time.sleep(3)
    os.system("cls")


def AcceptDel():
    print('    %+91s' % ('Potwierdz usunięcie wpisu (y/n):   ',), end="")
    y = input()
    if y == "y":
        return 1
    return 0
