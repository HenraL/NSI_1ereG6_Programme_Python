from tkinter import *
#from tkinter import ttk
#href: http://s15847115.domainepardefaut.fr/python/tkinter/fenetre_disposition_grid.html
#def popup():
    #fInfos = Toplevel()		  # Popup -> Toplevel()
    #fInfos.title('Infos')
    #Button(fInfos, text='Quitter', command=fInfos.destroy).pack(padx=10, pady=10)
    #fInfos.transient(jeu) 	  # Réduction popup impossible 
    #fInfos.grab_set()		  # Interaction avec fenetre jeu impossible
    #jeu.wait_window(fInfos)   # Arrêt script principal

#jeu = Tk()					  # Fenêtre principale -> Tk()
#jeu.title('Fenêtre principale')
#jeu.geometry('300x100')
#Button(jeu, text='Ouvrir popup', command=popup).pack(padx=10, pady=10)

#jeu.mainloop()				  # Uniquement pour la fenêtre principale

#, command=popup
jeu=Tk()
jeu.title("Temps écoulé")
jeu.geometry("3000x100")
Button(jeu, text="Ok", command=jeu.destroy).pack(padx=10, pady=10)
