from time import sleep
import os, platform, random, pygame, thorpy
def Pause():
    if platform.system()=="Windows":
        os.system("pause")
    else:
        sleep(10)
        print("for a better experience or to have acces to help please run this program in a Windows environement.")
instpygameeng, instpygamefr, instthorpy= """REM sets the color to background black, writing green\ncolor 0A\nREM hides C:\... and just shows the required text\necho off\nREM if your volume name is D it will go to D:\\ncd D:\\nREM if your volume name is  C it will not go to D:\ but to C:\\ncd C:\\nREM clears screen\ncls\nREM code mark, goes to it if asked in the code\n:choice\necho If the shell shows the message "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x04A394D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/pygame/"\necho try to run the program with admin writes or make sure you have an active connection.\nREM question\necho Do you whant to install pygame? [(y)es/(n)o/(U)update]:\nREM variable to remember youre choice\nset /p choice=\nREM instructions\nif %choice%==y goto i\nREM instructions\nif %choice%==Y goto i\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM instructions\nif %choice%==u goto m\nREM instructions\nif %choice%==U goto m\nREM error message\necho Please make sure you've entered either "y" for yes or "n" for no or "u" for update.\nREM instructions\ngoto choice\nREM code mark, goes to it if asked in the code\n:i\nREM text\necho Installing...:\nREM shows C:\....\necho on\nREM first try to install pygame\npy -m pip install -U pygame --user\nREM hides C:\... and just shows the required text\necho off\nREM testing to see if pygame is installed\necho keys to lay the game:\necho    - space to shoot\necho    - right arrow to go right\necho    - left arrow to go left\nREM we pause the code until a key is hit\npause\nREM we start pygame\npy -m pygame.examples.aliens\nREM text\necho Pygame has succefully been installed on your computer.\nREM code mark, goes to it if asked in the code\n:q\nREM question\necho Do you whant to update pygame? [(Y)es/(N)o]:\nset /p choice=\nREM instructions\nif %choice%==y goto m\nREM instructions\nif %choice%==Y goto m\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM error message\necho Please make sure you've entered either "y" for yes or "n" for no.\nREM instruction\ngoto q\nREM code mark, goes to it if asked in the code\n:m\nREM shows C:\....\necho on\nREM line of code to update pygame\npy -m pip install -U pygame --user\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM testing to see if pygame is installed\necho keys to lay the game:\necho    - space to shoot\necho    - right arrow to go right\necho    - left arrow to go left\nREM we pause the code until a key is hit\npause\nREM we start pygame\npy -m pygame.examples.aliens\nREM hides C:\... and just shows the required text\necho off\nREM Text\necho Pygame has been updated on youre computer.\nREM instructions\ngoto n\nREM code mark, goes to it if asked in the code\n:n\nREM text\necho Goodbye.\nREM text\necho created by Henry Letellier\nREM text\necho " ._____. "\nREM text\necho " |.   .| "\nREM text\necho " |  |  | "\nREM text\necho " |\___/| "\nREM text\necho " |_____| "\nREM sleep time\ntimeout 3\nREM we pause the code until a key is hit\npause\nREM we pause the code until a key is hit\npause""", """REM met la couleur à écriture verte sur fond noir\ncolor 0A\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM si votre disque dure se nome D il ira dedans\ncd D:\\nREM si votre disque dure se nome C il ira dans ce dernier et pas dans D\ncd C:\\nREM netoie l'écran\ncls\nREM première balise\n:choice\necho si l'invite des comandes vous affiche "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x04A394D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/pygame/"\necho Essayez d'‚x‚cuter l'invite des comandes en mode administrateur ou d'activer votre wifi\nREM question\necho Voulez-vous installer pygame? [(o)ui/(n)on/(m)ettre a jour]:\nREM variable pour récupérer votre choix\nset /p choice=\nREM instructions\nif %choice%==o goto i\nREM instructions\nif %choice%==O goto i\nREM instructions\nif %choice%==0 goto i\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM instructions\nif %choice%==m goto m\nREM instructions\nif %choice%==M goto m\nREM message d'erreur\necho Veuillez n'entrer que la lettre "o" ou la lettre "n" ou la lettre "m".\nREM instructions\ngoto choice\nREM balise\n:i\nREM texte\necho Installation:\nREM affiche C:\....\necho on\nREM première tentative d'installation\npy -m pip install -U pygame --user\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM test pour voir si pygame est installé\necho commandes pour jouer:\necho    - touche espace pour tirer\necho    - fleche droite pour aller a droite\necho    - fleche gauche pour aller a gauche\nREM on met la commande en pause\npause\nREM on va lancer le jeux pygame\npy -m pygame.examples.aliens\nREM texte\necho pygame a ‚t‚ install‚ sur votre ordinateur.\nREM balise\n:q\nREM question\necho Voulez-vous mettre a jour pygame [(o)ui/(n)on]:\nset /p choice=\nREM instructions\nif %choice%==o goto m\nREM instructions\nif %choice%==O goto m\nREM instructions\nif %choice%==0 goto m\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM message d'erreur\necho Veuillez n'entrer que la lettre "o" ou la lettre "n".\nREM instructions\ngoto q\nREM balise\n:m\nREM affiche C:\....\necho on\nREM ligne de code pour mettre a jour pip\npy -m pip install -U pygame --user\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM test pour voir si pygame est installé\necho commandes pour jouer:\necho    - touche espace pour tirer\necho    - fleche droite pour aller a droite\necho    - fleche gauche pour aller a gauche\nREM on met la commande en pause\npause\nREM on va lancer le jeux pygame\npy -m pygame.examples.aliens\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM Texte\necho pygame a ‚t‚ mis a jour sur votre ordinateur.\nREM instructions\ngoto n\nREM balise\n:n\nREM texte\necho Au revoir\nREM texte\necho cr‚‚ par Henry Letellier\nREM texte\necho " ._____. "\nREM texte\necho " |.   .| "\nREM texte\necho " |  |  | "\nREM texte\necho " |\___/| "\nREM texte\necho " |_____| "\nREM temp de pause\ntimeout 3\nREM met l'invite en pause\npause\nREM met l'invite en pause\npause ""","""color 0A\necho off\ncls\n:choice\necho Do you want to install Thorpy? [(y)es/(n)o]:\nset /p choice=\nif %choice%==y goto y\nif %choice%==Y goto y\nif %choice%==n goto n\nif %choice%==N goto n\necho please enter 'y' for yes or 'n' for no.\npause\ngoto choice\n:y\ntitle installing...\necho installing...\necho on\npip install thorpy\necho off\npause\ngoto n\n:n\necho created by Henry Letellier\necho " ._____. "\necho " |.   .| "\necho " |  |  | "\necho " |\___/| "\necho " |_____| "\ntimeout 3\npause\npause"""
# try:
#     import pygame
#     try:
#         import thorpy
#     except:
#         print("please install pip: a program to install it is avaidable here: http://bit.ly/38fvsSC \nThen run the file 'install_thorpy.bat'")
#         Pause()
#         f=open("install_thorpy.bat", "w")
#         s=f.write(instthorpy)
#         f.close()
#         print("A file named 'install_thorpy.bat' or 'install_thorpy' has been created in the same folder thet the program is. Please run it with admin whrigts once that the pip help has been installed.")
# except:
#     print ("Please install pygame to be able to run the program, with admin writghts, for windows you can run the program inst_pygame_eng.bat for the english version and inst_pygame_fr.bat for the french version.")
#     f=open("inst_pygame_eng.bat", "w")
#     s=f.write(instpygameeng)
#     f.close()
#     f=open("inst_pygame_fr.bat", "w")
#     s=f.write(instpygamefr)
#     f.close()
#     print("A file named 'inst_pygame_eng.bat' or 'inst_pygame_eng' and 'inst_pygame_fr.bat' or 'inst_pygame_fr' has been created in the same folder than the program is. Please run it with admin whrigts to be able to install pygame.")

#background = thorpy.Background(color=(255,255,255)) #color of the menu
#menu = thorpy.Menu(background) #color of the menu:
#menu.play() #color of the menu
def my_choices_1():
    some_element = thorpy.make_text("Choisissez votre langue.", font_size=18)
    Français=thorpy.make_button("Français")
    English=thorpy.make_button("English")
#    language = [("English","eng"), ("Français","fr")]
    another_element = thorpy.make_button("Quit")
    box = thorpy.Box.make([some_element, Français, English, another_element])
    thorpy.set_as_done_button(another_element,box)#could be set_as_cancel_button
    thorpy.launch_blocking(box)
application = thorpy.Application(size=(600, 400), caption="Questions d'Histoire")
button1 = thorpy.make_button("Non-blocking version", func=my_choices_1)
#if language==1:language="eng"
#elif language==2:language="fr"
if my_choices_1()=="eng":
    print("eng")
elif my_choices_1()=="fr":
    print("fr")
# languageeng=thorpy.Application(size=(300, 300), caption="English")
# languagefr=thorpy.Application(size=(300, 300), caption="Français")
