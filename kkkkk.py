print("ola mundo")

nome= input("digite seu nome:")
print(nome)

idade = input("digite sua idade:")
if int(idade) >= 18:
    print("maior de idade")
    else:
        print("menor de idade")


numero = input('digite um numero:')   
if int(numero) % 2 = 0:     
    print('numero par')
    else:
        print('numero impar')


numero1 = input('digite um numero:') 
numero2 = input('digite outro numero:') 
numero3 = input('digite mais um numero:')
print('o maior numero é:' + max(int(numero1), int(numero2), int(numero3)))


nota = float(input('me de uma nota de 0 a 10:'))
if nota >= 6:
    print('aprovado')
    else:
        print('reprovado')


numero = input('digite um numero:')        
print('mostre a tabuada do numero:' + numero)


numeros = print('varios numeros:')
input('pare qaundo eu digitar 0:')



conte = float(input('conte de 1 até 100 usando for:'))
for i in range(1, 101):
    print(i)


numero = input('digite um numero:')
print(math.fatorial(int(numero)))


import random
import string

caracteres = string.ascii_letters + string.digits  # Caixa de letras e números
senha = ""  # Começa vazia

for i in range(4):  # Repetir 4 vezes
    senha += random.choice(caracteres)  # Adiciona um caractere aleatório

print(senha)


n1 = input('digite um numero:')
n2 = input('digite outro numero:')
n3 = input('digite mais um numero:')
n4 = input('digite outro numero:')
n5 = input('digite mais um numero:')
media = (int(n1) + int(n2) + int(n3) + int(n4) + int(n5)) / 5
print('a media é:' + str(media))


