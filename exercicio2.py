a = 1
b = 0
c = 0
vetor = []
n = int(input("Digite um número: "))
for x in range(100):
    vetor.append(c)
    c = a + b
    a = b
    b = c
for x in range(100):
    if vetor[x]==n:
        a = 1
        
if a==1:
    print(f"O número {n} está na sequência de Fibonacci")
else:
    print(f"O número {n} não está na sequência de Fibonacci")
