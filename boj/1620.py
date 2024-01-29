n, m = map(int, input().split())

pokemondict = {}
for i in range(n):
    pokemon = input()
    pokemondict[str(i + 1)] = pokemon
    pokemondict[pokemon] = str(i + 1)

questions = []
for _ in range(m):
    questions.append(input())

for q in questions:
    print(pokemondict[q])
