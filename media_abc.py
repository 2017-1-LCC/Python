nome=(input("Informe o nome do aluno: "))
n1=int(input("Informe a nota da prova: "))
n2=int(input("Informe a nota do trabalho: "))
n3=int(input("Informe a nota do seminário: "))

media = (n1 + n2 + n3) /3

if  media >= 7:
    print(nome," APROVADO!")
elif media >=3 :
    nf = (50 - (media * 7))/3
    print(nome," precisa de tirar", nf, "na pova final!") 
elif media <3:
    print(nome," REPROVADO!")
    
