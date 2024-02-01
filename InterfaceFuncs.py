from tkinter import *
from tkinter import ttk,messagebox
from Classes import *
from Functions import *
from datetime import *
import time
import secrets
import os
import webbrowser


file_Admini="AuthAdministration.csv"
file_Prof="AuthProfs.csv"
file_Etu="AuthEtudiant.csv"

def MenuPrincipale(fen,frame=None):
    if frame:
        frame.destroy()
    LogFrame=Frame(fen)
    LogFrame.pack()
    MsgLog=Label(LogFrame, text="S'authentifier en tant que  :",font="Times 24 bold italic",  fg="#22B9A8")
    MsgLog.pack(pady=10)
    optionsLog=["Administration","Enseignant","Etudiant"]
    for i in range(len(optionsLog)):
        if i==1:
            bg="#1199B7"
        else:
            bg="#22B9A8"
        BT = Button(LogFrame, text=optionsLog[i].upper(), font="times 20 bold ", fg="white", bg=bg,width=25,
                    command= lambda a=i : OperationLog(fen, LogFrame, optionsLog[a]))
        BT.pack(pady=10)
    Exit = Button(LogFrame, text="Quitter", font="times 20 bold ", fg="white", bg="#ffa245",width=15,
                    command= exit, border=0)
    Exit.pack(pady=25)

def OperationLog(fen, FM, opt):
    FM.destroy()
    if opt == "Administration":
        afficherFrameConnexion(fen, opt)
    elif opt == "Enseignant":
        afficherFrameConnexion(fen, opt)
    else:
        afficherFrameConnexion(fen, opt)

def afficherFrameConnexion(fen, opt,frame=None):
    if frame:
        frame.destroy()
    frameLogin = Frame(fen, padx=5, pady=5)
    frameLogin.pack(pady=10)
    labelMsg=Label(frameLogin, text="Merci de vous connecter ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=2)
    if opt=="Etudiant":
        formLogin(frameLogin,fen,opt)
        
        labeInsc = Label(frameLogin, text=" Déposer votre candidature : ", font="Bahnschrift 16 bold", fg="#22B9A8",width=30)
        labeInsc.grid(row=6, column=0,columnspan=2, pady=5)
        
        Inscrir = Button(frameLogin, text="Candidature ", font="times 16 bold", width=34 ,fg="white", bg="#22B9A8",command= lambda : inscrptionFrame(frameLogin,fen,opt))
        Inscrir.grid(row=7, column=0, columnspan=2, pady=5)
    else:
        formLogin(frameLogin,fen,opt)
        
        
def formLogin(frameLogin,fen,user):
    global entUser, entPass
    labeUser = Label(frameLogin, text="Nom d'utilisateur : ", font="Times 12")
    labeUser.grid(row=1, column=0, pady=5, sticky=NW)
    
    entUser = Entry(frameLogin,font="times 20 ", width=30, border=0)
    entUser.grid(row=2, column=0,columnspan=2,pady=5, sticky=NW)
    
    labePass = Label(frameLogin, text="Mot de passe : ", font="Times 12")
    labePass.grid(row=3, column=0, pady=5, sticky=NW)
    
    entPass = Entry(frameLogin,font="times 20 ", width=30, border=0, show="*")
    entPass.grid(row=4, column=0,columnspan=2, pady=5, sticky=NW)
    
    annuler = Button(frameLogin, text="Annuler", font="times 16 bold",width=15 , fg="white", bg="#ffa245",command=lambda : MenuPrincipale(fen,frameLogin))
    annuler.grid(row=5, column=0,pady=5)
    
    connex = Button(frameLogin, text="Connexion", font="times 16 bold", width=15 ,fg="white", bg="#22B9A8", command=lambda : Connexion(fen,frameLogin,user))
    connex.grid(row=5, column=1, pady=5)
    
def inscrptionFrame(frame,fen,opt):
    global entCIN,entNom,entPrenom,entNotBac,entJrNai,entMsNai,entAnNai,entFil,frameInsc
    frame.destroy()
    frameInsc=Frame(fen)
    frameInsc.pack()
    labelMsg=Label(frameInsc, text="Inscription !", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    labeCIN = Label(frameInsc, text="CIN : ", font="Times 12")
    labeCIN.grid(row=1, column=0, pady=3, sticky=NW)
    
    entCIN = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entCIN.grid(row=2, column=0,columnspan=3,pady=3, sticky=NW)
    
    labeNom = Label(frameInsc, text="Nom : ", font="Times 12")
    labeNom.grid(row=3, column=0,columnspan=3, pady=3, sticky=NW)
    
    entNom = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entNom.grid(row=4, column=0,columnspan=3, pady=3, sticky=NW)
    
    labePrenom = Label(frameInsc, text="Prénom : ", font="Times 12")
    labePrenom.grid(row=5, column=0,columnspan=3, pady=3, sticky=NW)
    
    entPrenom = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entPrenom.grid(row=6, column=0,columnspan=3, pady=3, sticky=NW)
    
    labeNotBac = Label(frameInsc, text="La note du Baccalauréat: ", font="Times 12")
    labeNotBac.grid(row=7, column=0,columnspan=3, pady=3, sticky=NW)
    
    entNotBac = Entry(frameInsc,font="times 20 ", width=30, border=0)
    entNotBac.grid(row=8, column=0,columnspan=3, pady=3, sticky=NW)
    
    labeDateNai = Label(frameInsc, text="Date de naissance (jj/mm/aaaa) : ", font="Times 12")
    labeDateNai.grid(row=9, column=0,columnspan=3, pady=3, sticky=NW)
    
    entJrNai = Entry(frameInsc,font="times 20 ", width=9, border=0)
    entJrNai.grid(row=10, column=0, pady=3, sticky=NW)
    
    entMsNai = Entry(frameInsc,font="times 20 ", width=9, border=0)
    entMsNai.grid(row=10, column=1, padx=5, pady=3, sticky=NSEW)
    
    entAnNai = Entry(frameInsc,font="times 20 ", width=9, border=0)
    entAnNai.grid(row=10, column=2, pady=3, sticky=SE)
    
    labeFil = Label(frameInsc, text="Choisissez une option : ", font="Times 12")
    labeFil.grid(row=11, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFil=ttk.Combobox(frameInsc,width=30,font="times 20 ",values=FiliersValide())
    entFil.grid(row=12, column=0, columnspan=3, pady=3, sticky=NSEW)
    
    Inscrir = Button(frameInsc, text="Se candidater", font="times 16 bold", width=36 ,fg="white", bg="#22B9A8", command=lambda:Inscription(fen))
    Inscrir.grid(row=13, column=0, columnspan=3, pady=5)
    
    Annuler = Button(frameInsc, text="Annuler", font="times 16 bold", width=36 ,fg="white", bg="#ffa245", command=lambda:afficherFrameConnexion(fen, opt,frameInsc))
    Annuler.grid(row=14, column=0, columnspan=3, pady=5)

###################
def FiliersValide():
    fils=[]
    for fil in ListOption:
        fils.append(fil.Nom)
    return fils

###################
def ErrDate(min,max,val):
    try: 
        Age=int(val)
        if int(Age) > max or int(Age)< min:
            messagebox.showerror("Erreur","Date Entrée invalide !")
        else:
            return int(Age)
    except (ValueError):
            messagebox.showerror("Erreur","Saisir un nombre")

def ErrInt(val):
    try: 
        INT=int(val) 
        return int(INT)
    except (ValueError):
            messagebox.showerror("Erreur","Saisir un nombre")

def ErrNote(val):
    try: 
        Not=float(val)
        if float(Not) > 20 or float(Not)< 0:
            messagebox.showerror("Erreur","Note entrée invalide !")
        else:
            return float(Not)
    except (ValueError):
            messagebox.showinfo("Attention","Saisir un nombre")
###################

def Inscription(fen):
    L=[entCIN,entNom,entPrenom,entNotBac,entJrNai,entMsNai,entAnNai,entFil]
    for i in L:
        if i.get()=="":
            messagebox.showinfo("Attention","Veuillez remplir tous les champs")
            return 
    jj=ErrDate(1,31,entJrNai.get())
    mm=ErrDate(1,12,entMsNai.get())
    aa=ErrDate(1900,2023,entAnNai.get())
    if jj and mm and aa and ErrNote(entNotBac.get()):
        DN=date(aa,mm,jj)
        if not VerifierAge(DN,DA):
            messagebox.showinfo("Attention","Vous ne pouvez pas s'inscrire ")
            MenuPrincipale(fen,frameInsc)
        else:
            CIN=entCIN.get().upper()
            if ExisteEtudiant(ListEtu, CIN ) or ExisteEtudiant(List_Attend, CIN ):
                messagebox.showerror("Erreur","Un étudiant avec cette CIN existe déjà")
                return 
            Nom=entNom.get().title()
            Prenom=entPrenom.get().title()
            NotBac=ErrNote(entNotBac.get())
            if NotBac>=10:
                for fil in ListOption:
                    if fil.Nom == entFil.get():
                        id_fil=fil.getid()
                        break
                List_Attend.append(Etudiant(CIN,id_fil,Nom,Prenom,DN,ListOption,NotBac))
                messagebox.showinfo("Attention","Vous êtes inscrits avec succés  \n Merci d'attendre la confirmation.")
                MenuPrincipale(fen,frameInsc)
            else:
                messagebox.showerror("Erreur","La note entrée est invalide")

def Connexion(fen,frame,user):
    global UtlActuel
    # "or" for a while 
    if user == "Administration" and confirmeUtl(entUser.get(),entPass.get(),file_Admini):
        UtlActuel=entUser.get().upper()
        frame.destroy()
        fenAdmini(fen)
    elif user == "Enseignant" and confirmeUtl(entUser.get().upper(),entPass.get(),file_Prof):
        UtlActuel=entUser.get().upper()
        frame.destroy()
        fenFrmtr(fen)
    elif user == "Etudiant" and confirmeUtl(entUser.get().upper(),entPass.get(),file_Etu):
        UtlActuel=entUser.get().upper() 
        frame.destroy()
        fenEtu(fen)
    else:
        messagebox.showerror("Erreur","Nom d'utilisateur ou mot de passe  invalide !")
        entPass.delete(0,END)
        entPass.focus()

def fenAdmini(fen,frame=None):
    if frame :
        frame.destroy()
    frameAdmini = Frame(fen, padx=5, pady=5)
    frameAdmini.pack(pady=10)
    MsgLog=Label(frameAdmini, text="ADMINISTRATION", font="Times 24 bold italic" ,fg = "#22B9A8")
    MsgLog.grid(row=0,column=0,columnspan=3)
    optionsD = [
        "Ajouter une option",
        "Ajouter un étudiant",
        "Ajouter un enseignant",
        "Afficher les étudiants",
        "Afficher les enseignants",
        "Supprimer un étudiant",
        "Supprimer un enseignant",
        "Calculer les notes",
        "Exporter les données",
        "Importer les données",
        "Afficher Absences",
        "Déconnexion"
    ]
    n = 1
    for i in range(len(optionsD)):
        if i == len(optionsD)-1:
            button = Button(frameAdmini, text=optionsD[i].upper(), font="times 12 bold ", fg="white", bg="#ffa245",width=25,command=lambda: MenuPrincipale(fen,frameAdmini))
            button.grid(row=n, column=i % 3 , columnspan=2, padx=5, pady=10)
        else:
            button = Button(frameAdmini, text=optionsD[i].upper(), font="times 12 bold ", fg="white", bg="#22B9A8",width=25,
                            command=lambda a=i: OperationD(fen, frameAdmini, optionsD[a]))
            button.grid(row=n, column=i % 3 , padx=5, pady=10)
        if i % 3 == 2:
            n = n + 1



def OperationD(fen, fdr, x):
    fdr.destroy()
    framOperAdmi = Frame(fen, padx=5, pady=5)
    framOperAdmi.pack(pady=10)
    if x == "Ajouter une option":
        AjouFilFrame(fen,framOperAdmi)
    elif x =="Ajouter un étudiant":
        ValiderEtudiant(fen, framOperAdmi)
    elif x =="Ajouter un enseignant":
        AjouFormFrame(fen,framOperAdmi)
    elif x =="Afficher les étudiants":
        afficherListeEtudiants(fen,framOperAdmi)
    elif x =="Afficher les enseignants":
        afficherListeProfesseurs(fen,framOperAdmi)
    elif x =="Supprimer un étudiant":
        frameDeSupprission(fen,framOperAdmi,x)
    elif x =="Supprimer un enseignant":
        frameDeSupprission(fen,framOperAdmi,x)
    elif x =="Calculer les notes":
        Calcule(fen)
    elif x =="Exporter les données":
        Exportation(fen,framOperAdmi)
    elif x =="Importer les données":
        Importation(fen,framOperAdmi)
    elif x =="Afficher Absences":
        AfficherAbsancesAdmin(fen, framOperAdmi)

#######################################
# Les frames et les operations de l'Administration 

def AjouFilFrame(fen,frame):
    global entNomFil,entAbbr,entNomMod1,entNomMod2,entNomMod3,entCoef1,entCoef2,entCoef3
    labelMsg=Label(frame, text="Ajouter une option !".upper(), font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid( row=0,column=0, columnspan=4)
    
    labeNomFil = Label(frame, text="Nom d'option : ", font="Times 12")
    labeNomFil.grid(row=1, column=0, pady=5, sticky=NW)
    
    entNomFil = Entry(frame,font="times 20 ", width=30, border=0)
    entNomFil.grid(row=2, column=1,columnspan=3,pady=5, sticky=NW)
    
    labeAbbr = Label(frame, text="Abréviation : ", font="Times 12")
    labeAbbr.grid(row=3, column=0, pady=5, sticky=NW)
    
    entAbbr = Entry(frame,font="times 20 ", width=30, border=0)
    entAbbr.grid(row=4, column=1,columnspan=3, pady=5, sticky=NW)
    
    labelMsg=Label(frame, text="Ajouter les modules de cette option !".upper(), font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=5, column=0,  columnspan=4,pady=10)
    
    for i in range(3):
        labeNomMod = Label(frame, text=f"Module {i+1}:", font="Times 12")
        labeNomMod.grid(row=i+6, column=0, pady=10, sticky=NW)
        
        labeCoef = Label(frame, text="Coef :", font="Times 12")
        labeCoef.grid(row=i+6, column=2, pady=10, sticky=NW)
    # ***************
    entNomMod1 = Entry(frame,font="times 14 ", width=30)
    entNomMod1.grid(row=6, column=1,pady=10, sticky=NW)
    entCoef1 = Entry(frame,font="times 14 ", width=10 )
    entCoef1.grid(row=6, column=3,pady=10, sticky=NW)
    # ***************
    entNomMod2 = Entry(frame,font="times 14 ", width=30)
    entNomMod2.grid(row=7, column=1,pady=10, sticky=NW)
    entCoef2 = Entry(frame,font="times 14 ", width=10 )
    entCoef2.grid(row=7, column=3,pady=10, sticky=NW)
    # ***************
    entNomMod3 = Entry(frame,font="times 14 ", width=30)
    entNomMod3.grid(row=8, column=1,pady=10, sticky=NW)
    entCoef3 = Entry(frame,font="times 14 ", width=10 )
    entCoef3.grid(row=8, column=3,pady=10, sticky=NW)
    
    ajouFil = Button(frame, text="Ajouter", font="times 16 bold", width=20 ,fg="white", bg="#22B9A8",command= lambda : AjoutFil(frame,fen))
    ajouFil.grid(row=9, column=0, columnspan=2, pady=5)
    annuler = Button(frame, text="Annuler", font="times 16 bold",width=20 , fg="white", bg="#ffa245",command=lambda : fenAdmini(fen,frame))
    annuler.grid(row=9, column=2,pady=5,columnspan=2)

def AjoutFil(frame,fen):
    champs=[entNomFil,entAbbr,entNomMod1,entNomMod2,entNomMod3,entCoef1,entCoef2,entCoef3]
    for cham in champs:
        if cham.get()=="":
            messagebox.showinfo("Attention","Veuillez remplir tous les champs !!")
            return 
    nom = entNomFil.get().title()
    if ExisteOptien(nom):
        messagebox.showerror("Erreur","Cette option existe déjà.")
        return
    abbr = entAbbr.get().upper()
    F = Option(nom, abbr)
    idFil = F.getid()
    Noms = [entNomMod1.get(), entNomMod2.get(), entNomMod3.get()]
    
    coef1,coef2,coef3=entCoef1.get(),entCoef2.get(),entCoef3.get()
    if ErrInt(coef1) and ErrInt(coef2) and ErrInt(coef3):
        Coefs = [coef1,coef2,coef3]
        listMods = []
        for i in range(3):
            mod = Module(Noms[i].title(), idFil, Coefs[i])
            listMods.append(mod)
            ToutsModules.append(mod)
            
        F.ListModules = listMods
        ListOption.append(F) 
        messagebox.showinfo("Parfait", " Option ajoutée avec succès !!")
        frame.destroy()
        fenAdmini(fen)
    else :
        return

########################################
def PrintEtudiant(obj):
    return StrSpaces(obj.Nom,18) + StrSpaces(obj.Prenom,20) + StrSpaces(str(obj.BacNote),16) + StrSpaces(obj.NomFil(),30)
entete=StrSpaces("Nom",18) + StrSpaces("Prenom",20) + StrSpaces("Note Bac",16) + StrSpaces("Option",30)

def ValiderEtudiant(fen, frame):
    global EtuLables, AcceptBtns, RefuBtns
    frame.pack()
    if List_Attend == []:
        messagebox.showerror("Erreur", "La liste d'attente est vide")
        fenAdmini(fen,frame)
    else:
        if len(ListEtu) <= 50:
            List_Attend.sort(key=getnote, reverse=True)
            n = 0
            EtuLables = []
            AcceptBtns = []
            RefuBtns = []
            annuler = Button(frame, text="Retour", font="times 14 bold",width=10 , fg="white", bg="#ffa245",command=lambda : fenAdmini(fen,frame))
            annuler.grid(row=0, column=0,pady=5,sticky="W")
            
            EntetLabl = Label(frame,text=entete, font="times 14",width=56,bg="white")
            EntetLabl.grid(row=1, column=0,columnspan=4,sticky="W")
            
            EntetLabl = Label(frame,text="Actions", font="times 14",width=20, bg="white")
            EntetLabl.grid(row=1, column=4,columnspan=2)
            for stg in List_Attend:
                if n%2==0:
                    bg="#faf4ee"
                else:
                    bg="#f2e4d7"
                frame.pack(padx=5, pady=5) 
                EtuLabel = Label(frame, text=PrintEtudiant(stg),font="times 14 ", bg=bg, width=56, pady=5)
                EtuLabel.grid(row=n+2, column=0, columnspan=4, pady=2,sticky="W")
                EtuLables.append(EtuLabel)
                
                accept_button = Button(frame, text="Accepter",font="times 12 bold ", fg="white", bg="#22B9A8",width=10,
                                    command=lambda s=stg, index=n: AccepterEtudiant(s, index))
                accept_button.grid(row=n+2, column=4,padx=5, pady=5)
                AcceptBtns.append(accept_button)
                
                reject_button = Button(frame, text="Refuser",font="times 12 bold ", fg="white", bg="#ffa245",width=10,
                                    command=lambda s=stg, index=n: RefuserEtudiant(s, index))
                reject_button.grid(row=n+2, column=5, pady=5)
                RefuBtns.append(reject_button)
                n += 1
                
def AccepterEtudiant(stg, index):
    ListEtu.append(stg)
    yesno=messagebox.askyesno("Confirme",f"Êtes-vous sûr de vouloir accepter {stg.Nom} {stg.Prenom} ?")
    if yesno:
        file = file_Etu
        with open(file, 'a') as f:
            Pass = secrets.token_hex(5)
            f.write(f"{stg.CIN},{Pass}\n")
        List_Attend.remove(stg)
        EtuLables[index].grid_forget()
        AcceptBtns[index].grid_forget()
        RefuBtns[index].grid_forget()
    else:
        return

def RefuserEtudiant(stg, index):
    yesno=messagebox.askyesno("Confirme",f"Êtes-vous sûr de vouloir refuser  {stg.Nom} {stg.Prenom} ?")
    if yesno:
        List_Attend.remove(stg)
        EtuLables[index].grid_forget()
        AcceptBtns[index].grid_forget()
        RefuBtns[index].grid_forget()
    else:
        return 
########################################
def RecupereNomModules(Liste):
    NomModules=[]
    for m in Liste:
        NomModules.append(m.Nom)
    return NomModules
########################################
def AjouFormFrame(fen,frame):
    global entFrmCIN,entFrmNom,entFrmPrenom,entFrmAnNai,entFrmMsNai,entFrmJrNai , listBoxMods
    labelMsg=Label(frame, text="Ajout d'un Enseignant", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    labeFrmCIN = Label(frame, text="C I N : ", font="Times 12")
    labeFrmCIN.grid(row=1, column=0, pady=3, sticky=NW)
    
    entFrmCIN = Entry(frame,font="times 20 ", width=30, border=0)
    entFrmCIN.grid(row=2, column=0,columnspan=3,pady=3, sticky=NW)
    
    labeFrmNom = Label(frame, text="Nom : ", font="Times 12")
    labeFrmNom.grid(row=3, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFrmNom = Entry(frame,font="times 20 ", width=30, border=0)
    entFrmNom.grid(row=4, column=0,columnspan=3, pady=3, sticky=NW)
    
    labeFrmPrenom = Label(frame, text="Prénom : ", font="Times 12")
    labeFrmPrenom.grid(row=5, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFrmPrenom = Entry(frame,font="times 20 ", width=30, border=0)
    entFrmPrenom.grid(row=6, column=0,columnspan=3, pady=3, sticky=NW)

    labeFrmDateNai = Label(frame, text="Date de naissance (jj/mm/aaaa) : ", font="Times 12")
    labeFrmDateNai.grid(row=7, column=0,columnspan=3, pady=3, sticky=NW)
    
    entFrmJrNai = Entry(frame,font="times 20 ", width=9, border=0)
    entFrmJrNai.grid(row=8, column=0, pady=3, sticky=NW)
    
    entFrmMsNai = Entry(frame,font="times 20 ", width=9, border=0)
    entFrmMsNai.grid(row=8, column=1, padx=5, pady=3, sticky=NSEW)
    
    entFrmAnNai = Entry(frame,font="times 20 ", width=9, border=0)
    entFrmAnNai.grid(row=8, column=2, pady=3, sticky=SE)
    
    labelMods = Label(frame, text="Choisissez le(s) module(s) que le prof enseignera:", font="Times 12")
    labelMods.grid(row=9, column=0, columnspan=2, padx=5, pady=5)
    listBoxMods = Listbox(frame, selectmode=MULTIPLE, height=3, width=25)
    listBoxMods.grid(row=9, column=2, pady=3)

    for module in RecupereNomModules(ToutsModules):
        listBoxMods.insert(END, module)
    
    Inscrir = Button(frame, text="Ajouter", font="times 16 bold", width=36 ,fg="white", bg="#22B9A8", command=lambda:AjoutProf())
    Inscrir.grid(row=11, column=0, columnspan=3, pady=5)
    
    Annuler = Button(frame, text="Annuler", font="times 16 bold", width=36 ,fg="white", bg="#ffa245", command=lambda:fenAdmini(fen,frame))
    Annuler.grid(row=12, column=0, columnspan=3, pady=5)
########################################
def AjoutProf():
    L =[ entFrmCIN, entFrmNom, entFrmPrenom, entFrmAnNai, entFrmMsNai, entFrmJrNai]
    for i in L:
        if i.get()=="":
            messagebox.showinfo("Attention","Merci de remplir tous les champs ")
            return 
    CinFrmtr=entFrmCIN.get().upper()
    if ExisteProf(CinFrmtr):
        messagebox.showerror("Erreur", "Le prof existe déjà")
        return
    
    NF=entFrmNom.get().title()
    PF=entFrmPrenom.get().title()
    if ErrDate(1,31,entFrmJrNai.get()) and ErrDate(1,12,entFrmMsNai.get()) and ErrDate(1900,2023,entFrmAnNai.get()):
        jj=ErrDate(1,31,entFrmJrNai.get())
        mm=ErrDate(1,12,entFrmMsNai.get())
        aa=ErrDate(1900,2023,entFrmAnNai.get())
        
        DNF=date(aa,mm,jj)
        Form=Professeur(CinFrmtr,NF,PF,DNF)
        
        selectedMods= listBoxMods.curselection()
        if len(selectedMods)>3:
            messagebox.showerror("Erreur", "Sélectionnez trois modules au max !")
        else:
            listModFrmtr=[]
            for mod in ToutsModules:
                for index in selectedMods:
                    if mod.Nom==listBoxMods.get(index):
                        mod.CINFrmtr=CinFrmtr
                        listModFrmtr.append(mod)
            Form.Modules=listModFrmtr
            ListFrmtr.append(Form)
            file = file_Prof
            with open(file, 'a') as f:
                Pass = secrets.token_hex(5)
                f.write(f"{CinFrmtr},{Pass}\n")
            f.close()
            messagebox.showinfo("info", f"{NF} {PF} est bien ajouté")
    else :
        return
########################################

def afficherListeEtudiants(fen, frame):
    Annuler = Button(frame, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenAdmini(fen,frame))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(frame, text="La liste des étudiants ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("CIN","Nom","Prenom","Date de Naissaance","Note de Bac","Option ")
    CodeC=('cin','nom','Prenom','Date de Naissaance','Note de Bac','Option ')
    TM=ttk.Treeview(frame,columns=CodeC,show='headings')
    for i in range(6):
        TM.column(CodeC[i],width=120,anchor='center')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
    for i in range(len(ListEtu)):
        TM.insert('','end',values=(f'{ListEtu[i].CIN}',f'{ListEtu[i].Nom}',f'{ListEtu[i].Prenom}',f'{ListEtu[i].DateNai}',f'{ListEtu[i].BacNote}',f'{ListEtu[i].NomFil()}'))
########################################
def afficherListeProfesseurs(fen, frame):
    Annuler = Button(frame, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenAdmini(fen,frame))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(frame, text="La liste des professeurs ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("CIN","Nom","Prenom","Date de Naissaance","Modules")
    CodeC=('cin','nom','Prenom','Date de Naissaance','Modules')
    TM=ttk.Treeview(frame,columns=CodeC,show='headings')
    for i in range(5):
        TM.column(CodeC[i],width=150,anchor='center')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
    for i in range(len(ListFrmtr)):
        TM.insert('','end',values=(f'{ListFrmtr[i].CIN}',f'{ListFrmtr[i].Nom}',f'{ListFrmtr[i].Prenom}',f'{ListFrmtr[i].DateNai}',f'{ListFrmtr[i].AfficheNomMods()}'))
        
########################################
# supression 
def frameDeSupprission(fen,frame,x):
    global entCinSup
    if x == "Supprimer un étudiant":
        msg="Etudiant"
    else:
        msg="Profeseur"

    labelMsg=Label(frame, text=f"Supression d'un {msg} !!", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)

    labelCIN = Label(frame, text=f"Entrez le CIN de {msg} à supprimer: ", font="Times 12")
    labelCIN.grid(row=1, column=0, pady=5, sticky=NW)
    
    entCinSup = Entry(frame,font="times 20 ", width=30, border=0)
    entCinSup.grid(row=2, column=0,columnspan=3,pady=15, sticky=NW)

    Supp = Button(frame, text="Supprimer", font="times 16 bold", width=36 ,fg="white", bg="#22B9A8", command= lambda: Supprimer(x))
    Supp.grid(row=11, column=0, columnspan=3, pady=5)
    
    Retour = Button(frame, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#ffa245", command=lambda:fenAdmini(fen,frame))
    Retour.grid(row=12, column=0, columnspan=3, pady=5)

def Supprimer(x):
    
    if entCinSup.get()=="" :
        messagebox.showerror("Erreur","Veuillez choisir un code")
    else:
        C=entCinSup.get().upper()
        if x == "Supprimer un étudiant":
            if not ExisteEtudiant(ListEtu,C):
                messagebox.showerror("Erreur","Aucun étudiant avec ce CIN !")
            else:
                for stg in ListEtu:
                    if stg.CIN==C:
                        yesno=messagebox.askyesno("Confirmation",f"Êtes-vous sûr de vouloir supprimer {stg.Nom} {stg.Prenom}?")
                        if yesno:
                            ListEtu.remove(stg)
                            messagebox.showinfo("Confirmation","L'étudiant à été supprimé")
                        else :
                            return
        else:
            if not ExisteProf(C):
                messagebox.showerror("Erreur","Aucun professeur avec ce CIN !")
            else:
                for frmtr in ListFrmtr:
                    if frmtr.CIN==C:
                        yesno=messagebox.askyesno("Confirmation",f"Êtes-vous sûr de vouloir supprimer {frmtr.Nom} {frmtr.Prenom} ?")
                        if yesno:
                            ListEtu.remove(frmtr)
                            messagebox.showinfo("Confirmation","Le professeur à été supprimé")
                        else :
                            return

########################################
def Calcule(fen):
    if ListeNotes ==[]:
        messagebox.showerror("Non disponible","Les note sont pas encore disponibles !")
    else:
        for etu in ListEtu:
            CalculeNotes(etu.CIN)
        messagebox.showinfo("Operation terminé","Toutes les notes sont calculés avec succès")
    fenAdmini(fen)
########################################


def Importation(fen,frame):
    labelMsg=Label(frame, text="Importation des données ...", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    image = PhotoImage(file="img/transfering.gif")
    label =Label(frame, image=image)
    label.grid(row=2,column=0, pady=10)
    
    progress = ttk.Progressbar(frame, length=300)
    progress.grid(row=1,column=0, pady=10)
    
    def MiseAJourProgress(count, total):
        progress['value'] = (count / total) * 100
        frame.update_idletasks()
        frame.update()
        time.sleep(1)
    
    count = 0
    total = 6

    with open("Data/Options.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 2:
                N, Abr = info[0], info[1]
                ListOption.append(Option(N, Abr))
    
    count += 1
    MiseAJourProgress(count, total)
    with open("Data/Modules.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 4:
                N, idfil, Coeff, CinF = info[0], info[1], info[2], info[3]
                ToutsModules.append(Module(N, int(idfil), int(Coeff), CinF))
                
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/Etudiants.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                ListEtu.append(Etudiant(C, int(idF), N, P, DN, ListOption, BN))
    
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/Notes.csv","r") as Notesfile:
        for line in Notesfile:
            info = line.strip().split(",")
            if len(info) == 5:
                idM,Cstg,C1,C2,EFM= info[0],info[1],info[2],info[3],info[4]
                ListeNotes.append(Note(int(idM),Cstg,float(C1),float(C2),float(EFM)))
    
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/EtudiantsEnAttent.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                List_Attend.append(Etudiant(C, int(idF), N, P, DN, ListOption, float(BN)))
    
    count += 1
    MiseAJourProgress(count, total)
    
    with open("Data/Professeurs.csv","r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 5:
                C,N,P= info[0],info[1],info[2]
                DN = ImportDate(info[3])
                NomMods=info[4].strip().split("-")
                NomMods = list(filter(lambda x: x != "", NomMods))
                listMods=[]
                for nom in NomMods:
                    mod=retModByName(nom.strip())
                    if mod.CINFrmtr == C:
                        listMods.append(mod)
                ListFrmtr.append(Professeur(C,N,P,DN,listMods))
        
    
    count += 1
    MiseAJourProgress(count, total)
    with open("Data/Absances.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 2:
              date_absence = datetime.strptime(info[2], '%Y-%m-%d').date()
            ListeAbsences.append(Absence(info[0], int(info[1]), date_absence))
    count += 1
    MiseAJourProgress(count, total)
    
    messagebox.showinfo("Importatation Terminé","Toutes les données ont été importés avec succès")
    
    fenAdmini(fen,frame)


def Exportation(fen, frame):

    labelMsg=Label(frame, text="Exportation des Données ...", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    image = PhotoImage(file="img/transfering.gif")
    label =Label(frame, image=image)
    label.grid(row=2,column=0, pady=10)
    
    total = 6 
    count = 0 
    progress = ttk.Progressbar(frame, length=300)
    progress.grid(row=1,column=0, pady=10)

    def ExportProgress():
        nonlocal count
        count += 1
        progress['value'] = (count / total) * 100
        frame.update_idletasks()
        time.sleep(1)


    File_filieres = open("Data/Filieres.csv", "a")
    FilWriter = csv.writer(File_filieres, delimiter=",")
    for fil in ListOption:
        FilWriter.writerow([fil.Nom, fil.Abr])
    File_filieres.close()
    ExportProgress()

    File_Modules = open("Data/Modules.csv", "a")
    ModWriter = csv.writer(File_Modules, delimiter=",")
    for mod in ToutsModules:
        ModWriter.writerow([ mod.Nom, mod.id_fil, mod.Coeff, mod.CINFrmtr])
    File_Modules.close()
    ExportProgress()

    file_Etu = open("Data/Etudiants.csv", "a")
    EtuWriter = csv.writer(file_Etu, delimiter=",")
    for etu in ListEtu:
        EtuWriter.writerow([etu.CIN, etu.Nom, etu.Prenom, etu.DateNai, etu.idFil, etu.BacNote])
    file_Etu.close()
    ExportProgress()

    EtuAttent = open("Data/EtudiantsEnAttent.csv", "a")
    StgWriter = csv.writer(EtuAttent, delimiter=",")
    for stg in List_Attend:
        StgWriter.writerow([stg.CIN, stg.Nom, stg.Prenom, stg.DateNai, stg.idFil, stg.BacNote])
    EtuAttent.close()
    ExportProgress()

    file_Prof = open("Data/Professeurs.csv", "a")
    FrmtWriter = csv.writer(file_Prof, delimiter=",")
    for frmtr in ListFrmtr:
        FrmtWriter.writerow([frmtr.CIN, frmtr.Nom, frmtr.Prenom, frmtr.DateNai,frmtr.AfficheNomMods()])
    file_Prof.close()
    ExportProgress()

    File_Notes = open("Data/Notes.csv", "a")
    NoteWriter = csv.writer(File_Notes, delimiter=",")
    for note in ListeNotes:
        NoteWriter.writerow([note.id_mod, note.CIN_Etu, note.PrControl, note.DeControl, note.EFM, round(note.MoyenModule(),2)])
    File_Notes.close()
    ExportProgress()
    File_Absences = open("Data/Absances.csv", "a")  # Use 'w' to overwrite the existing file
    AbsWriter = csv.writer(File_Absences, delimiter=",")
    for abs in ListAbsences:
        AbsWriter.writerow([abs.id_mod, abs.CIN_Etu, abs.date_absence.strftime("%Y-%m-%d")])
    
    File_Absences.close()
    ExportProgress()
    progress.destroy()
    messagebox.showinfo("Exportatation Terminé","Toutes les données ont été exporté avec succès")
    fenAdmini(fen,frame)
def AfficherAbsancesAdmin(fen, frame):
    frame.destroy()
    frameAbsences = Frame(fen, padx=10, pady=5)
    frameAbsences.pack(pady=10)
    labelMsg=Label(frameAbsences, text="Liste d'absence ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    # Treeview widget
    cols = ('Module', 'CIN', 'Date d\'Absence')
    tree = ttk.Treeview(frameAbsences, columns=cols, show='headings', height=8)

    # Style configuration
    style = ttk.Style(fen)
    style.configure("Treeview.Heading", font=('Calibri', 12, 'bold'))
    style.configure("Treeview", font=('Calibri', 12), rowheight=25)

    # Define headings and column widths
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=200)

    # Grid the treeview in the frame
    tree.grid(row=0, column=0, sticky='nsew')

    # Add a scrollbar to the treeview
    scrollbar = ttk.Scrollbar(frameAbsences, orient=VERTICAL, command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    tree.config(yscroll=scrollbar.set)

    # Populate data
    for absence in ListAbsences:
        tree.insert("", "end", values=(absence.CIN_Etu, absence.Non, absence.date_absence))

    # Return button
    buttonReturn = Button(frameAbsences, text="Retour", font="times 16 bold", fg="white", bg="#22B9A8")
    buttonReturn.grid(row=1, column=0, columnspan=2, pady=5, sticky='W')

    # Configure the grid layout to allow resizing
    frameAbsences.grid_rowconfigure(0, weight=1)
    frameAbsences.grid_columnconfigure(0, weight=1)

    # Assign the button's command
    buttonReturn['command'] = lambda: fenAdmini(fen, frameAbsences)


########################################
########################################
########################################

def fenFrmtr(fen,frame=None):
    user=RetUserByCIN(UtlActuel,ListFrmtr)
    if frame:
        frame.destroy()
    frameFrmtr = Frame(fen, padx=5, pady=5)
    frameFrmtr.pack(pady=10)
    username=user.Nom+" "+user.Prenom
    MsgLog=Label(frameFrmtr, text=f"Bonjour {username}", font="Bahnschrift 16 bold", fg="#1199B7")
    MsgLog.grid(row=0,column=0,columnspan=2)
    optionsF = [
        "Saisir les notes",
        "Consulter les notes",
        "Ajouter absence",
        "Ajouter cours",
        "Déconnexion"
    ]

    saisir = Button(frameFrmtr, text=optionsF[0].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=25,
                    command=lambda: OperationF(fen, frameFrmtr, optionsF[0]))
    saisir.grid(row=1, column=0 , padx=5, pady=10)
    
    consulte = Button(frameFrmtr, text=optionsF[1].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=25,
                    command=lambda : OperationF(fen, frameFrmtr, optionsF[1]))
    consulte.grid(row=1, column=1 , padx=5, pady=10)
    AbsenceEtu = Button(frameFrmtr, text=optionsF[2].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=25,
                    command=lambda : OperationF(fen, frameFrmtr, optionsF[2]))
    AbsenceEtu.grid(row=1, column=2 , padx=5, pady=10)
    courss = Button(frameFrmtr, text=optionsF[3].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=25,
                    command=lambda : OperationF(fen, frameFrmtr, optionsF[3]))
    courss.grid(row=1, column=3 , padx=5, pady=10)
    
    button = Button(frameFrmtr, text=optionsF[4].upper(), font="times 12 bold ", fg="white", bg="#EA5A4F",width=53,
                    command=lambda: MenuPrincipale(fen,frameFrmtr))
    button.grid(row=2, column=0 , columnspan=4, padx=5, pady=10)

    
    
def OperationF(fen, fdr, x):
    fdr.destroy()
    framOperFrmtr = Frame(fen, padx=5, pady=5)
    framOperFrmtr.pack(pady=10)
    if x == "Saisir les notes":
        Saisirnotes(fen,framOperFrmtr)
    elif x == "Consulter les notes":
        ConsulteNoteFr(fen,framOperFrmtr)
    elif x == "Ajouter absence":
        GererAbsences(fen,framOperFrmtr)
    elif x == "Ajouter cours":
       ajouterCoursInterface(fen,framOperFrmtr)
        
def Saisirnotes(fen, frame):
    labelMsg=Label(frame, text="Saisir les notes !".upper(), font="Bahnschrift 16 bold", fg="#1199B7")
    labelMsg.grid( row=0,column=0, columnspan=4)

    LCM = Label(frame, text=f"Choisir le module dans lequel vous voulez saisir les notes ", font="Times 12")
    LCM.grid(row=1, column=0, pady=5, sticky=NW)

    ModulesDeFrmtr = RetUserByCIN(UtlActuel, ListFrmtr).Modules

    MC=ttk.Combobox(frame, font="Arial 18", values=RecupereNomModules(ModulesDeFrmtr))
    MC.grid(row=1, column=1, pady=5)

    BT = Button(frame, text="Entrez les Notes", font="times 16 bold", width=36 ,fg="white", bg="#1199B7", command=lambda: Valide(fen, frame ,MC.get()))
    BT.grid(row=2, column=0, columnspan=3, pady=5)

    
    Retour = Button(frame, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:fenFrmtr(fen,frame))
    Retour.grid(row=3, column=0, columnspan=3, pady=5)

def GererAbsences(fen, frame):
    frame.destroy()
    frameAbsences = Frame(fen, padx=5, pady=5)
    frameAbsences.pack(pady=10)

    # Label and entry for Student CIN
    labelCin = Label(frameAbsences, text="CIN Étudiant:", font="Times 12")
    labelCin.grid(row=0, column=0, pady=5)
    entryCin = Entry(frameAbsences, font="times 20 ", width=30, border=0)
    entryCin.grid(row=0, column=1, pady=5)

    # Dropdown for Module Selection
    labelModule = Label(frameAbsences, text="Module:", font="Times 12")
    labelModule.grid(row=1, column=0, pady=5)
    comboModule = ttk.Combobox(frameAbsences, font="times 20 ", width=30, values=[mod.Nom for mod in ToutsModules])
    comboModule.grid(row=1, column=1, pady=5)

    # Entry for Date of Absence
    labelDate = Label(frameAbsences, text="Date(JJ/MM/AAAA):", font="Times 12")
    labelDate.grid(row=2, column=0, pady=5)
    entryDate = Entry(frameAbsences, font="times 20 ", width=30, border=0)
    entryDate.grid(row=2, column=1, pady=5)

    # Button to Add Absence
    buttonAdd = Button(frameAbsences, text="Ajouter Absence", font="times 16 bold", fg="white", bg="#1199B7", width=30,
                       command=lambda: AjouterAbsence(entryCin.get(), comboModule.get(), entryDate.get(), frameAbsences))
    buttonAdd.grid(row=3, column=0, columnspan=2, pady=10)

    # Button to go back
    buttonBack = Button(frameAbsences, text="Retour", font="times 16 bold", fg="white", bg="#ffa245", width=30,
                        command=lambda: fenFrmtr(fen, frameAbsences))
    buttonBack.grid(row=4, column=0, columnspan=2, pady=10)


def ajouterCoursInterface(fen, frame):
    frame.destroy()
    frameAjouterCours = Frame(fen, padx=5, pady=5)
    frameAjouterCours.pack(pady=10)

    # Title Label
    labelTitle = Label(frameAjouterCours, text="Ajouter un Cours", font="Bahnschrift 16 bold", fg="#1199B7")
    labelTitle.grid(row=0, column=0, columnspan=2, pady=10)

    # Course Name Entry
    labelCourseName = Label(frameAjouterCours, text="Nom du Cours:", font="Times 12")
    labelCourseName.grid(row=1, column=0, sticky=W)
    entryCourseName = Entry(frameAjouterCours, font="times 20", width=30, border=0)
    entryCourseName.grid(row=1, column=1, pady=5)

    # PDF Path Entry
    labelPdfPath = Label(frameAjouterCours, text="Chemin du PDF:", font="Times 12")
    labelPdfPath.grid(row=2, column=0, sticky=W)
    entryPdfPath = Entry(frameAjouterCours, font="times 20", width=30, border=0)
    entryPdfPath.grid(row=2, column=1, pady=5)

    # Add Course Button
    buttonAddCourse = Button(frameAjouterCours, text="Ajouter Cours", font="times 16 bold", fg="white", bg="#1199B7", width=30,
                             command=lambda: addCours(entryCourseName.get(), entryPdfPath.get(), frameAjouterCours))
    buttonAddCourse.grid(row=3, column=0, columnspan=2, pady=10)

    # Return Button
    buttonReturn = Button(frameAjouterCours, text="Retour", font="times 16 bold", fg="white", bg="#ffa245", width=30,
                          command=lambda: fenFrmtr(fen, frameAjouterCours))
    buttonReturn.grid(row=4, column=0, columnspan=2, pady=10)







def SelectEtudiantApartairNomModul(nom):
    Etudiant = []
    for m in ToutsModules:
        if m.Nom==nom:
            for f in ListOption:
                if m.id_fil==f.getid():
                    for etu in ListEtu:
                        if etu.idFil== f.getid():
                            Etudiant.append(etu)
                    return Etudiant

def nameEtu(obj):
    return StrSpaces(obj.CIN,16) + StrSpaces(obj.Nom,20) + StrSpaces(obj.Prenom,20)
entete2= StrSpaces("CIN",16) + StrSpaces("Nom",20) + StrSpaces("Prenom",20)


NotesSaisé=[]
def Valide(fen, frame, MC):
    frame.destroy()
    noteframe =Frame(fen, padx=5, pady=5)
    noteframe.pack(padx=5, pady=5)
    
    annuler = Button(noteframe, text="Retour", font="times 14 bold",width=10 , fg="white", bg="#EA5A4F",command=lambda : fenFrmtr(fen,noteframe))
    annuler.grid(row=0, column=0,pady=5,sticky="W")
    
    labelMsg=Label(noteframe, text="La liste des étudiants".upper(), font="Bahnschrift 16 bold", fg="#1199B7")
    labelMsg.grid( row=1,column=0, columnspan=5,)
    
    EntetLabl = Label(noteframe,text=entete2, font="times 14",width=56,bg="white")
    EntetLabl.grid(row=2, column=0,columnspan=4,sticky="W",pady=10)
            
    EntetLabl = Label(noteframe,text="Action", font="times 14",width=20, bg="white")
    EntetLabl.grid(row=2, column=4,pady=10)
    listestagers=SelectEtudiantApartairNomModul(MC)
    n = 3
    
    for etu in listestagers:
        L=[etu.CIN,MC]
        if L not in NotesSaisé:
            if n%2==0:
                bg="#faf4ee"
            else:
                bg="#f2e4d7"

            LCM = Label(noteframe, text=nameEtu(etu), font="Times 12",bg=bg,width=56 )
            LCM.grid(row=n, column=0, columnspan=4 , pady=5, sticky="W")
            
            saisirNote = Button(noteframe, text="saisir les notes",font="times 12 bold ", fg="white", bg="#1199B7", width=20 ,command=lambda s=etu : note_etudiant(s, fen, noteframe,MC))
            saisirNote.grid(row=n, column=4,padx=5, pady=5)
            n+=1
            noteframe.update()

def note_etudiant(s, fen, noteframe,MC):

    noteframe.destroy()
    frameNote = Frame(fen, padx=5, pady=5)
    frameNote.pack(padx=5, pady=5)

    labelMsg=Label(frameNote, text=f"Saisir les notes de l'étudiant {s.Nom} {s.Prenom} de module {MC} ", font="Bahnschrift 14 bold", fg="#1199B7")
    labelMsg.grid(column=0, row=0, columnspan=3)
    
    C1= Label(frameNote, text="La note du premier contrôle :", font="Times 12")
    C1.grid(row=1, column=0, pady=5, sticky=NW)
    
    Note1 = Entry(frameNote, font="times 20 ", width=36, border=0)
    Note1.grid(row=2, column=0,columnspan=3, pady=5,sticky=NSEW)
    
    C2= Label(frameNote, text="La note du deuxième contrôle :", font="Times 12")
    C2.grid(row=3,column=0, pady=5, sticky=NW)
    
    Note2 = Entry(frameNote, font="times 20 ", width=36, border=0)
    Note2.grid(row=4, column=0,columnspan=3,pady=5,sticky=NSEW)
    
    EFM= Label(frameNote,text="La note de l'examen du fin de module :", font="Times 12")
    EFM.grid(row=5, column=0, pady=5, sticky=NW)
    
    NoteEFM = Entry(frameNote, font="times 20 ", width=36, border=0)
    NoteEFM.grid(row=6, column=0,columnspan=3,pady=5,sticky=NSEW)
    
    BtnValider =Button(frameNote,text ="valider",command= lambda STG=s, C1=Note1, C2=Note2, EFM=NoteEFM, mod=MC: ValiderNoteEtudiant(STG,C1,C2,EFM,mod,fen, frameNote,MC),
    font="Times 17 ", bg="#1199B7", fg="white",width=36)
    BtnValider.grid(row=7, column=0, columnspan=3, pady=5,sticky=NSEW)
    
    Retour = Button(frameNote, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:Valide(fen,frameNote,MC))
    Retour.grid(row=8, column=0, columnspan=3, pady=5)


def ValiderNoteEtudiant(STG,C1,C2,EFM,mod,fen,frameNote,MC):
    for m in ToutsModules:
        if m.Nom==mod:
            IDMOD=m.getid()
    if (ErrNote(C1.get()) and ErrNote(C2.get()) and ErrNote(EFM.get())):
        yesno=messagebox.askyesno("Confirmation",f"Voulez vous affecter ces notes a {STG.Nom} {STG.Prenom} ?")
        if yesno:
            N=Note(IDMOD,STG.CIN,C1.get(),C2.get(),EFM.get())
            ListeNotes.append(N)
            NotesSaisé.append([STG.CIN,mod])
            messagebox.showinfo("Confirmation",f"Vous avez saisi la note de {STG.Nom} {STG.Prenom} avec succès")
            Valide(fen,frameNote,MC)
        else:
            return
    else:
        return
    

def ConsulteNoteFr(fen, frame):
    labelMsg=Label(frame, text="Consulter les notes !".upper(), font="Bahnschrift 16 bold", fg="#1199B7")
    labelMsg.grid( row=0,column=0, columnspan=4)

    LCM = Label(frame, text=f"Choisir le module dans lequel voulez consulter les notes ", font="Times 12")
    LCM.grid(row=1, column=0, pady=5, sticky=NW)

    ModulesDeFrmtr = RetUserByCIN(UtlActuel, ListFrmtr).Modules

    MC=ttk.Combobox(frame, font="times 16", values=RecupereNomModules(ModulesDeFrmtr))
    MC.grid(row=1, column=1, pady=5)

    BT = Button(frame, text="Consulter", font="times 16 bold", width=36 ,fg="white", bg="#1199B7", command=lambda: AffichageNoteMod(fen, frame ,MC.get()))
    BT.grid(row=2, column=0, columnspan=3, pady=5)

    
    Retour = Button(frame, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:fenFrmtr(fen,frame))
    Retour.grid(row=3, column=0, columnspan=3, pady=5)
    
def AffichageNoteMod(fen,frame,mod):
    frame.destroy()
    FrameConNote=Frame(fen,padx=5, pady=5)
    FrameConNote.pack(pady=10)
    Annuler = Button(FrameConNote, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenFrmtr(fen,FrameConNote))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(FrameConNote, text=f"Les notes de module {mod} ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("CIN","Nom","Prenom","CONTROLE 1","CONTROLE 2","EFM")
    CodeC=('cin','nom','Prenom','CONTROLE 1','CONTROLE 2','EFM')
    TM=ttk.Treeview(FrameConNote,columns=CodeC,show='headings')
    for i in range(6):
        TM.column(CodeC[i],width=120,anchor='center')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
    for Stg in SelectEtudiantApartairNomModul(mod):
        for note in ListeNotes:
            if note.CIN_stgr==Stg.CIN and note.id_mod== retModByName(mod).getid():
                TM.insert('','end',values=(f'{Stg.CIN}',f'{Stg.Nom}',f'{Stg.Prenom}',f'{note.PrControl}',f'{note.DeControl}',f'{note.EFM}'))
########################################

def fenEtu(fen,frame=None):
    if frame:
        frame.destroy() 
    user=RetUserByCIN(UtlActuel,ListEtu)
    frameEtud = Frame(fen, padx=5, pady=5)
    frameEtud.pack(pady=10)
    username=user.Nom+" "+user.Prenom
    MsgLog=Label(frameEtud, text=f"Bonjour {username}", font="Bahnschrift 16 bold", fg="#1199B7")
    MsgLog.grid(row=0,column=0)
    optionsS = [
        "Consulter les notes",
        "Consulter absence",
        "Afficher cours ",
        "Déconnexion"
    ]

    consulte = Button(frameEtud, text= optionsS[0].upper(), font="times 12 bold ", fg="white", bg="#1199B7",width=23,
                    command=lambda : OperationS(fen, frameEtud,  optionsS[0], user))
    consulte.grid(row=1, column=0 , padx=5, pady=10)

    button = Button(frameEtud, text= optionsS[1].upper(), font="times 12 bold ", fg="white", bg="#EA5A4F",width=23,
                    command=lambda : OperationS(fen, frameEtud,  optionsS[1],user))
    button.grid(row=2, column=0 , padx=5, pady=10)
    buttonCours = Button(frameEtud, text=optionsS[2], font="times 12 bold ", fg="white", bg="#1199B7", width=23,
                          command=lambda: VoirCoursInterface(fen, frameEtud))
    buttonCours.grid(row=3, column=0, padx=5, pady=10)
    button = Button(frameEtud, text=optionsS[3].upper(), font="times 12 bold ", fg="white", bg="#EA5A4F",width=53,
                    command=lambda: MenuPrincipale(fen,frameEtud))
    button.grid(row=4, column=0 , padx=5, pady=10)
    
def OperationS(fen, frameetu, x,user):
    frameetu.destroy()
    framOpeEtu = Frame(fen, padx=5, pady=5)
    framOpeEtu.pack(pady=10)
    if x == "Consulter les notes":
        ConsulteNoteS(fen, framOpeEtu,user)
    elif x == "Consulter absence":
        AfficherAbsancesEtu(fen, framOpeEtu,user)
    
def ConsulteNoteS(fen,framOpeEtu,user):
    Annuler = Button(framOpeEtu, text="Retour", font="times 16 bold" ,fg="white", bg="#22B9A8", command=lambda:fenEtu(fen,framOpeEtu))
    Annuler.grid(row=0, column=0, pady=5 , sticky="W")
    labelMsg=Label(framOpeEtu, text="Mes  Notes  ", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelMsg.grid(row=1, column=0, columnspan=2)
    NomC=("MODULES","CONTROLE 1","CONTROLE 2","EFM","MOYENNE GENERAL")
    CodeC=('MODULES','CONTROLE 1','CONTROLE 2','EFM','MOYENNE GENERAL')
    TM=ttk.Treeview(framOpeEtu,columns=CodeC,show='headings')
    for i in range(5):
        TM.column(CodeC[i],width=150,anchor='w')
        TM.heading(CodeC[i],text=NomC[i])
        TM.grid(row=2,columnspan=2,padx=5,pady=5)
        
    for note in ListeNotes:
        for mod in ToutsModules:
            if note.CIN_Etu==user.CIN and note.id_mod== mod.getid():
                TM.insert('','end',values=(f'{mod.Nom}',f'{note.PrControl}',f'{note.DeControl}',f'{note.EFM}',f'{round(note.MoyenModule(),2)}'))
def AfficherAbsancesEtu(fen, frame, user):
    frame.destroy()
    frameAbsencesEtu = Frame(fen, padx=5, pady=5)
    frameAbsencesEtu.pack(pady=10)

    # Treeview widget
    cols = ('ID Module', 'Date d\'Absence')
    tree = ttk.Treeview(frameAbsencesEtu, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER)

    tree.grid(row=0, column=0, sticky='nsew')

    # Populate data
    for absence in [abs for abs in ListAbsences if abs.CIN_Etu == user.CIN]:
        tree.insert("", "end", values=(absence.id_mod, absence.date_absence))

    # Return button
    Retour = Button(frameAbsencesEtu, text="Retour", font="times 16 bold", width=36 ,fg="white", bg="#EA5A4F", command=lambda:fenEtu(fen,frameAbsencesEtu))
    Retour.grid(row=3, column=0, columnspan=3, pady=5)




from tkinter.ttk import Treeview

def VoirCoursInterface(fen, frame ):
    frame.destroy()
    frameVoirCours = Frame(fen, padx=5, pady=5)
    frameVoirCours.pack(pady=10)

    labelTitle = Label(frameVoirCours, text="Liste des Cours", font="Bahnschrift 16 bold", fg="#22B9A8")
    labelTitle.grid(row=0, column=0, pady=10)

    cols = ('Nom du Cours', 'Ouvrir')
    tree = Treeview(frameVoirCours, columns=cols, show='headings')

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER)

    tree.grid(row=1, column=0, sticky='nsew')

    for cours in Listecours:
        tree.insert("", "end", values=(cours.nom, "Ouvrir"))

    def openPdf(event):
        region = tree.identify('region', event.x, event.y)
        if region == 'cell':
            column = tree.identify_column(event.x)
            item = tree.identify_row(event.y)
            if tree.heading(column)['text'] == 'Ouvrir':
                Cours = Listecours[tree.index(item)]
                chemin_pdf = Cours.chemin_pdf
                #if os.path.exists(chemin_pdf):
                webbrowser.open(chemin_pdf)
                #else:
                #   messagebox.showerror("Erreur", "Fichier PDF introuvable")

    tree.bind('<Double-1>', openPdf)

    buttonReturn = Button(frameVoirCours, text="Retour", font="times 16 bold", fg="white", bg="#ffa245", width=30, command=lambda:fenEtu(fen,frameVoirCours))
    buttonReturn.grid(row=2, column=0, pady=10)
