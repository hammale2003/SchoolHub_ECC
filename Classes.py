from abc import * 

###################################

class Utilisateur (ABC):
    def __init__(self,C,N,P,DN):
        self._CIN=C
        self._Nom=N
        self._Prenom=P
        self._DateNai=DN
    @property
    def CIN(self):
        return self._CIN
    
    @property
    def Nom(self):
        return self._Nom
    
    @property
    def Prenom(self):
        return self._Prenom
    
    @property
    def DateNai(self):
        return self._DateNai
    
    @abstractmethod
    def __str__():
        pass
###################################
class Administration(Utilisateur):
    def __init__(self, C, N=None, P=None, DN=None):
        super().__init__(C, N, P, DN)
    
    def __str__(self):
        return f"""
        CIN                 : {self._CIN}
        Nom                 : {self._Nom}
        Prenom              : {self._Prenom}
        Date de Naissaance  : {self._DateNai}
        """
###################################
class Professeur(Utilisateur):
    def __init__(self, C, N, P, DN, Mods=None):
        super().__init__(C, N, P, DN)
        self._Modules = Mods
    
    @property
    def Modules(self):
        return self._Modules
    
    @Modules.setter
    def Modules(self,ListModFrmtr):
        self._Modules = ListModFrmtr

    def AjoutMod(self,obj):
        self._Modules.append(obj)
        
    def NomModules(self):
        modules_Ens=[]
        for mod in self._Modules:
            modules_Ens.append(mod.Nom)
        return modules_Ens
    
    def AfficheNomMods(self):
        str=""
        i=1
        for mod in self._Modules:
            str+=f"-{mod.Nom} "
            i+=1
        return str
    
    def ajouterCours(self, nom_module, chemin_cours):
        if nom_module in self.NomModules():
            self._Cours[nom_module] = chemin_cours
            print(f"Cours ajouté pour le module {nom_module}: {chemin_cours}")
        else:
            print(f"Module {nom_module} non trouvé.")
    def __str__(self):
        return f"""
        CIN                 : {self._CIN}
        Nom                 : {self._Nom}
        Prenom              : {self._Prenom}
        Date de Naissaance  : {self._DateNai}
        Liste des Modules   : {self.NomModules()}
        """
###################################
class Etudiant(Utilisateur):
    def __init__(self, C,id_fil, N, P, DN,lstFil, BacNote, MoyGeneral=None):
        super().__init__(C, N, P, DN)
        self._id_fil = id_fil
        self._BacNote = BacNote
        self._lstFil=lstFil
        self._MoyGeneral=MoyGeneral
    
    @property
    def idFil(self):
        return self._id_fil
    
    @property
    def BacNote(self):
        return self._BacNote
    
    @property
    def MoyGeneral(self):
        return self._MoyGeneral
    
    @MoyGeneral.setter
    def MoyGeneral(self,MG):
        self._MoyGeneral = MG
    
    def NomFil(self):
        for Fil in self._lstFil:
            if self._id_fil == Fil.getid() :
                return Fil.Nom
    
    def __str__(self):
            return f"""
            CIN                 : {self._CIN}
            Nom                 : {self._Nom}
            Prenom              : {self._Prenom}
            Date de Naissaance  : {self._DateNai}
            Note de Bac         : {self._BacNote}
            filiere             : {self.NomFil()}
            """
###################################
class Option:
    id=1
    def __init__(self,N,Abr,listModule=None):
        self._id=Option.id
        self._Nom=N
        self._Abr=Abr
        self._ListModules=listModule
        Option.id+=1
        
    
    def getid(self):
        return self._id
    
    @property
    def Nom(self):
        return self._Nom
    
    @property
    def Abr(self):
        return self._Abr

    @property
    def ListModules(self):
        return self._ListModules
    @ListModules.setter
    def ListModules(self,L):
        self._ListModules=L
    
    def __str__(self):
        return f"""
        id          : {self._id}
        Nom         : {self._Nom}
        Abr         : {self._Abr}
        """
###################################
class Module:
    id=1
    def __init__(self,N,id_fil,Coeff,CINFrmtr=None) :
        self._id=Module.id
        self._Nom=N
        self._id_fil=id_fil
        self._Coeff=Coeff
        self._CINFrmtr=CINFrmtr
        Module.id+=1
    
    def getid(self):
        return self._id
    
    @property
    def Nom(self):
        return self._Nom
    
    @property
    def id_fil(self):
        return self._id_fil
    
    @property
    def Coeff(self):
        return self._Coeff
    
    @property
    def CINFrmtr(self):
        return self._CINFrmtr
    
    @CINFrmtr.setter
    def CINFrmtr(self,C):
        self._CINFrmtr = C
    
    def __str__(self):
        return f"""
        Nom          : {self._Nom}
        Coefficient  : {self._Coeff}
        """
###################################
class Note:
    def __init__(self, id_mod, CIN_Etu, C1=None, C2=None, EFM=None):
        self._PrControl = C1
        self._DeControl = C2
        self._EFM = EFM
        self._id_mod=id_mod
        self._CIN_Etu=CIN_Etu
    
    @property
    def id_mod(self):
        return self._id_mod
    
    @property
    def CIN_Etu(self):
        return self._CIN_Etu
    
    @property
    def PrControl(self):
        return self._PrControl
    
    @PrControl.setter
    def PrControl(self,C1):
        self._PrControl=C1
    
    @property
    def DeControl(self):
        return self._DeControl
    
    @DeControl.setter
    def DeControl(self,C2):
        self._DeControl=C2
    
    @property
    def EFM(self):
        return self._EFM
    
    @EFM.setter
    def EFM(self,EFM):
        self._EFM=EFM
        
    @property
    def id_mod(self):
        return self._id_mod
    
    @property
    def CIN_Edu(self):
        return self._CIN_Edu
    
    def MoyenModule(self):
        if self._PrControl !=None and self._DeControl !=None and self._EFM !=None :
            moycnt = (float(self._PrControl) + float(self._DeControl))/2
            return (moycnt + float(self._EFM)*2)/3
        else :
            return 0
class Absence:
    def __init__(self, Non, CIN_Etu, date_absence):
        self._Non = Non       # ID of the Module
        self._CIN_Etu = CIN_Etu     # CIN of the Student
        self._date_absence = date_absence # Date of Absence
    
    @property
    def Non(self):
        return self._Non
    
    @property
    def CIN_Etu(self):
        return self._CIN_Etu
    
    @property
    def date_absence(self):
        return self._date_absence

    def __str__(self):
        return f"""
        Module        : {self._Non}
        Student CIN      : {self._CIN_Etu}
        Date of Absence  : {self._date_absence}
        """
###################################
class Cours:
   

    def __init__(self, nom, chemin_pdf):
        
        self._nom = nom  # Name of the course
       # ID of the module this course belongs to
        self._chemin_pdf = chemin_pdf  # File path to the course PDF
        #self._auteur = auteur  # Author of the course
       
    
    
    @property
    def nom(self):
        return self._nom
    
    
    @property
    def chemin_pdf(self):
        return self._chemin_pdf

   
    
    def __str__(self):
        return (self.nom, self.chemin_pdf)
###################################
