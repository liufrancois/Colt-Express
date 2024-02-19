from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time
from random import randint

chemin_absolu = ""

class Jeu(Tk):
    def __init__(self):
        super().__init__()
        #valeur modifiable
        self.nb_wagons=4
        self.nb_joueur=3 #max 3
        self.nb_action=3
        self.nb_tour=3

        self.nb_action2=self.nb_action
        self.nb_ac_a_eff0=0
        self.nb_ac_a_eff1=0
        self.nb_ac_a_eff2=0
        self.nb_ac_a_eff3=0
        self.tourde=0
        
        self.scroll = Scrollbar(self,width=200)
        self.liste=Listbox(self,yscrollcommand=self.scroll.set,width=50,height=25)    

        self.coord=[]
        self.coord_possible()

        self.afficher_wagons()
        self.afficher_locomotive()

        #generation du butin
        self.butins=[]
        self.butin_x=[]
        self.generer_butin()
        
        #bandits
        self.bandits=[]
        for i in range(self.nb_joueur):
            self.bandits.append(Bandit(self,40,40,'player'+str(i),i*170+40,50,[],0,[],self.coord,ImageTk.PhotoImage(Image.open(chemin_absolu+"bandit"+str(i)+".png").resize((35,65)))))

        #Marshall
        self.marshall=Marshall(self,40,40,self.coord[-1],140,self.coord)

        #image des boutons
        self.dr=ImageTk.PhotoImage(Image.open(chemin_absolu+"droite.png").resize((20,20)))
        self.gu=ImageTk.PhotoImage(Image.open(chemin_absolu+"gauche.png").resize((20,20)))
        self.ha=ImageTk.PhotoImage(Image.open(chemin_absolu+"haut.png").resize((20,20)))
        self.ba=ImageTk.PhotoImage(Image.open(chemin_absolu+"bas.png").resize((20,20)))


        #boutons pour le player0
        self.b00=Button(self,image=self.dr,command=self.buton_droit0)
        self.b10=Button(self,image=self.gu,command=self.buton_gauche0)
        self.b20=Button(self,image=self.ha,command=self.buton_haut0)
        self.b30=Button(self,image=self.ba,command=self.buton_bas0)
        #boutons pour le player1
        self.b01=Button(self,image=self.dr,command=self.buton_droit1)
        self.b11=Button(self,image=self.gu,command=self.buton_gauche1)
        self.b21=Button(self,image=self.ha,command=self.buton_haut1)
        self.b31=Button(self,image=self.ba,command=self.buton_bas1)
        #boutons pour le player2
        self.b02=Button(self,image=self.dr,command=self.buton_droit2)
        self.b12=Button(self,image=self.gu,command=self.buton_gauche2)
        self.b22=Button(self,image=self.ha,command=self.buton_haut2)
        self.b32=Button(self,image=self.ba,command=self.buton_bas2)
        #boutons pour le player3
        self.b03=Button(self,image=self.dr,command=self.buton_droit3)
        self.b13=Button(self,image=self.gu,command=self.buton_gauche3)
        self.b23=Button(self,image=self.ha,command=self.buton_haut3)
        self.b33=Button(self,image=self.ba,command=self.buton_bas3)

        #jeu
        self.planification(0)



    def planification(self,i):
        self.scrollbar(f"tour de {self.bandits[i].name}.")
        self.cree_button(i)


    def action(self):
        bon=0
        for j in range(self.nb_joueur):
            if len(self.bandits[j].action)==self.nb_action:
                bon+=1
                if self.tourde<=self.nb_joueur-1:
                    self.planification(self.tourde)
                    return


        if bon==self.nb_joueur:
            for i in range(self.nb_action):
                self.marshall.mouvement_Marshall()
                self.verif_Marshall()
                for k in range(self.nb_joueur):
                    if self.bandits[k].action[i]=="haut":
                        self.bandits[k].deplacement_haut()
                    if self.bandits[k].action[i]=="bas":
                        self.bandits[k].deplacement_bas()
                    if self.bandits[k].action[i]=="gauche":
                        self.bandits[k].deplacement_gauche()
                    if self.bandits[k].action[i]=="droit":
                        self.bandits[k].deplacement_droite()
                    self.verif_butin(k)
                    self.verif_Marshall()
                    time.sleep(1)
        else:
            return
        for m in range(self.nb_joueur):
            self.bandits[m].action=[]
        self.nb_action=self.nb_action2
        self.nb_ac_a_eff0=0
        self.nb_ac_a_eff1=0
        self.nb_ac_a_eff2=0
        self.nb_ac_a_eff3=0
        self.nb_tour-=1
        self.tourde=0
        if self.nb_tour!=0:
            self.planification(0)
        else:
            resultat=self.fin()
            if resultat[1]!=0:
                mon_jeu.scrollbar(f"{resultat[0]} à gagné avec {resultat[1]}")
            else:
                mon_jeu.scrollbar(f"personne n'à gagné")
            

            return

    def fin(self):
        for i in range(self.nb_joueur):
            for valeur in self.bandits[i].butin:
                self.bandits[i].valeur_butin+= valeur 
        max=0
        personne=""
        for i in range(self.nb_joueur):
            for i in range(self.nb_joueur):
                self.bandits[i].valeur_butin
                if max < self.bandits[i].valeur_butin:
                    max = self.bandits[i].valeur_butin
                    personne = self.bandits[i].name
        return [personne,max]


    def scrollbar(self,texte):
        self.liste.insert(END, texte)
        self.liste.place(x=1100,y=0)


    #que pour player0
    def buton_droit0(self):
        if self.nb_ac_a_eff0!=self.nb_action-1:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("droit")
        else:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("droit")
            self.delete_button(0)
            self.tourde+=1
            self.action()

    def buton_gauche0(self):
        if self.nb_ac_a_eff0!=self.nb_action-1:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("gauche")
        else:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("gauche")
            self.delete_button(0)
            self.tourde+=1
            self.action()

    def buton_haut0(self):
        if self.nb_ac_a_eff0!=self.nb_action-1:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("haut")
        else:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("haut")
            self.delete_button(0)
            self.tourde+=1
            self.action()

    def buton_bas0(self):
        if self.nb_ac_a_eff0!=self.nb_action-1:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("bas")
        else:
            self.nb_ac_a_eff0+=1
            self.bandits[0].action.append("bas")
            self.delete_button(0)
            self.tourde+=1
            self.action()


    
    #que pour player1
    def buton_droit1(self):
        if self.nb_ac_a_eff1!=self.nb_action-1:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("droit")
        else:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("droit")
            self.delete_button(1)
            self.tourde+=1
            self.action()

    def buton_gauche1(self):
        if self.nb_ac_a_eff1!=self.nb_action-1:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("gauche")
        else:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("gauche")
            self.delete_button(1)
            self.tourde+=1
            self.action()

    def buton_haut1(self):
        if self.nb_ac_a_eff1!=self.nb_action-1:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("haut")
        else:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("haut")
            self.delete_button(1)
            self.tourde+=1
            self.action()

    def buton_bas1(self):
        if self.nb_ac_a_eff1!=self.nb_action-1:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("bas")
        else:
            self.nb_ac_a_eff1+=1
            self.bandits[1].action.append("bas")
            self.delete_button(1)
            self.tourde+=1
            self.action()
    


    #pour le player2
    def buton_droit2(self):
        if self.nb_ac_a_eff2!=self.nb_action-1:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("droit")
        else:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("droit")
            self.delete_button(2)
            self.tourde+=1
            self.action()
            
    def buton_gauche2(self):
        if self.nb_ac_a_eff2!=self.nb_action-1:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("gauche")
        else:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("gauche")
            self.delete_button(2)
            self.tourde+=1
            self.action()

    def buton_haut2(self):
        if self.nb_ac_a_eff2!=self.nb_action-1:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("haut")
        else:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("haut")
            self.delete_button(2)
            self.tourde+=1
            self.action()

    def buton_bas2(self):
        if self.nb_ac_a_eff2!=self.nb_action-1:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("bas")
        else:
            self.nb_ac_a_eff2+=1
            self.bandits[2].action.append("bas")
            self.delete_button(2)
            self.tourde+=1
            self.action()
    


    #pour le player3
    def buton_droit3(self):
        if self.nb_ac_a_eff3!=self.nb_action-1:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("droit")
        else:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("droit")
            self.delete_button(3)
            self.tourde=+1
            self.action()
            
    def buton_gauche3(self):
        if self.nb_ac_a_eff3!=self.nb_action-1:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("gauche")
        else:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("gauche")
            self.delete_button(3)
            self.tourde=+1
            self.action()

    def buton_haut3(self):
        if self.nb_ac_a_eff3!=self.nb_action-1:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("haut")
        else:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("haut")
            self.delete_button(3)
            self.tourde=+1
            self.action()

    def buton_bas3(self):
        if self.nb_ac_a_eff3!=self.nb_action-1:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("bas")
        else:
            self.nb_ac_a_eff3+=1
            self.bandits[3].action.append("bas")
            self.delete_button(3)
            self.tourde=+1
            self.action()



    def cree_button(self,i):
        if i==0:
            self.b00.place(x=90,y=350)
            self.b10.place(x=50,y=350)
            self.b20.place(x=70,y=330)
            self.b30.place(x=70,y=350)
        if i==1:
            self.b01.place(x=260,y=350)
            self.b11.place(x=220,y=350)
            self.b21.place(x=240,y=330)
            self.b31.place(x=240,y=350)
        if i==2:
            self.b02.place(x=430,y=350)
            self.b12.place(x=390,y=350)
            self.b22.place(x=410,y=330)
            self.b32.place(x=410,y=350)
        if i==3:
            self.b03.place(x=600,y=350)
            self.b13.place(x=560,y=350)
            self.b23.place(x=580,y=330)
            self.b33.place(x=580,y=350)

    def delete_button(self,i):
        if i==0:
            self.b00.place_forget()
            self.b10.place_forget()
            self.b20.place_forget()
            self.b30.place_forget()
        if i==1:
            self.b01.place_forget()
            self.b11.place_forget()
            self.b21.place_forget()
            self.b31.place_forget()
        if i==2:
            self.b02.place_forget()
            self.b12.place_forget()
            self.b22.place_forget()
            self.b32.place_forget()
        if i==3:
            self.b03.place_forget()
            self.b13.place_forget()
            self.b23.place_forget()
            self.b33.place_forget()
        pass

    def verif_butin(self,i):
        for k in range(len(self.butins)):
            if self.bandits[i].x == self.butins[k].x and self.bandits[i].y == 140:
                mon_jeu.scrollbar(f"{self.bandits[i].name} a récupéré un butin")
                self.bandits[i].butin.append(self.butins[k].valeur)
                self.butins[k].supprimer_butin()
                self.butins[k]=Butin(self,400,400,"rien",-100,165,ImageTk.PhotoImage(Image.open(chemin_absolu+"bijou.png").resize((40,30))))
    
    def verif_Marshall(self):
        for i in range(self.nb_joueur):
            if self.bandits[i].x == self.marshall.x and self.bandits[i].y ==140:
                if len(self.bandits[i].butin)!=0:
                    valeur=randint(0,len(self.bandits[i].butin)-1)

                    if self.bandits[i].butin[valeur]==100 or self.bandits[i].butin[valeur]==200:
                        self.bandits[i].butin.pop(valeur)
                        self.butins.append(Butin(self,40,40,"bource",self.bandits[i].x,165,ImageTk.PhotoImage(Image.open(chemin_absolu+"bource.png").resize((35,35)))))
                        mon_jeu.scrollbar(f"{self.bandits[i].name} a laché une bource")
                    elif self.bandits[i].butin[valeur]==500:
                        self.bandits[i].butin.pop(valeur)
                        self.butins.append(Butin(self,40,40,"bijou",self.bandits[i].x,165,ImageTk.PhotoImage(Image.open(chemin_absolu+"bijou.png").resize((40,30)))))
                        mon_jeu.scrollbar(f"{self.bandits[i].name} a laché une bijou")
                    elif self.bandits[i].butin[valeur]==1000:
                        self.bandits[i].butin.pop(valeur)
                        self.butins.append(Butin(self,40,40,"magot",self.bandits[i].x,165,ImageTk.PhotoImage(Image.open(chemin_absolu+"magot.png").resize((60,32)))))
                        mon_jeu.scrollbar(f"{self.bandits[i].name} a laché une magot")
                self.bandits[i].deplacement_haut()
    

    def coord_possible(self):
        self.x1=40
        for i in range(self.nb_wagons):
            self.coord.append(self.x1)
            self.coord.append(self.x1+30)
            self.coord.append(self.x1+60)
            self.x1+=170
        self.coord.append(self.x1+20)

    def generer_butin(self):
        for i in range(randint(self.nb_wagons,self.nb_wagons*2)):
            tempo_x=self.coord[randint(0,len(self.coord)-2)]
            if tempo_x not in self.butin_x: #self.img=ImageTk.PhotoImage(Image.open(chemin_absolu+"bandit.png").resize((35,65)))
                if randint(0,1)==1:
                    self.butins.append(Butin(self,40,40,"bource",tempo_x,165,ImageTk.PhotoImage(Image.open(chemin_absolu+"bource.png").resize((35,35)))))
                else:
                    self.butins.append(Butin(self,40,40,"bijou",tempo_x,165,ImageTk.PhotoImage(Image.open(chemin_absolu+"bijou.png").resize((40,30)))))
                self.butin_x.append(tempo_x)
        self.butins.append(Butin(self,40,40,"magot",self.coord[-1],180,ImageTk.PhotoImage(Image.open(chemin_absolu+"magot.png").resize((60,32)))))
    
    def afficher_wagons(self):
        self.img = ImageTk.PhotoImage(Image.open(chemin_absolu+"wagon.png"))
        self.wi = self.img.width()
        self.hi = self.img.height()
        for i in range(self.nb_wagons):
            self.C = Canvas(self,bg="#1e1e1e",highlightthickness=0)
            self.C.create_image(self.wi/2 ,self.hi/2 ,image=self.img,)
            self.C.place(x=self.wi*i+10, y = 100)

    def afficher_locomotive(self):
        self.img2 = ImageTk.PhotoImage(Image.open(chemin_absolu+"loco.png"))
        self.C2 = Canvas(self,bg="#1e1e1e",highlightthickness=0)
        self.C2.create_image(self.wi ,self.hi/2 ,image=self.img2,)
        self.C2.place(x=self.wi*self.nb_wagons+10, y = 100)
    


class Bandit(Canvas):
    def __init__(self,fenetre:Tk,width, height,nom,x,y,butin,valeur_butin,action,coord,img):
        super().__init__(fenetre,width= width, height =height)
        self.name=nom
        self.x=x
        self.y=y
        self.butin=butin
        self.valeur_butin=valeur_butin
        self.action=action
        self.coord=coord
        self.img=img
        self.C = Canvas(bg="green")
        self.afficher_bandit(self.x,self.y)


    def afficher_bandit(self,x,y):
        wi = self.img.width()
        hi = self.img.height() 
        self.C['width'] = wi
        self.C['height'] = hi
        self.C.create_image(wi/2 ,hi/2 ,image=self.img,)
        self.C.place(x=x, y = y)

    def supprimer_bandit(self):
        self.C.place_forget()
        self.C.delete()


    def deplacement_gauche(self):
        self.supprimer_bandit()
        if self.x!=40:
            mon_jeu.scrollbar(f"{self.name} se deplace vers la gauche.")
            self.x=self.coord[self.coord.index(self.x)-1]
        else:
            mon_jeu.scrollbar(f"{self.name} ne bouge pas")
        self.afficher_bandit(self.x,self.y)

    def deplacement_droite(self):
        self.supprimer_bandit()
        if self.x in self.coord and self.x != self.coord[-1]:
            mon_jeu.scrollbar(f"{self.name} se deplace vers la droite.")
            self.x=self.coord[self.coord.index(self.x)+1]
        else:
            mon_jeu.scrollbar(f"{self.name} ne bouge pas")
        self.afficher_bandit(self.x,self.y)

    def deplacement_haut(self):
        self.supprimer_bandit()
        if self.y==140:
            mon_jeu.scrollbar(f"{self.name} monte.")
            self.y=50
        else:
            mon_jeu.scrollbar(f"{self.name} ne bouge pas")
        self.afficher_bandit(self.x,self.y)

    def deplacement_bas(self):
        self.supprimer_bandit()
        if self.y==50:
            mon_jeu.scrollbar(f"{self.name} descend.")
            self.y=140
        else:
            mon_jeu.scrollbar(f"{self.name} ne bouge pas")
        self.afficher_bandit(self.x,self.y)

class Marshall(Canvas):
    def __init__(self,fenetre:Tk,width, height,x,y,coord):
        super().__init__(fenetre,width= width, height =height)
        self.x=x
        self.y=y
        self.coord=coord
        self.img = ImageTk.PhotoImage(Image.open(chemin_absolu+"marshall.png").resize((35,65))) #a changer
        self.C = Canvas(bg="blue")
        self.afficher_Marshall(self.x,self.y)
    
    def mouvement_Marshall(self):
        #de [0 a 4] il va a gauche | de ]4 a 9]  | 10 ne fais rien
        rand=randint(0,10)
        if rand<=4:
            self.deplacement_gauche()
        elif rand>4 and rand<=9:
            self.deplacement_droit()
        else:
            mon_jeu.scrollbar(f"Marshall ne se deplace pas")
        

    def afficher_Marshall(self,x,y):
        wi = self.img.width()
        hi = self.img.height() 
        self.C['width'] = wi
        self.C['height'] = hi
        self.C.create_image(wi/2 ,hi/2 ,image=self.img,)
        self.C.place(x=x, y = y)

    def supprimer_Marshall(self):
        self.C.place_forget()

    def deplacement_gauche(self):
        self.supprimer_Marshall()
        if self.x!=40:
            self.x=self.coord[self.coord.index(self.x)-1]
            mon_jeu.scrollbar(f"Marshall se deplace vers la gauche")
        else:
            mon_jeu.scrollbar(f"Marshall ne se deplace pas")
        self.afficher_Marshall(self.x,self.y)

    def deplacement_droit(self):
        self.supprimer_Marshall()
        if self.x in self.coord and self.x != self.coord[-1]:
            mon_jeu.scrollbar(f"Marshall se deplace vers la droite")
            self.x=self.coord[self.coord.index(self.x)+1]
        else:
            mon_jeu.scrollbar(f"Marshall ne se deplace pas")
        self.afficher_Marshall(self.x,self.y)

class Butin(Canvas):
    def __init__(self, fenetre:Tk, width, height, name, x, y, img):
        super().__init__(fenetre, width=width, height=height)
        self.val=[100,200,500,1000]
        self.name=name
        self.valeur=0
        self.x=x
        self.y=y
        self.img = img
        self.C = Canvas(bg="red")
        self.afficher_butin(self.x,self.y)
        self.add_valeur()
    
    def add_valeur(self):
        if self.name=="bource":
            self.valeur=self.val[randint(0,1)]
        elif self.name=="bijou":
            self.valeur=self.val[2]
        elif self.name=="magot":
            self.valeur=self.val[3]
        else:
            self.valeur=0


    def afficher_butin(self,x,y):
        wi = self.img.width()
        hi = self.img.height()
        self.C['width'] = wi
        self.C['height'] = hi
        self.C.create_image(wi/2 ,hi/2 ,image=self.img,)
        self.C.place(x=x, y = y)

    def supprimer_butin(self):
        self.C.place_forget()
        self.C.delete()


mon_jeu = Jeu()
mon_jeu.geometry("1400x400")
mon_jeu.configure(bg="#1e1e1e")
#mon_jeu.resizable(False,False)
mon_jeu.title("colt Express")
mon_jeu.mainloop()