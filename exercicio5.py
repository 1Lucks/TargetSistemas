palavra = str(input("Digite uma palavra: "))
invertida = ""
for x in range(len(palavra) -1, -1, -1):
    invertida = invertida + palavra[x]
print(f"A palavra {palavra} ao contrário é: {invertida}")
