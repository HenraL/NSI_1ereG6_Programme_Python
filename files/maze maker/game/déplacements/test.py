import codecs, os, tkinter, sys
from msvcrt import getch, kbhit
from time import sleep
while True:
    if kbhit():
        final="======================== Début de la touche ========================\n"
        z=getch()
        code=ord(z)
        final+="{} =".format(z)
        final+="{}\n".format(code)
        final+="========================  Fin de la touche  ========================\n"
        print(final)