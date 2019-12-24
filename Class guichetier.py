# Made by yawa matima modeste

class Guichetier :

   
    
  def __init__(self,matricule,nom,telephone,solde,solde_courant):
      
         self.matricule=matricule
         self.nom=nom
         self.telephone=telephone
         self.solde=solde
         self.solde_courant=solde_courant

         print("le solde de", nom, "est :", solde)

  def    versement (self):
         sum=float(input("Entrer le montant du versement:"))
         print("versement de:", sum, "sur le compte de :", self.nom)
         self.solde=self.solde + sum
         print("nouveau solde:", self.solde)

  def    retrait (self):
         sum=float (input(" Entrer le montant à retirer"))
         if sum>self.solde:
            print(" Solde Insuffisant")
         else:
            self.solde=self.solde-sum
            print("Retrait de :", sum, "sur le compte de:", self.nom)
            print("Votre Nouveau Solde est:", self.solde)
    
    
  def    virement(self):
         sum=float(input("Entrer le montant du virement"))
         print("virement de :", sum, "vers le compte :", self.nom)
         if sum> self.solde:
           print ("Solde insuffisant")
         else:
            self.solde= self.solde-sum
            print("Votre nouveau solde est:", self.solde)
            
  def operation_internationale (self):
         sum=float(input("Entrer le montant d'operation"))
         if sum>self.solde:
            print("Solde Insuffisant")
         else:
            self.solde=self.solde-sum
            print("Operation effectuée avec success")
            print("Votre Nouveau solde est:", self.solde)
       
  def emprunt(self):
           sum=float(input("Veuiller entrer le montant avec un taux de 10℅ d'emprunt"))
           if sum>self.solde_courant:
             print("Enprunt Impossible")
           else:
            self.solde_courant=self.solde_courant-sum
            print("Emprunt effectue avec success")
            print("Votre nouveau solde est:", self.solde)
        
            
        
  def modificatio(self):
            print("Informations sur le client", self.nom)
            self.matricule=int(input("Entrer le matriculet"))
            self.nom=input("Entrer le nom")
            self.telephone=int(input("Entrer ne numero de telephone"))
            print("Les informations sont: \n matricule:", self.matricule,"\n nom: ", self.nom ," \n telephone:", self.telephone)
            c=Guichetier(7, "YAWA MATIMA", 20, 10000)
            c.versement()
            c.retrait()
            print("Le solde de ",c.nom, "est de", c.solde)
   
    
    
        
