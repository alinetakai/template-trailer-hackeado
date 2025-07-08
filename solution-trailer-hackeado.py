# Sinopse bagunçada
sinopse = """
[0001]::|>✨Prepare-se para uma aventura épica no espaço profundo!<|::[fim]
[0002]::|>✨Personagens cativantes e cenas de tirar o fôlego te aguardam.<|::[fim]
[0003]::|>✨Estreia mundial em breve. Você não pode perder!<|::[fim]
"""

# Usamos fatiamento com base em posições fixas de cada linha
linha1 = sinopse[14:66]   # Começa após o primeiro '✨' e vai até antes do '<'
linha2 = sinopse[81:138]  # Índices ajustados manualmente para a segunda linha
linha3 = sinopse[153:202] # Índices para a terceira linha

# Exibindo a sinopse formatada
print("🎥 Sinopse Oficial:")
print(linha1)
print(linha2)
print(linha3)
