
import random
from queue import *
from threading import Thread
import time

enStock = Queue(100)#notre pile, qui peut contenir 100 elements max( 0 pour enlever la limite)

class producteur(Thread):

    def __init__(self):
        self.ouvert = True
        Thread.__init__(self)

    def run(self):
        while self.ouvert :

            while not enStock.full() :
                try :

                    enStock.put("ajout d'un paquet de chocolat",True,1000)
                    ### le producteur va ajouter un paquet dans le rayon, et s'il y a plus de place,
                    ### va attendre pendant 1 seconde qu'un paquet soit achete .
                except Full as e :
                    print( "Il n'y a pas de place pour un paquet !\n");

                else:
                    print( "On ajoute un paquet de chocolat dans le rayon\n")


            time.sleep(10)
            #temps de file d'attente


class Client(Thread):

    def __init__(self,achat,numero):
        self.achat = achat
        self.numero = numero
        Thread.__init__(self)



    def run(self):
        while self.achat :
            time.sleep(1)
            #le client arrive au bout d'une seconde au rayon

            ok=False
            paquet = random.randint(1,7)
            #nombre de paquet qu'il va prendre
            i=1
            print( "Le client n "+str(self.numero)+ " veut "+str(paquet)+ "paquet(s) de chocolat\n")
            while i<=paquet :
                try:
                    enStock.get(True,500)
                    ok = True
                    print( "n "+ str(self.numero) +  ": Prend un paquet\n")

                except Empty as e:
                    ok = False
                    break
                else:
                    i+=1
            if ok :
                print( "Il reste  "+ str( enStock.qsize() ) + " paquet(s) de chocolat\n")
            else :
                print( "n "+ str(self.numero) +  ": Il n'y a pas assez de paquets\n")
            self.jAiFaim = False

if __name__=='__main__':
    produit = producteur()
    produit.ouvert = True
    print("remplissage")
    produit.start()

    i=1
    while i < 100:
        Client(achat = True ,numero = i).start()
        i=i+1

    time.sleep(60)
    produit.ouvert=False
    print("##### Le magasin ferme ses portes #####")