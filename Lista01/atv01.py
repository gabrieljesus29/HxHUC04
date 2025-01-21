#Faça um programa em Python que  calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
 
# idade = int(input('Digite sua idade: '))
# ano_atual = int(input('Digite o ano atual: '))
# resposta = ano_atual - idade
# print (f'Seu ano de nascimento é {resposta}.')
 
# Crie um programa que receba um número inteiro digitado pelo usuário e informe se ele é par ou ímpar.
# num1 = int(input('informe um numero inteiro de sua preferencia: '))
# if (num1%2==0):
#     print('o numero é par')
# else:
#     print('o numero é impar')
 
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
# valorA = int(input("Digite o valor A:"))
# valorB = int(input("Digite o valor B:"))
# if(valorA%valorB==0) or (valorB%valorA==0):
#     print(f"Os valores {valorA} e {valorB} são múltiplos. ")
# else:
#     print(f"Os valores {valorA} e {valorB} não são múltiplos. ")
 
#Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7. Construa um programa que leia um número inteiro positivo e determine se ele é primo ou não.  
 
# numero = int(input("Digite o número inteiro: "))
# contador = 0
 
# for i in range (1,numero+1):
#     if (numero % i == 0):
#         contador = contador+1
#     print(i)
# if(contador==2):    
#     print (f'O número {numero} é primo')
# else:
#     print(f'O número {numero} não é primo')
 
#Elabore um programa que, dado um valor de temperatura (em graus Celsius), informe se o clima é "frio" (abaixo de 15°C), "ameno" (entre 15°C e 30°C, inclusive) ou "quente" (acima de 30°C).
# Entrada: Um valor numérico representando a temperatura.
# Saída: Uma mensagem classificando o clima como "frio", "ameno" ou "quente".
 
# numero = float(input('Digite a temperatura:'))
# if (numero<15):
#     print(f'Clima Frio {numero}')
# elif(numero>=15 and numero<=30):
#     print(f'Clima Ameno {numero}')
# else:
#     print(f'Clima Quente {numero}')
 
# Escreva um programa que calcule o valor final de uma compra, aplicando um desconto de 10% caso o valor da compra seja maior que R$100.
# Entrada: O valor total da compra antes do desconto.
# Saída: O valor final da compra, formatado com duas casas decimais.
 
# Quest 06
# valorCompra = float(input('Digite o valor total da compra: '))
# if(valorCompra>100):
#     #novoValor = valorCompra - valorCompra*0.1
#     valorCompra*=0.9
#     print(f'Novo Valor com desconto = {valorCompra}')
# else:
#     print(f'O desconto não pode ser aplicado. Total = {valorCompra}') 

# Quest 07

# for numero in range(1, 101):
#     print(numero)

# Quest 08

# for numero in range(200, 0, -1):
#     print(numero)

# Quest 09

# idades_soma = 0
# while True:
#     idade = int(input("Sua Idade (pra para digite 0):  "))
#     if idade == 0:
#         break
#     idades_soma+=idade
# print(idades_soma)

# Quest 10

# frase = (input("Digite sua frase: "))
# palavras = frase.split()
# print(f'A frase tem {len(palavras)} palavras.')

# Quest 11

#produtos = []
#while True:
#    entrada = input("Produto: ")
#    valor = input("Preço: ")
#    quantidade = input("Unidades: ")
#    if entrada == 'sair':
#        break
#    produtos.append ({"Produto": entrada, "Preço" : valor, "Unidades": quantidade})
   
#print(produtos)

#Quest 12

# def validar_cpf(cpf):
#     if len(cpf) == 11 and cpf.isdigit():
#         return "CPF válido"
#     else:
#         return "CPF inválido"

# cpf_usuario = input("Digite o CPF: ")

# print(validar_cpf(cpf_usuario))

#Quest 13

# soma_pares = 0
# while True:
#     numero = int(input("Digite um número (0 para parar): ")) 
#     if numero == 0:
#         break
#     if numero % 2 == 0:
#         soma_pares += numero

# print("Soma dos números pares:", soma_pares)

#Quest 14

# import random
# nomes = []
# while True:
#     nome = input("Digite um nome (ou 'sair' para finalizar): ")
#     if nome.lower() == "sair":
#         break
#     nomes.append(nome)

# if nomes:
#     nome_sorteado = random.choice(nomes)
#     print("O nome sorteado foi:", nome_sorteado)
# else:
#     print("Nenhum nome foi inserido.")

# Quest 15

# def validar_senha(senha):
#     if len(senha) < 8:
#         return "Senha inválida"
#     if not any(char.isdigit() for char in senha):
#         return "Senha inválida"
    
#     return "Senha válida"

# senha = input("Digite a senha: ")
# print(validar_senha(senha))

# Quest 16

# def calcular_media_turma():
#     notas = []
#     while True:
#         entrada = input("nota do aluno (ou 'sair' para terminar): ")
        
#         if entrada.lower() == "sair":
#             break
        
#         try:
#             nota = float(entrada)
#             if 0 <= nota <= 10:
#                 notas.append(nota)
#             else:
#                 print("A nota é entre 0 e 10. Tente novamente.")
#         except ValueError:
#             print("Entrada inválida. Digite um número ou 'sair'.")
    
#     if notas:
#         media = sum(notas) / len(notas)
#         print(f"A média da turma é: {media:.2f}")
#     else:
#         print("Nenhuma nota foi registrada.")

# calcular_media_turma()

# Quest 17

# palavra = input("Digite uma palavra: ").lower() 
# vogais = "aeiou"
# contador = 0

# for letra in palavra:
#     if letra in vogais:
#         contador += 1

# print(f"O número total de vogais é: {contador}")

# Quest 18

# numero = int(input("Digite um número: "))
# soma_divisores = 0

# for i in range(1, numero):
#     if numero % i == 0: 
#         soma_divisores += i

# if soma_divisores == numero:
#     print("Número Perfeito")
# else:
#     print("Não é Perfeito")

# Quest 19

# numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
# produto = 1

# for numero in numeros:
#     produto *= numero

# print(f"O produto dos números é: {produto}")

# Quest 20
lista_presenca = []

while True:
    nome = input("Digite um nome (ou 'sair' para finalizar): ")
    
    if nome.lower() == 'sair':
        break
    
    lista_presenca.append(nome)

palavra_busca = input("Digite a palavra a ser buscada: ").lower()

nomes_encontrados = []

for nome in lista_presenca:
    if palavra_busca in nome.lower():
        nomes_encontrados.append(nome)

if nomes_encontrados:
    print("Os nomes que contêm a palavra '{}' são:".format(palavra_busca))
    for nome in nomes_encontrados:
      print(nome)

else:
    print("Nenhum nome contém a palavra '{}'.".format(palavra_busca))