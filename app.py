alunos = []

# Entrada de dados
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ").strip()
    while not nome:
        nome = input("Nome não pode ser vazio. Digite novamente: ").strip()
    
    while True:
        try:
            idade = int(input(f"Digite a idade de {nome}: ").strip())
            if idade < 0:
                print("Idade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro para a idade.")
    
    alunos.append({"nome": nome, "idade": idade})

# Encontrar o aluno mais velho
mais_velho = max(alunos, key=lambda x: x["idade"])
maior_idade = mais_velho["idade"]

# Listar todos que têm a maior idade (em caso de empate)
mais_velhos = [a["nome"] for a in alunos if a["idade"] == maior_idade]

# Saída
if len(mais_velhos) == 1:
    print(f"O aluno mais velho é {mais_velho['nome']}, com {maior_idade} anos.")
else:
    print("Os alunos mais velhos são " + ", ".join(mais_velhos) + f", com {maior_idade} anos.")
