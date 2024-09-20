'''
Psi - Mod 2
Anthony Fuzinato
Exercicio
20/10/23
'''

# input
nota1 = float(input("Introduza a nota do aluno (0-20): "))

# testar se é uma nota é invalida

if (nota1<0) or (nota1>20):
    print("A nota nao é valida")

else: # Teste Logico
    if (nota1 >= 9.5):
        print("O aluno está aprovado") 
        if (nota1>= 9.5) and (nota1 <=13,5):
            print("O aluno teve suficiente")
        elif (nota1 >= 13,5) and (nota1 <= 17.5):
            print("O aluno teve bom")
        elif (nota1 >= 17,5) and (nota1 <= 20):
            print("O aluno teve muito bom")
    else: 
        print("O aluno está reprovado")
        print("O aluno tera de fazer o exame")
