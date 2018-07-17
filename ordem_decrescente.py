##### POSSIBILIDADES ATRAVÉS DA ANÁLISE COMBINATÓRIA #####

#N1 > N2 > N3
#N1 > N3 > N2
#N2 > N1 > N3
#N2 > N3 > N1
#N3 > N1 > N2
#N3 > N2 > N1
#N1 == N2 == N3


n1=int(input("Insira o primeiro valor: "))
n2=int(input("Insira o segundo valor: "))
n3=int(input("Insira o terceiro valor: "))

if n1 > n2 > n3:
    print(n1, n2, n3)
if n1 > n3 > n2:
    print(n1,n3,n2)
if n2 > n1 > n3:
    print(n2,n1,n3)
if n2 > n3 > n1:
    print(n2,n3,n1)
if n3 > n1 > n2:
    print(n3,n1,n2)
if n3 > n2 > n1:
    print(n3,n2,n1)
if n1 == n2 == n3:
    print("INVALIDO!")

