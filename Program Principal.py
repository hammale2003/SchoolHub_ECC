from Classes import *
from Functions import *
from datetime import date

while True:
    print(
        """
        #########################################
        #            Entrez Comme :             #
        #---------------------------------------#
        # 1 | Administr                         #
        # 2 | Professeu                         #
        # 3 | Etudiant                          #
        #---------------------------------------#
        # 0 | Quitter le programme              #
        #                                       #
        #########################################
        """
    )
    options=[0,1,2,3]
    utl=EntChoix(options,"Entrez votre choix :")
    if utl == 1:
        user=input("Entrez le nom d'utilisatuer : ")
        Pass=input("Entrez le mot de pass : ")
        fois=0
        while confirmeUtl(user,Pass,file_Admini)==False:
            print("Nom d'utilisatuer ou mot de pass non valide !!")
            user=input("Entrez le nom d'utilisatuer : ")
            Pass=input("Entrez le mot de pass : ")
        while True:
            MenuAdmini()
            options=[0,1,2,3,4,5,6,7,8,9,10]
            choix=EntChoix(options,"Entrez votre choix :")
            if choix == 1:  
                AjouteOption()
            elif choix == 2:
                AjoutEtu()
            elif choix == 3:
                AjoutFrmtr()
            elif choix == 4:
                AfficherEtu()
            elif choix == 5:
                AfficherProf()
            elif choix == 6:
                SupremeEtu()
            elif choix == 7:
                SupremeFrmtr()
            elif choix == 8:
                AfficherNotes()
            elif choix == 9:
                Exportation()
            elif choix == 10:
                Importation()
            else:
                break
    elif utl == 2:
        cin=input("Entrez le CIN d'utilisatuer : ").upper()
        Pass=input("Entrez le mot de pass : ")
        while  confirmeUtl(cin,Pass,file_Prof)==False:
            cin=input("Entrez un CIN valide !!! : ")
            Pass=input("Entrez le mot de pass : ")
        while True:
            MenuProf()
            options=[0,1,2,3]
            choix=EntChoix(options,"Entrez votre choix :")
            if choix == 1:
                AfficherEtu()
            elif choix == 2:
                SaisirNotes()
            elif choix == 3:
                ConsulterNoteFr()
            else:
                print("Au revoir !!")
                break
    elif utl == 3:
        while True:
            MenuEtu()
            options=[0,1,2]
            choix=EntChoix(options,"Entrez votre choix :")
            if choix == 1:
                Inscription()
            elif choix == 2:
                ConsulterNoteEtudiant()
            else:
                print("Au revoir !!")
                break
    elif utl == 0:
        break
    else:
        print("Choix non valide")

