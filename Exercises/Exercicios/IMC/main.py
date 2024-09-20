'''
Psi - Mod 2
Anthony Fuzinato
Exercicio IMC
20/10/23
'''

# input

peso = float (input("Qual o seu peso? "))
altura = float (input("Qual a sua altura? "))

#processamento

IMC = peso / (altura * altura)

#output

print(IMC)

# Niveis de IMC
if (IMC >= 18.6):
    print("Voce está magro")
if (IMC >= 18.7 ) and (IMC <= 24.9):
    print("Voce está no peso ideal ")
if (IMC >= 30) and (IMC <= 34.9):
    print("Voce está com grau I de obesidade (Cuidado)")
if (IMC >= 35) and (IMC >= 39,9):
    print("Voce esta no grau de obesidade II (Severo)")
if (IMC >= 40):
    print("Voce esta no grau de obesidade III (Morbido)")


