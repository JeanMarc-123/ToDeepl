# -*- coding: utf-8 -*-
"""
@author: JeanMarc
"""

import pyperclip
import tkinter

class Interface(tkinter.Frame):
    """Classe contentant la fenêtre principale.
    Toutes les widgets sont contenu dans cette frame"""
    
    def __init__(self, fenetre, **kwargs):
        """Fonction permettant de définir nos widget (et même ici de les mettre en application)"""
        tkinter.Frame.__init__(self, fenetre, width = 758, height = 300, **kwargs)
        self.pack(fill = "both")
        
        #Création des widgets
        self.message = tkinter.Label(self, text = "Aucun traitement effectué")
        self.message.pack()
        
        self.boutton_cliquer = tkinter.Button(self, text = "PDF to Deepl", fg = "red", command = self.cliquer)
        self.boutton_cliquer.pack()
        
    def cliquer(self):
        """Fonction appelée par boutton_cliqer (widget) pour changer le texte du dessus de la fenêtre"""
        self.message["text"] = """En cours de traitement ..."""
        
        text = pyperclip.paste()

        phrase = ""
        text = text.split(sep = "\r\n")
        
        for elem in text:
            phrase += elem + " "
        
        pyperclip.copy(phrase)
        
        self.message["text"] = """Traitement terminé"""
        
        

fenetre = tkinter.Tk()
fenetre.title("ToDeepl")
fenetre.geometry("250x50")
fenetre.iconbitmap("icone.ico")
interface = Interface(fenetre)

interface.mainloop()
