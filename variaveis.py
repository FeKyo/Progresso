#print("Hello World")

#nome = "Kyu"
#Profissão = "FullSail"
#print(type(nome))
#print(type(Profissão))

#y = 3
#x = 1
##print(type(x))
##print(type(y))
#print(x + y)

#pi = 3.1415
#print(type(pi))

#nandoéTop = True
#print(type(nandoéTop))

#a = 5+2j
#b = 20+6j
#print(type(a))
#print(type(b))
#print(complex(2, 5))

#lista = ["a", "b", "c"] são mutáveis, ou seja, podem ser editadas
#numeros = [2, 4]
#print(type(lista))
#print(type(numeros))

#valores = (1, 2, 4, 89, 24)
#pontos =(23.45, 67.5, 956.7)
#print(type(valores))
#print(type(pontos))

#altura = {"Erick": 1, "Nando": 2, "asdksa": 9}
#print(type(altura))
#print(altura)

#d = {1, 3, 4}
#c = {'fasd', 'sjdka'}
#print(type(c))
#print(type(d))

# Aritiméticos:
# + adição
# - subtração
# * multiplicação
# / divisão
# // divisão inteira
# % módulo
# ** exponenciação

#x = 4**1000
#print(x) 

# Atribuição:
# = equivalente a x = 1
# += equivalente x = x + 1
# -= equivalente x = x - 1
# *= equivalente x = x * 1
# /= equivalente x = x/1
# %= equivalente x = x%1

#pato = 5
#pato += 5
#print(pato)
#gato = 5
#gato *= 5
#gato /= 5
#print(gato)

# Comparação:
# == igual a
# != diferente de
# >  maior que
# >= maior ou igual que
# < menor que
# <= menor ou igual que

#pato = 1
#print(pato == 1)
#print(pato != 1)

#pato = 5
#if pato == 5: print("pato") 
#elif pato == 6: pato += 1
#if pato == 7: print("pato")
#else: print("gato")

#pato = 3
#while pato == 3: print("murilo")
#pato = 1
#while pato < 10: 
#    pato += 1
#    print("murilo")

#pato = 7
#for gato in range(10):
#    print(pato)
#for pato in range(10):
#    print(pato)

#Animais = ["Gato", "Rato", "Pato"] #esse aqui é LISTA
#Números = [1, 2, 3]
#tamanho_lista = len(Animais)
#índice = 0#para fazer o while funcionar
#
#print('Lista usando WHILE')
#while (índice < tamanho_lista):
#    print(Animais[índice], ':\t\t', Números[índice])
#    índice += 1
#print('Lista usando WHILE')
#while (índice < tamanho_lista):
#    print(f'{Animais[índice]} :  {Números[índice]}')
#    índice += 1
#
#print('Lista usando FOR')
#for Indice in range(tamanho_lista):
#    print(Animais[índice], ':\t\t', Números[índice])

#Animais = {"Gato": 1, "Rato": 2, "Pato": 3} #esse aqui é DICIONÁRIO
#print("\nLista usando FOR com DICIONÁRIO")
#for nome, número in Animais.items():
#    print (nome, "\t\t", número)

#def função():
#    print ("oi")
#função()

#def parametro(a):
#        print(a)
#parametro('café')
#def sum(a, b):
#      print (a + b)
#sum(1, 3)
#sum( "pato, ", "gato")
#
#def soma(a, b, c):
#    print ((a + b)* c)
#
#soma(1, 3, 6)
#soma(c=4, a = 2, b =9)

#def tabuada(a, b):
#      print (a * b)
#tabuada(a = 1, b = int(input("número")))

#def multiplicação():
#        a = int(input('Qual valor você deseja?\t'))
#        print(f'{a} X 1 = ' + str(a *1))   
#        print(f'{a} X 2 = ' + str(a *2))
#        print(f'{a} X 3 = ' + str(a *3))
#        print(f'{a} X 4 = ' + str(a *4))
#        print(f'{a} X 5 = ' + str(a *5))
#        print(f'{a} X 6 = ' + str(a *6))
#        print(f'{a} X 7 = ' + str(a *7))
#        print(f'{a} X 8 = ' + str(a *8))
#        print(f'{a} X 9 = ' + str(a *9))
#        print(f'{a} X 10 = ' + str(a *10))
#multiplicação()

def tabuada():
    x = 1
    a = int(input('Qual valor você deseja?\t'))
    while x != 11:
        print(f'{a} X {x} = {a*x}')
        x += 1
tabuada()
tabuada()