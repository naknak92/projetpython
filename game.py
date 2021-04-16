import inquirer
import random
import os
import json
import os
import time
from PyInquirer import Separator, prompt
 

def clear():
    print("\n" * 100)


def loadingScreen():

    cmd = 'mode 60,46'
    os.system(cmd)


    print("Rap contenders")


def word():
    phrase =''
    list1 =['tu es', 'tu as ', 'tu allais ', 'tu grognes', "t'es", "t'as",'tu rales', 'tu bouffes', 'tu glandes']
    word1 = random.choice(list1)
    word2 = random.choice(list1)
    word3 = random.choice(list1)
    word4 = random.choice(list1)
    word =  [
        {
            'type': 'list',
            'name': 'word',
            'message':'Quels verbes voulait vous choisir? :',
            'choices': [
               word1,
               word2,
               word3,
               word4,

               
            ]
        }
    ]

    answers = prompt(word)
    phrase = phrase + ' ' + answers['word']


    list2 =['une', 'tes', 'ta', 'ton', 'des', 'les','le','la','un','ses','ces','du','mon','mes','ma','nos']
    word1 = random.choice(list2)
    word2 = random.choice(list2)
    word3 = random.choice(list2)
    word4 = random.choice(list2)
    word =  [
        {
            'type': 'list',
            'name': 'word',
            'message':'Quels determinants voulait vous choisir? :',
            'choices': [
               word1,
               word2,
               word3,
               word4,

               
            ]
        }
    ]

    answers = prompt(word)
    phrase = phrase + ' ' + answers['word']


    list3 =['grognasse', 'Banane', 'Patate', 'Andouille', 'Gros beta', 'Crapule','Chenapan','fripouille','zigoto','zgeg','flibustier','abruti','beauf','bougre','chnoque','debile','folle','fumier','glandeur','incapable']
    word1 = random.choice(list3)
    word2 = random.choice(list3)
    word3 = random.choice(list3)
    word4 = random.choice(list3)
    word =  [
        {
            'type': 'list',
            'name': 'word',
            'message':'Quels insultes voulait vous choisir? :',
            'choices': [
               word1,
               word2,
               word3,
               word4,

               
            ]
        }
    ]

    answers = prompt(word)
    phrase = phrase + ' ' + answers['word']

    len(phrase)

    return phrase


def Accueil():
         print(15 * '-')
         print("ACCUEIL")
         print(15 * '-')
         print("1. Combattre")
         print("2. Champions")
         print("3.Regle du jeu")
         print("4. Credits")
         print("5. Fuir")
         print(15 * '-')

         valid = False
         while(valid == False):

            choix = input('Que voulez-vous faire ?')

            choix = int(choix)

            if choix == 1:
                print("")               
                jeu()
                rejouer()
            

            elif choix == 2:
                Champions()
                print("")
                valid == True

            elif choix == 3:
                print("Ce jeu consiste à faire la meilleur insulte. Tout d'abord vous devez choisir votre Champions que vous vous voulez, vous avez le choix entre trois. Par la suite le Joueur1 fait sa phrase et ensuite le joueur2 l'a fait. Celui qui a la meilleure et la plus longue gagne.")
            
            elif choix == 4:
                print("Ce jeu a été concu en 1mois, par le biais de Rafael Nakache, Salim Bentefrit et Marvin Mezouani! J'èspere que vous avez apprecié notre jeu, ce n'est qu'une demo il va bien sur être ameliorer. Merci d'avoir jouer à notre beta!")
                valid == True 

            elif choix == 5: 
                print("Sale Peureux")
                valid == True            
                time.sleep(1)  
                quit() 


def Champions():
    sentence   =  ''
    score      =  0
    Champion1 = [
        {
            'type': 'list',
            'name': 'Champions',
            'message':'Choisissez votre personnage :',
            'choices': [
                'Marzau : Le loueur de gamos',
                'NakNak : Le lanceur de kipa', 
                'SaSaKalash : Le mythomane de montrueil',

               
            ]
        }
    ]
    Champion2 = [
        {
            'type': 'list',
            'name': 'Champions',
            'message':'Choisissez votre personnage :',
            'choices': [
                'Marzau : Le loueur de gamos',
                'NakNak : Le lanceur de kipa', 
                'SaSaKalash : Le mythomane de montrueil',

               
            ]
        }
    ]
  
    return prompt(Champion1)["Champions"], prompt(Champion2)["Champions"]


def jeu():
    champion1,champion2 = Champions()
    
    time.sleep(2)

    tour = 1
    phraseChampion1 = ''
    phraseChampion2 = ''
    clear()

    PremierJoueur = ((random.randint(1,2)))
    print('Le Champion1 commence')   
    player1 = PremierJoueur
    phraseChampion1= word()
    print('phrase du champion 1:' + phraseChampion1)

    deuxiemejoueur = ((random.randint(1,2)))
    print('Le Champion2 commence')
    player2 = deuxiemejoueur
    phraseChampion2= word()
    print('phrase du champion 2:' + phraseChampion2)

    points(phraseChampion1,phraseChampion2)


def rejouer():

    continuer = True
    while continuer == True :
        choix = input("Voulez vous rejouer ? ")
        if choix in('o', 'oui', 'ok'):
            continuer = False
            break

        
def points(phrase,phrase2): 
     score1,score2 = len(phrase),len(phrase2)
     print('Score du Champion 1 :', len(phrase)* 2)
     print('Score du Champion 2 :', len(phrase2)* 2)

     if score1 > score2:
         print("GG à toi champion1 tu as win ce battle")
     if score1 < score2:
         print("GG à toi champion2 tu as win ce battle")
     if score1 == score2:
         print("Match Nul! Rejouez pour savoir qui est le best!")
    
    





#loadingScreen()
Accueil()
#qefdhufsefi
#jfdhqeuifgze





   
