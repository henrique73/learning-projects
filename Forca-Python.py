#Henrique Erzinger Dousseau e Maycon Rafael Cruz Silva
import random
import re
import urllib.request

forca =["""
   +-----+
   |     |
   O     |
  /|\    |
  / \    |
         |
==========""",#0
"""
   +-----+
   |     |
   O     |
  /|\    |
  /      |
         |
==========""",#1
"""
   +-----+
   |     |
   O     |
  /|\    |
         |
         |
==========""",#2
"""
   +-----+
   |     |
   O     |
  /|     |
         |
         |
==========""",#3
"""
   +-----+
   |     |
   O     |
   |     |
         |
         |
==========""",#4
"""
   +-----+
   |     |
   O     |
         |
         |
         |
==========""",#5
"""
   +-----+
   |     |
         |
         |
         |
         |
=========="""]#6


Certas = ""
Erradas = ""

def site1():
    global listaNomes
    pagina = urllib.request.urlopen(
    'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt')
    texto = pagina.read().decode('utf8')
    listaNomes = (texto.split('\n'))

site1()
    
def escolhe():
    global Palavra
    numRandomico = (random.randint(0,(len(listaNomes))))
    print (listaNomes[numRandomico])
    Palavra = (listaNomes[numRandomico])
    return (listaNomes[numRandomico])

def comercar1():
    global campo
    global Certas
    global Erradas

    escolhe()
    campo = ["_ "]*(len(Palavra))
    Certas = ""
    Erradas = ""


comercar1()


def desenha():
    print(forca[6 - len(Erradas)])
    print (' '.join(campo))
    
def chute():
    global chuteUs
    chuteUs = str(input('Chute uma Letra : '))   
    s = ""
    s += Certas+Erradas
    while chuteUs.isdigit() or chuteUs in s or len(chuteUs) > 1 or set('`.,=-+/[~!@#$%^&*()_+{}":;\']+$').intersection(chuteUs):
        print ("Essa Letra já foi utilizada ou Não é uma letra")
        chuteUs = str(input('Chute uma Letra : '))        
    else:
        return chuteUs
            
def chute2(letra):
    global Erradas
    global Certas
    global Palavra
    if letra in Palavra:
        must_replace = [i for i, a in enumerate(Palavra) if a == letra]
        for x in must_replace:
          campo[x] = letra
        Certas += letra
        desenha()      
    else:
        Erradas += letra
        desenha()

def comecar():
    desenha()
    chute2(chute())


comecar()

def ganhou():
    counter2 = 0
    for i in Certas:
        if i not in Palavra:
           exit() 
        else:
            print ("Voce ganhou!")
            return True
            break
        
                
def jogar_novamente():
    Pergunta = str(input('Quer jogar novamente : '))  
    if Pergunta.lower() == "sim" or Pergunta.lower() == "yes":
        print ("-----------")
        comercar1()
        comecar()
    else:
        exit()


while len(Erradas) < 6:
    if '_ ' not in campo :
        ganhou()
        jogar_novamente()
    chute2(chute())
    if len(Erradas) > 5:
        print ("Voce Perdeu!")
        jogar_novamente()