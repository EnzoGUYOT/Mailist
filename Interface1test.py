from tkinter import *
import os.path
import os
import re
import requests

def checkExistFile(fileName, fenetre):
    # Chemin du fichier
    my_file = "/Users/enzoguyot/Desktop/"+fileName

    if os.path.exists(my_file):
        fenetre.destroy()
        windows1(Lire(my_file))
    else:
        fenetre.destroy()
        windows1(Ecrire(my_file, ""))


def Ecrire(fichier,mail):
    with open(fichier, 'a+') as fichier:
        fichier.write(mail)
def Lire(fichier):
    listmail = list()
    with open(fichier, 'r') as fichier:
        for line in fichier:
            listmail.append(line)
    return listmail

def importCSV ():
    global cheminCsv
    with open (cheminCsv.get (), 'r') as fichier:
        contenu = fichier.read()
    fichier.close ()
    analyse (contenu)

    return

def importURL ():
    global urlPage
    contenu = requests.get(urlPage.get ()).text
    analyse (contenu)

    return

def ValidMail(mail):
    if ('@' in mail) and (mail.endswith(".com") or mail.endswith(".fr")) and PingNasa (RecuperationDomaine (mail)):
        return True
    else:
        return False

def RecuperationDomaine(mail):
    return re.split(r"@", mail)[1]

def PingNasa(hostname):
    print("ping ", hostname)
    retour = os.system ("ping -c 1 "+ hostname)
    if retour == 0:
        return True
    else:
        return False

def analyse (chaine):
    global liste
    global addresses

    # extraction adresses mail
    result = re.findall (r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', chaine)

    # ajout à la liste globale
    for address in list(set(result)):
        print ("check ", address)
        if ValidMail (address):
             addresses.append (address)

    # filtrage doublons
    addresses = list (set (addresses))

    # tri alpha
    addresses.sort ()

    print (addresses)

    # mise à jour listbox
    liste.delete (0, "end")
    for adr in addresses:
        liste.insert ("end", adr)

    return

def envoyerEmails ():
    global addresses

    return

def windows1 (salutlesfrites):
    global cheminCsv
    global urlPage
    global liste

    fenetre = Tk ()

    # titre
    label = Label (fenetre, text = "Nom de la campagne", fg = 'red')
    x = StringVar ()
    entree = Entry (fenetre, textvariable = x)

    # liste
    label = Label (fenetre, text = "Adresses")
    liste = Listbox (fenetre)

    # bouton csv
    cheminCsv = StringVar()
    cheminCsv.set ("/Users/enzoguyot/Desktop/antennesindisponibles.csv")
    champCsv = Entry (fenetre, textvariable = cheminCsv)
    boutonCsv = Button (fenetre, text="Import CSV", command=importCSV)

    # bouton url
    urlPage = StringVar()
    urlPage.set ("https://univcergy.phpnet.org/python/mail.html")
    champUrl = Entry (fenetre, textvariable = urlPage)
    boutonUrl = Button (fenetre, text="Import URL", command=importURL)

    # bouton mail
    boutonMail = Button (fenetre, text="Envoyer emails", command=envoyerEmails)

    # bouton quitter
    boutonQuitter = Button (fenetre, text="Quitter", command=fenetre.quit)

    # magie
    label.pack ()
    entree.pack ()
    liste.pack ()
    boutonMail.pack ()
    champCsv.pack ()
    boutonCsv.pack ()
    champUrl.pack ()
    boutonUrl.pack ()
    boutonQuitter.pack ()

    return fenetre

def windows2 ():
    global cheminCsv
    global urlPage
    global liste

    fenetre = Tk ()

    # titre
    label = Label (fenetre, text = "Nom de la campagne", fg = 'red')
    x = StringVar ()
    entree = Entry (fenetre, textvariable = x)
    # bouton mail
    boutoncree = Button(fenetre, text="Crée la compagne", command=lambda:checkExistFile(entree.get(),fenetre))

    # bouton quitter
    boutonQuitter = Button (fenetre, text="Quitter", command=fenetre.quit)

    # magie
    label.pack ()
    entree.pack ()
    boutoncree.pack()
    boutonQuitter.pack ()

    return fenetre

global addresses
addresses = []
fenetre=windows2()
fenetre.mainloop ()