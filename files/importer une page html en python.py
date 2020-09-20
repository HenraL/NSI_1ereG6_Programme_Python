#py -3 -m pip install beautifulsoup4
#pip3 install beautifulsoup4
try:
    pip install bs4 requests
    import os
    import csv
    import requests
    from bs4 import BeautifulSoup
otherwise:
    choice=input("Avez-vous installé bs4? [(o)ui/(n)on]")
    if choice=="o" or choice=="O":
        print("tentez de le réinstallé ou vérifiez qu'il est bien au bon emplacement")
    elif choice=="n" or choice=="N":
        print("mercie de bien vouloir le faire en éxécutant le fichier inst_bs4_w.bat pour windows, inst_bs4_m.d pour mac et inst_bs4_l.f pour linux")
    else:
        print("Vous avez rentré {}\nÊtes-vous sûre d'avoir entré 'n' pour non ou 'o' pour oui?".format(choice))
        continue
requete = requests.get("https://zestedesavoir.com/tutoriels/?category=autres-informatique")
page = requete.content
soup = BeautifulSoup(page)
#import urllib
#sock = urllib.urlopen("https://python.developpez.com/cours/DiveIntoPython/php/frdiveintopython/html_processing/extracting_data.php")
#phpSource = sock.read()
#sock.close()
#print (htmlSource)                   
#http://bit.ly/2NZnvYU
