'''
PSI - Modulo 1
Anthony Fuzinato
13-10-2023
Exercicio tecla 2018 (fase premiliniar)
'''

#Libraria Math
import math


#input
TamanhoPista = int(input("Qual o Tamanho da Pista? "))
NumeroVoltas = int (input("Qual o Numero de Voltas "))
ConsumoMedio = int(input("Qual o Consumo Medio do carro "))
CapacidadeDeposito = int(input("Qual a capacidade de deposito do carro? "))
#processamento
DistanciaProva = TamanhoPista * NumeroVoltas
GastoCombustivel = DistanciaProva * ConsumoMedio / CapacidadeDeposito
NumeroDepositos = math.ceil (GastoCombustivel / CapacidadeDeposito)
#output
print("Sao necessarios "+ str (NumeroDepositos) + " depositos para concluir a prova")
