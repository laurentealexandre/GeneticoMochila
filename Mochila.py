import random

def algoritmo_genetico_mochila(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes):
    def criar_individuo():
        return [random.randint(0, 1) for _ in range(len(pesos_e_valores))]

    def fitness(individuo):
        peso_total = sum(pesos_e_valores[i][0] * gene for i, gene in enumerate(individuo))
        if peso_total > peso_maximo:
            return 0
        return sum(pesos_e_valores[i][1] * gene for i, gene in enumerate(individuo))

    def selecao(populacao):
        return random.choices(
            populacao,
            weights=[fitness(ind) for ind in populacao],
            k=2
        )

    def cruzamento(pai1, pai2):
        ponto = random.randint(1, len(pai1) - 1)
        filho = pai1[:ponto] + pai2[ponto:]
        return filho

    def mutacao(individuo):
        for i in range(len(individuo)):
            if random.random() < 0.01:
                individuo[i] = 1 - individuo[i]
        return individuo

    populacao = [criar_individuo() for _ in range(numero_de_cromossomos)]
    melhores_unicos = []

    for _ in range(geracoes):
        nova_populacao = []
        for _ in range(numero_de_cromossomos):
            pai1, pai2 = selecao(populacao)
            filho = cruzamento(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)
        
        populacao = nova_populacao
        
        
        for individuo in populacao:
            valor_fitness = fitness(individuo)
            if [valor_fitness, individuo] not in melhores_unicos:
                melhores_unicos.append([valor_fitness, individuo])
        
        
        melhores_unicos.sort(key=lambda x: x[0], reverse=True)
        melhores_unicos = melhores_unicos[:5]

    return melhores_unicos

# Valores de uso
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300],
                   [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

resultado = algoritmo_genetico_mochila(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)


print("[")
for i, (fitness, individuo) in enumerate(resultado):
    print(f"    [{fitness:.2f}, {individuo}]{',' if i < len(resultado) - 1 else ''}")
print("]")