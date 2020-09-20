from time import sleep
import os, platform, random, pygame, thorpy
def Pause():
    if platform.system()=="Windows":
        os.system("pause")
    else:
        sleep(10)
        print("for a better experience or to have acces to help please run this program in a Windows environement.")
instpygameeng, instpygamefr, instthorpy= """REM sets the color to background black, writing green\ncolor 0A\nREM hides C:\... and just shows the required text\necho off\nREM if your volume name is D it will go to D:\\ncd D:\\nREM if your volume name is  C it will not go to D:\ but to C:\\ncd C:\\nREM clears screen\ncls\nREM code mark, goes to it if asked in the code\n:choice\necho If the shell shows the message "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x04A394D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/pygame/"\necho try to run the program with admin writes or make sure you have an active connection.\nREM question\necho Do you whant to install pygame? [(y)es/(n)o/(U)update]:\nREM variable to remember youre choice\nset /p choice=\nREM instructions\nif %choice%==y goto i\nREM instructions\nif %choice%==Y goto i\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM instructions\nif %choice%==u goto m\nREM instructions\nif %choice%==U goto m\nREM error message\necho Please make sure you've entered either "y" for yes or "n" for no or "u" for update.\nREM instructions\ngoto choice\nREM code mark, goes to it if asked in the code\n:i\nREM text\necho Installing...:\nREM shows C:\....\necho on\nREM first try to install pygame\npy -m pip install -U pygame --user\nREM hides C:\... and just shows the required text\necho off\nREM testing to see if pygame is installed\necho keys to lay the game:\necho    - space to shoot\necho    - right arrow to go right\necho    - left arrow to go left\nREM we pause the code until a key is hit\npause\nREM we start pygame\npy -m pygame.examples.aliens\nREM text\necho Pygame has succefully been installed on your computer.\nREM code mark, goes to it if asked in the code\n:q\nREM question\necho Do you whant to update pygame? [(Y)es/(N)o]:\nset /p choice=\nREM instructions\nif %choice%==y goto m\nREM instructions\nif %choice%==Y goto m\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM error message\necho Please make sure you've entered either "y" for yes or "n" for no.\nREM instruction\ngoto q\nREM code mark, goes to it if asked in the code\n:m\nREM shows C:\....\necho on\nREM line of code to update pygame\npy -m pip install -U pygame --user\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM testing to see if pygame is installed\necho keys to lay the game:\necho    - space to shoot\necho    - right arrow to go right\necho    - left arrow to go left\nREM we pause the code until a key is hit\npause\nREM we start pygame\npy -m pygame.examples.aliens\nREM hides C:\... and just shows the required text\necho off\nREM Text\necho Pygame has been updated on youre computer.\nREM instructions\ngoto n\nREM code mark, goes to it if asked in the code\n:n\nREM text\necho Goodbye.\nREM text\necho created by Henry Letellier\nREM text\necho " ._____. "\nREM text\necho " |.   .| "\nREM text\necho " |  |  | "\nREM text\necho " |\___/| "\nREM text\necho " |_____| "\nREM sleep time\ntimeout 3\nREM we pause the code until a key is hit\npause\nREM we pause the code until a key is hit\npause""", """REM met la couleur à écriture verte sur fond noir\ncolor 0A\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM si votre disque dure se nome D il ira dedans\ncd D:\\nREM si votre disque dure se nome C il ira dans ce dernier et pas dans D\ncd C:\\nREM netoie l'écran\ncls\nREM première balise\n:choice\necho si l'invite des comandes vous affiche "WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x04A394D0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed')': /simple/pygame/"\necho Essayez d'‚x‚cuter l'invite des comandes en mode administrateur ou d'activer votre wifi\nREM question\necho Voulez-vous installer pygame? [(o)ui/(n)on/(m)ettre a jour]:\nREM variable pour récupérer votre choix\nset /p choice=\nREM instructions\nif %choice%==o goto i\nREM instructions\nif %choice%==O goto i\nREM instructions\nif %choice%==0 goto i\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM instructions\nif %choice%==m goto m\nREM instructions\nif %choice%==M goto m\nREM message d'erreur\necho Veuillez n'entrer que la lettre "o" ou la lettre "n" ou la lettre "m".\nREM instructions\ngoto choice\nREM balise\n:i\nREM texte\necho Installation:\nREM affiche C:\....\necho on\nREM première tentative d'installation\npy -m pip install -U pygame --user\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM test pour voir si pygame est installé\necho commandes pour jouer:\necho    - touche espace pour tirer\necho    - fleche droite pour aller a droite\necho    - fleche gauche pour aller a gauche\nREM on met la commande en pause\npause\nREM on va lancer le jeux pygame\npy -m pygame.examples.aliens\nREM texte\necho pygame a ‚t‚ install‚ sur votre ordinateur.\nREM balise\n:q\nREM question\necho Voulez-vous mettre a jour pygame [(o)ui/(n)on]:\nset /p choice=\nREM instructions\nif %choice%==o goto m\nREM instructions\nif %choice%==O goto m\nREM instructions\nif %choice%==0 goto m\nREM instructions\nif %choice%==n goto n\nREM instructions\nif %choice%==N goto n\nREM message d'erreur\necho Veuillez n'entrer que la lettre "o" ou la lettre "n".\nREM instructions\ngoto q\nREM balise\n:m\nREM affiche C:\....\necho on\nREM ligne de code pour mettre a jour pip\npy -m pip install -U pygame --user\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM test pour voir si pygame est installé\necho commandes pour jouer:\necho    - touche espace pour tirer\necho    - fleche droite pour aller a droite\necho    - fleche gauche pour aller a gauche\nREM on met la commande en pause\npause\nREM on va lancer le jeux pygame\npy -m pygame.examples.aliens\nREM n'affiche pas C:\... mais juste la comande\necho off\nREM Texte\necho pygame a ‚t‚ mis a jour sur votre ordinateur.\nREM instructions\ngoto n\nREM balise\n:n\nREM texte\necho Au revoir\nREM texte\necho cr‚‚ par Henry Letellier\nREM texte\necho " ._____. "\nREM texte\necho " |.   .| "\nREM texte\necho " |  |  | "\nREM texte\necho " |\___/| "\nREM texte\necho " |_____| "\nREM temp de pause\ntimeout 3\nREM met l'invite en pause\npause\nREM met l'invite en pause\npause ""","""color 0A\necho off\ncls\n:choice\necho Do you want to install Thorpy? [(y)es/(n)o]:\nset /p choice=\nif %choice%==y goto y\nif %choice%==Y goto y\nif %choice%==n goto n\nif %choice%==N goto n\necho please enter 'y' for yes or 'n' for no.\npause\ngoto choice\n:y\ntitle installing...\necho installing...\necho on\npip install thorpy\necho off\npause\ngoto n\n:n\necho created by Henry Letellier\necho " ._____. "\necho " |.   .| "\necho " |  |  | "\necho " |\___/| "\necho " |_____| "\ntimeout 3\npause\npause"""
application = thorpy.Application((500,500), "Launching alerts")
def my_alert_1():
    print("English")
    global language
    language="eng"
def my_alert_2():
    print("Français")
    global language
    language="fr"
def my_launch():
    print("Quitter le jeux/quit game")
    global contiinue
    contiinue="q"
text4 = thorpy.make_text("Set the language/Choisissez votre langue", 15, (0,0,255))

boxfr=thorpy.make_ok_cancel_box([thorpy.make_button("Vous avez défini la langue au Français")],ok_text="Ok")
boxeng=thorpy.make_ok_cancel_box([thorpy.make_button("You've set the language to English")],ok_text="Ok")
au_revoir=thorpy.make_ok_cancel_box([thorpy.make_button("Goodbye/Au revoir")],ok_text="Ok")

application = thorpy.Application((190,150), "Language selection/sélection de la langue")
button1 = thorpy.make_button("English",my_alert_1)
button2 = thorpy.make_button("Français",my_alert_2)
button3 = thorpy.make_button("Quit Game/Quitter le Jeux",my_launch)
thorpy.set_launcher(button1, my_alert_1, click_quit=True)
thorpy.set_launcher(button2, my_alert_2, click_quit=True)
button3.set_as_exiter()
thorpy.set_launcher(button1, boxfr)#, click_quit=True)
thorpy.set_launcher(button2, boxeng)#, click_quit=True)
thorpy.set_launcher(button3, au_revoir)#, click_quit=True)
background=thorpy.Background(elements=[text4,button1,button2,button3])
background.set_main_color((220,220,220,180))
thorpy.store(background, x=10, y=10, align="left")
menu = thorpy.Menu(background)
menu.play()
if my_alert_1=="eng":
    print("englais")
elif my_alert_2=="fr":
    print("français")
elif my_launch=="q":
    print("quit")
launched.add_reaction(reac_clickquit)
application.quit()


#thorpy.makeup.add_basic_help(draggable,"Draggable:\nYou can drag it.")
#central_box.set_main_color((220,220,220,180))
