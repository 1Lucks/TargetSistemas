import json
with open('dados.json', 'r') as file:
    dados = json.load(file)

fatura = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor = fatura[0]
maior = fatura[0]

for valor in fatura:
    if valor < menor:
        menor = valor

for valor in fatura:
    if valor > maior:
        maior = valor

media = sum(fatura) / len(fatura)

acima = sum(1 for valor in fatura if valor > media)

print(f"O menor valor de faturamento foi: R$ {round(menor,2)}")
print(f"O maior valor de faturamento foi: R$ {round(maior,2)}")
print(f"O número de dias com faturamento acima da média foi: {acima}")
