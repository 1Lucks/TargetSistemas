valores = [6783643, 3667866, 2922988, 2716548, 1984953]
estados = ['SP', 'RJ', 'MG', 'ES', 'Outros']
total = 6783643 + 3667866 + 2922988 + 2716548 + 1984953
for x in range(5):
    porc = (valores[x] / total) * 100
    print(f"{estados[x]} representa {round(porc, 2)}%")
