import csv
from Classes import *
from datetime import *
import secrets
from prettytable import PrettyTable
from tkinter import messagebox 

ListOption,List_Attend,ListEtu,ToutsModules,ListFrmtr,ListeNotes,ListAbsences,Listecours  = [],[],[],[],[],[],[],[]


####################
# ####################

M1=Module("Physique",1,2,"WB122")
M2=Module("MATHS",1,1,"WB457")
M3=Module("Informatique",1,2,"P789")
M4=Module("Industrie 4.0",1,1,"PA123")
LM=[M1,M2,M3,M4]

for m in LM:
    ToutsModules.append(m)
IND=Option("Industrie 4.0","IND4",LM)
GE=Option("Gestion Des Entreprises","GE",LM)


F1=Professeur('CIN1','Ryane','Fouad',date(1998,8,23),LM)
F2=Professeur('CIN2','Boukamel','Adnane',date(1998,8,23),LM)
LFO=[F1,F2]
for f in LFO:
    ListFrmtr.append(f)

LF=[IND,GE]
for f in LF:
    ListOption.append(f)
S1=Etudiant("PA2215",1,"benkiranne","mohamed",date(2003,8,23),LF,11.66,12.5)
S2=Etudiant("PA2245",2,"mourad","hammale",date(2003,6,15),LF,11.58)
S3=Etudiant("PA2875",1,"doha","friat",date(2004,6,26),LF,14.74)
S4=Etudiant("PA2645",1,"El_gharsi","Imane",date(2004,10,16),LF,14.98)
S5=Etudiant("PA2240",1,"Banouar","Omaima",date(2000,8,20),LF,14.42)

LA=[S1,S2,S3,S4,S5]
for s in LA:
    List_Attend.append(s)

N1=Note(1,"PA2215",12.5,17.75,15.00)
N2=Note(2,"PA2215",19.5,19.75,18.00)
N3=Note(3,"PA2215",17.5,19.25,18.00)
N4=Note(4,"PA2215",18.5,18.75,19.00)

N5=Note(1,"PA2875",10,11.50,12.00)
N6=Note(2,"PA2875",10,10,18.00)
N7=Note(3,"PA2875",11.75,15.25,14.00)
N8=Note(4,"PA2875",18.5,18.75,19.00)

LN=[N1,N2,N3,N4,N5,N6,N7,N8]
for n in LN:
   ListeNotes.append(n)

ListeAbsences = [
    Absence("CIN123", 1, date(2023, 1, 10)), 
    Absence("CIN456", 2, date(2023, 1, 15)),  
    Absence("CIN789", 1, date(2023, 1, 20))]

path = "https://www.bing.com/ck/a?!&&p=a5a5fc86ae7ff927JmltdHM9MTcwNDA2NzIwMCZpZ3VpZD0xMzI1MTBiZi0yZGJhLTYyYmEtMTQ3NS0wM2U5MmNiMjYzNmUmaW5zaWQ9NTE1OQ&ptn=3&ver=2&hsh=3&fclid=132510bf-2dba-62ba-1475-03e92cb2636e&psq=mmc+pdf&u=a1aHR0cDovL3d3dy5jaGlyZXV4LmZyL21wL2NvdXJzL21lY2FuaXF1ZV9taWxpZXV4X2NvbnRpbnVzLnBkZg&ntb=1"
Listecours = [Cours("mmc", path), Cours("Deep Learning","https://d2l.ai/")]


####################



DA=date(2022,6,6)
file_Admini="AuthAdministration.csv"
file_Prof="AuthProfs.csv"
file_Etu="AuthEtudiant.csv"
def MenuEtu():
    print("""
        #########################################
        #                  Menu                 #
        #---------------------------------------#
        # 1 | Inscrir                           #
        # 2 | Consulter notes                   #
        # 0 | Deconnexion                       #
        #                                       #
        #########################################
        """)
    
def MenuProf():
    print("""
        #########################################
        #                  Menu                 #
        #---------------------------------------#
        # 1 | Aficher La liste des étudiants    #
        # 2 | Saisir notes                      #
        # 3 | Consulter les notes               #
        # 3 | Ajouter absence                   #
        # 0 | Deconnexion                       #
        #                                       #
        #########################################
        """)
    
def MenuAdmini():
    print("""
        ############################################
        #                    Menu                  #
        #------------------------------------------#
        # 1  | Ajouter une option                  #
        # 2  | Ajouter un étudiant                 #
        # 3  | Ajouter un enseignant               #
        # 4  | Afficher La liste des étudiants     #
        # 5  | Afficher La liste des enseignants   #
        # 6  | Supprimer un étudiant               #
        # 7  | Supprimer un enseignant             #
        # 8  | Calculer et Afficher les notes      #
        # 9  | Exporter les données dans des CSVs  #
        # 10 | Importer les données                #
        # 11 | Afficher Absance                    #
        # 0  | Deconnexion                         #
        #                                          #
        ############################################
        """)

# fonction pour verifier si un étudiant est deja existé
def ExisteEtudiant(List,C):
    for stg in List:
        if stg.CIN == C:
            return True
    return False

# fonction pour verifier si une prof est deja existe
def ExisteProf(C):
    for frmtr in ListFrmtr:
        if frmtr.CIN == C:
            return True
    return False

# fonction pour verifier si un module existe ou non
def ExisteModule(nom_mod):
    for mdl in ToutsModules:
        if mdl.Nom == nom_mod:
            return True
    return False

# fonction pour verifier si une option existe ou non
def ExisteOptien(nom_fil):
    for flr in ListOption:
        if flr.Nom == nom_fil:
            return True
    return False

#################################
# Gestion des erreurs

def EntChoix(options,msg):
    while True:
        try:
            choix = int(input(msg))
            if choix in options:
                return choix
            else:
                print("Choix non valide")
        except (ValueError):
            print("Entrée invalide. Veuillez entrer un entier.")
            
def EntNoteFloat(msg):
    while True:
        try:
            N = float(input(msg))
            if N > 0 and N < 20:
                return N
            else:
                print("La valuer donnée non valide ")
        except (ValueError):
            print("Entrée invalide !!")
def EntDate(min,max,msg):
    while True:
        try:
            N = int(input(msg))
            if N >= min and N <= max:
                return N
            else:
                print("La valuer donnée non valide ")
        except (ValueError):
            print("Entrée invalide !!")
##################################

# fonction pour confiremer l'utilisateur
def confirmeUtl(User, Pass, File):
    global UtlActuel
    f = open(File, 'r')
    reader = csv.reader(f)
    for ligne in reader:
        if len(ligne) == 2:
            U, P = ligne[:2]
            if U == User and P == Pass:
                UtlActuel = User
                return True
    return False

# fonction pour verifier si l'age de l'étudiant est entre 15ans et 30 ans
def VerifierAge(DN,DA):
    age = int((DA - DN).days / 365.25)
    if age  < 30 and age > 15:
        return True
    else:
        return False
    
#  fonction pour ajouter un option
def AjouteOption():
    nom=input("Entrez nom de l'option :").title()
    while ExisteOptien(nom):
        print("Une option  avec ce nom est deja existe !!")
        nom=input("Entrez nom de l'option :").title()
    abbr=input("Entrez l'abbr de l'option :").upper()
    listMods=[]
    F=Option(nom,abbr)
    idFil=F.getid()
    print("Entrez les modules de", nom)
    for i in range(3):
        print("Entrez nom de module N°",i+1,end=":")
        Nom_mod=input().title()
        Coeff=EntChoix([1,2,3,4],"Entrez le coeffeciant de module (Max : 4): ")
        mod=Module(Nom_mod,idFil,Coeff)
        listMods.append(mod)
        
        ToutsModules.append(mod)
    F.ListModules=listMods
    ListOption.append(F)
    print(nom,"a été ajouté avec succée")
    
# function pour tries les étudiants par rapport au notes de bac
def getnote(obj):
    return obj.BacNote
# fonction pour accepter des étudiants  que sont dans la liste d'attent
def AjoutEtu():
    if List_Attend == []:
        print("La liste d'attent est vide")
    else :
        if len(ListEtu) <= 50:
            List_Attend.sort(key=getnote,reverse=True)
            for etu in List_Attend :
                print(etu)
                print("\n 1 | Accepter \t 2 | Refuser")
                option=[1,2]  
                choix=EntChoix(option,"Votre decision : ")
                
                if choix == 1 :
                    ListEtu.append(etu)
                    print("Vous avez accepté",etu.Nom,etu.Prenom)
                    file="AuthEtudiant.csv"
                    F=open(file,'a')
                    ECV=csv.writer(F)
                    Pass = secrets.token_hex(5)
                    ECV.writerow([etu.CIN, Pass])
                    F.close()
                else :
                    print("Vous avez refusé",etu.Nom,etu.Prenom)
            for etu in List_Attend:
                for etud in ListEtu:
                    if etu.CIN == etud.CIN :
                        List_Attend.remove(etu)
        else :
            print("La list des étudiants  est insuffisante")
            
# fonction pour personaliser la languer d'une chain de characters
def StrSpaces(text, total_length):
    spaces_needed = max(0, total_length - len(text))
    filled_text = text + " " * spaces_needed
    return filled_text

# fonction pour afficher tout le module en form d'un Menu 
def afficherModules(List):
    print("#"*40)
    for mod in List:
        print("#",StrSpaces(str(mod.getid()),3),"|",StrSpaces(mod.Nom,30),"#")
    print("#"*40)
#  fonction pour entrez la date de naissance
def SaisirDateNai():
    print("Entrez la date de naissance :")
    jj=EntDate(1,31,"Le Jour :")
    mm=EntDate(1,12,"Le Mois :")
    aaaa=EntDate(1950,2015,"L'Anné :")
    DN=date(aaaa,mm,jj)
    return DN

# fonction pour a jouter un formateur
def AjoutFrmtr():
    cin=input("Enrtez la CIN du professeur :").upper()
    while ExisteProf(cin) == True:
        print("Le professeur est deja existe")
        cin=input("Enrtez un autre CIN :")
    nom=input("Entrez le nom de professeur :").title()
    prenom=input("Entrez le prenom de professeur :").title()
    DN=SaisirDateNai()
    print("Choisissez le (s) module (s) que le professeur enseignera :")
    Form=Professeur(cin,nom,prenom,DN)
    listModFrmtr=[]
    options=[]
    for mod in ToutsModules:
        options.append(mod.getid())
        
    NM=EntChoix([1,2,3],"Nombre de module que ce Professeur va enseigner (Max : 3): ")
    afficherModules(ToutsModules)
    
    for i in range(NM):
        print("Module",i+1,":")
        NumMod=EntChoix(options,"Entrez l'id de module a ajouter :")
        for mod in ToutsModules:
            if mod.getid()==NumMod:
                listModFrmtr.append(mod)
    Form.Modules=listModFrmtr
    ListFrmtr.append(Form)
    print(nom,prenom,"a été ajouté avec succée")
    # enregestrer les infos d'acces du professeur 
    file="AuthProfs.csv"
    F=open(file,'a')
    ECV=csv.writer(F)
    Pass = secrets.token_hex(5)
    ECV.writerow([cin, Pass])
    F.close()

# fonction pour afficher tout les 
# étudiants  en from d'un tableau
def AfficherEtu():
    if ListEtu==[]:
        print("*"*30)
        print("Aucan étudiannt a afficher !!")
        print("*"*30)
    else :
        table=PrettyTable(["CIN","Nom","Prenom","Date de naissance","Note de bac","Option"])
        for etu in ListEtu:
            table.add_row([etu.CIN,etu.Nom,etu.Prenom,str(etu.DateNai),etu.BacNote,etu.NomFil()])
        print(table)
def AfficherProf():
    if ListFrmtr == []:
        print("*"*30)
        print("Aucun professeur a afficher !!")
        print("*"*30)
    else:
        table=PrettyTable(["CIN","Nom","Prenom","Date de naissance","Modules"])
        for frmtr in ListFrmtr:
            table.add_row([frmtr.CIN,frmtr.Nom,frmtr.Prenom,str(frmtr.DateNai),frmtr.NomModules()])
        print(table)
def SupremeEtu():
    CIN=input("Entrez CIN de l'étudiant a suppremer: ")
    while ExisteEtudiant(ListEtu,CIN)==False:
        print("Etudian tn'existe pas!!")
        CIN=input("Entrez CIN de l'étudiant: ")
    for etu in ListEtu:
        if CIN ==etu.CIN:
            ListEtu.remove(etu)
    print("Un étudiant a été suppremé avec succée")
    
def SupremeFrmtr():
    CIN=input("Entrez CIN de  formateur a suppremer: ")
    while ExisteProf(CIN)==False:
        print(" Professeur n'existe pas!!")
        CIN=input("Entrez CIN de professeur valide: ")
    for frmtr in ListFrmtr:
        if CIN ==frmtr.CIN:
            ListFrmtr.remove(frmtr)
    print("Un professeur a été suppremé avec succée")

def RetUserByCIN(cin,List):
    for ele in List:
        if ele.CIN==cin:
            return ele
    
def RetModuleByID(id):
    for ele in ToutsModules:
        if ele.getid()==id:
            return ele

def CalculeNotes(cin):
    NoteGeneral = 0
    Coeff = 0
    for Note in ListeNotes:
        if cin == Note.CIN_Etu:
            NG = Note.MoyenModule()
            CO = RetModuleByID(Note.id_mod).Coeff
            NoteGeneral += NG * CO
            Coeff += CO
    if Coeff != 0:
        MoyenGenerale = round(NoteGeneral / Coeff, 2)
    else:
        MoyenGenerale = 0
    RetUserByCIN(cin, ListEtu).MoyGeneral = MoyenGenerale

def AfficherNotes():
    for etu in ListEtu:
        CalculeNotes(etu.CIN)
    
    table=PrettyTable(["CIN","Nom et Prenom","Filiere","Moyenne Generale"])
    for Etu in ListEtu:
        table.add_row([Etu.CIN,Etu.Nom+" "+Etu.Prenom,Etu.NomFil(),Etu.MoyGeneral])
    print(table)

def SaisirNotes():
    ModulesDeFrmtr=RetUserByCIN(UtlActuel,ListFrmtr).Modules
    afficherModules(ModulesDeFrmtr)
    options=[]
    for mod in ModulesDeFrmtr:
        options.append(mod.getid())
    choix=EntChoix(options,"Entrez le module que vous voullez saisir les notes :")
    module=RetModuleByID(choix)
    print("Vous avez choisé le module",module.Nom)
    fil=module.id_fil
    for etu in ListEtu:
        if etu.idFil == fil :
            print("Saisir le note de",etu.Nom)
            C1=EntNoteFloat("Entrez la note de 1ere controle :")
            
            C2=EntNoteFloat("Entrez la note de 2éme controle :")
            
            EFM=EntNoteFloat("Entrez la note de l'EFM :")
            
            N=Note(module.getid(),etu.CIN,C1,C2,EFM)
            ListeNotes.append(N)
            
def ConsulterNoteFr():
    ModulesDeFrmtr=RetUserByCIN(UtlActuel,ListFrmtr).Modules
    fils=set()
    for module in ModulesDeFrmtr:
        fils.add(module.id_fil)
    table=PrettyTable([["CIN","Nom et Prenom","Option","Moyenne Generale"]])
    for stg in ListEtu:
        if stg.idFil in fils:
            table.add_row([stg.CIN,stg.Nom+" "+stg.Prenom,stg.NomFil(),stg.MoyGeneral])
    print(table)
    
def retModByName(name):
    for mod in ToutsModules:
        if mod.Nom == name:
            return mod
        
def Inscription():
    DN=SaisirDateNai()
    DA=date(2023,9,10)
    if VerifierAge(DN,DA)== False :
        print("Vous ne peuvent pas iscrir !!")
    else:
        C = input("Entrez CIN: ").upper()
        while ExisteEtudiant(ListEtu,C) or ExisteEtudiant(List_Attend,C):
            print("Ce CIN est deja existe !!")
            C= input("Entrez votre CIN")
        N = input("Entrez votre nom: ").title()
        P = input("Entrez votre prénom: ").title()
        BacNote = EntNoteFloat("Enter la note de bac: ")

        options=[]
        print("########## LES OPTIONS ##########")
        print("#"*40)
        for ops in ListOption:
            options.append(ops.getid())
            print("#",StrSpaces(str(ops.getid()),3),"|",StrSpaces(ops.Nom,30),"#")
        print("#"*40)
        
        fil = EntChoix(options,"Choiser une option: ")
        Etudiant = Etudiant(C,fil, N, P, DN, ListOption, BacNote)
        List_Attend.append(Etudiant)
        print("Vous avez inscré avec succée")
        # enregestrer les infos d'acces de l'étudiant 
        

def ConsulterNoteEtudiant():
    cin=input("Entrez le CIN d'utilisatuer : ").upper()
    if ExisteEtudiant(cin):
        Pass=input("Entrez le mot de pass : ")
        if  confirmeUtl(cin,Pass,file_Etu):
            print("Mon Notes:")
            table=PrettyTable(["Module","1er Controle","2éme Controle","EFM","Moyenne de module"])
            for note in ListeNotes:
                if note.CIN_Etu == UtlActuel:
                    module = RetModuleByID(note.id_mod)
                    table.add_row([module.Nom,note.PrControl,note.DeControl,note.EFM,round(note.MoyenModule(),2)])
            print(table)
        else:
            print("Mot de pass non valide!")
    else :
        print("Aucun étudiant avec ce CIN !!")




def AjouterAbsence(CIN_Etu, nom_module, date_str, frame):
    # Validate the student's CIN
    if not ExisteEtudiant(ListEtu, CIN_Etu):
        messagebox.showerror("Erreur", "Aucun étudiant avec ce CIN trouvé !")
        return 

    # Find the module ID based on the module name
    id_mod = None
    for mod in ToutsModules:
        if mod.Nom == nom_module:
            id_mod = mod.getid()
            break

    if id_mod is None:
        messagebox.showerror("Erreur", "Aucun module trouvé avec ce nom !")
        return

    # Parse the date
    try:
        jj, mm, aaaa = map(int, date_str.split('/'))
        date_absence = date(aaaa, mm, jj)
    except ValueError:
        messagebox.showerror("Erreur", "Format de date incorrect !")
        return

    # Create and add the absence
    absence = Absence(CIN_Etu, nom_module, date_absence)
    ListAbsences.append(absence)
    messagebox.showinfo("Succès", "Absence ajoutée avec succès !")



def Exportation():
    File_filieres=open("Data/Options.csv","a")
    FilWriter=csv.writer(File_filieres, delimiter=",")
    for fil in ListOption:
        FilWriter.writerow([fil.Nom,fil.Abr])
        
    File_Modules=open("Data/Modules.csv","a")
    ModWriter=csv.writer(File_Modules, delimiter=",")
    for mod in ToutsModules:
        ModWriter.writerow([mod.getid(),mod.Nom, mod.id_fil,mod.Coeff,mod.CINFrmtr])
    File_Cours = open("Data/cours.csv", "a")
    CoursWriter = csv.writer(File_Cours, delimiter=",")
    for cours in Listecours:
        CoursWriter.writerow([cours.nom,cours.chemin_pdf])
        
    File_Etudiants=open("Data/Etudiants.csv","a")
    StgWriter=csv.writer(File_Etudiants, delimiter=",")
    for etu in ListEtu:
        StgWriter.writerow([etu.CIN,etu.Nom, etu.Prenom,etu.DateNai,etu.idFil,etu.BacNote])
        
    EtuAttent=open("Data/EtudiantsEnAttent.csv","a")
    EtuWriter=csv.writer(EtuAttent, delimiter=",")
    for etu in List_Attend:
        EtuWriter.writerow([etu.CIN,etu.Nom, etu.Prenom,etu.DateNai,etu.idFil,etu.BacNote])
        
    File_Formatuer=open("Data/Professeurs.csv","a")
    FrmtWriter=csv.writer(File_Formatuer, delimiter=",")
    for frmtr in ListFrmtr:
        FrmtWriter.writerow([frmtr.CIN,frmtr.Nom, frmtr.Prenom,frmtr.DateNai,frmtr.AfficheNomMods()])
        
    File_Notes=open("Data/Notes.csv","a")
    NoteWriter=csv.writer(File_Notes, delimiter=",")
    for note in ListeNotes:
        NoteWriter.writerow([note.id_mod,note.CIN_Etu,note.PrControl,note.DeControl,note.EFM,note.MoyenModule()])
    File_Absences = open("Data/Absances.csv", "a")  # 'a' to append data
    AbsWriter = csv.writer(File_Absences, delimiter=",")
    for abs in ListAbsences:
        AbsWriter.writerow([abs.id_mod, abs.CIN_Etu, abs.date_absence.strftime("%Y-%m-%d")])
      # Écrire les informations du cours dans le fichier cours.csv
    with open("Data/cours.csv", "a", encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=",")
        for c in Listecours :
            writer.writerow([c.nom , c.chemin_pdf])

    print("Touts le données ont été exporté avec succeé ")

def ImportDate(str):
    DNai = datetime.strptime(str, "%Y-%M-%d").date()
    return DNai

def Importation():
    with open("Data/Options.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 2:
                N, Abr = info[0], info[1]
                ListOption.append(Option(N, Abr))
    

    with open("Data/Modules.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 4:
                N, idfil, Coeff, CinF = info[0], info[1], info[2], info[3]
                ToutsModules.append(Module(N, int(idfil), int(Coeff), CinF))
                

    with open("Data/Etudiants.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                ListEtu.append(Etudiant(C, int(idF), N, P, DN, ListOption, BN))
    

    with open("Data/Notes.csv","r") as Notesfile:
        for line in Notesfile:
            info = line.strip().split(",")
            if len(info) == 5:
                idM,Cstg,C1,C2,EFM= info[0],info[1],info[2],info[3],info[4]
                ListeNotes.append(Note(int(idM),Cstg,float(C1),float(C2),float(EFM)))
    

    
    with open("Data/EtudiantsEnAttent.csv", "r") as file:
        for line in file:
            info = line.strip().split(",")
            if len(info) == 6:
                C, N, P, DN, idF, BN = info[0], info[1], info[2], info[3], info[4], info[5]
                DN = ImportDate(info[3])
                List_Attend.append(Etudiant(C, int(idF), N, P, DN, ListOption, float(BN)))
    with open("Data/cours.csv", "r") as file:
        for line in file:
            line = line.strip().split(",")
            if len(line) == 2:
                nom, chemin_pdf = line[0] ,line[1]
                Listecours.append(Cours(nom , chemin_pdf))
    
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

    with open("Data/Absances.csv", "r") as File_Absences:
        reader = csv.reader(File_Absences)
        for row in reader:
            if len(row) == 3:
                id_mod, CIN_Etu, date_abs = row
                ListAbsences.append(Absence(id_mod, CIN_Etu, datetime.strptime(date_abs, "%Y-%m-%d").date()))
    print("Touts le données valides ont été importés avec succeé ")

def addCours(nom, path, frame):
    for cours in Listecours:
        if cours.nom == nom:
            messagebox.showerror("Erreur", "Un cours avec ce nom existe déjà.", parent=frame)
            return

    # Ajouter le cours à la liste
    nouveau_cours = Cours(nom, path)
    Listecours.append(nouveau_cours)
    messagebox.showinfo("Parfait", "Le cours est ajouté avec succès")
  

