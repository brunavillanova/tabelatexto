def criar_tabela(dados):
    tabela = "+------+--------------+----------+\n"
    tabela += "| ID   | Nome         | Idade    |\n"
    tabela += "+------+--------------+----------+\n"

    for linha in dados:
        tabela += f"| {linha['ID']:4} | {linha['Nome']:<12} | {linha['Idade']:8} |\n"

    tabela += "+------+--------------+----------+"
    return tabela

dados = [
    {"ID": 1, "Nome": "João", "Idade": 28},
    {"ID": 2, "Nome": "Maria", "Idade": 32},
    {"ID": 3, "Nome": "Carlos", "Idade": 45},
    {"ID": 4, "Nome": "Ana", "Idade": 22}
]

tabela_texto = criar_tabela(dados)
print(tabela_texto)
