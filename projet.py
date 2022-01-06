import random
e=0
d=0
b=0

print("à quelle jeux voulez vous jouer?")
print("taper 1 pour jouer à pierre feuille ciseaux")
a=int(input("taper 2 pour jouer au morpion:"))


if a==1:
    print("pour utiliser la pierre taper 1")
    print("pour utiliser feuille taper 2")
    print("pour utiliser le ciseaux taper 3")
    print("taper 4 pour arrêter")
    while b<4:
         b=int(input(":"))
         c=random.randint(1,3)
         
         
         if b==1 and c==2:
             e=e+1
             print("le bot a gagner en utilisant feuille re essayer")
         if b==1 and c==3:
            d=d+1
            print("vous avez gagner contre le bot qui a utiliser ciseaux!!")
         if b==2 and c==1 :
            d=d+1
            print("vous avez gagner contre le bot qui a utiliser pierre!!")
         elif b==2 and c==3 :
            e=e+1
            print("le bot a gagner en utilisant ciseaux re essayer")
         if b==3 and c==1:
             e=e+1
             print("le bot a gagner en utilisant pierre re essayer")
         elif b==3 and c==2:
            d=d+1
            print("vous avez gagner contre le bot qui a utiliser feuille!!")
         else :
            print("vous avez fait égaliter")
            
    print("Voici les scores:")
    print("vous avez un score de",d)
    print("le bot a un score de",e)
    
    
if a==2:
    cases_vides=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    x=int(input("coordonné de x"))
    y=int(input("coordonné de y"))
    p=x,y
    while not
    cases_vides.remove(p)
    
    
        
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       #print("  |  |  ")
        #print("  |  |  ")
        #print("  |  |  ")
        #print("pour placer votre rond il faut mettre le numero de la case ou vous voullez poser votre rond et taper 10 pour arrêté")
    
        #f=int(input("Où voulez vous poser votre rond: "))
              
        #if f==1 :
         #   print("0|  |  ")
          #  print(" |  |  ")
           # print(" |  |  ")
            #g=random.randint(2,9)
            
        #if f==2 :
       #     print
          
          
          
          
          
          
          
         
        