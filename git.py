n = int(input("Digite quantos numeros quer na sequencia: "))
ant = 0
prox = 1
for i in range(0,n):
    print(ant)
    prim = ant
    ant = prox
    prox += prim
    
