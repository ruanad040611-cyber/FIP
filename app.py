import time
import pandas as pd
js = pd.read_json("FIP/dados.json")
print("-"*20)
print("        FIP")
print("-"*20)
print("\n")
print("Ben-Vindo(a) ao sistema FIP, o software vai ajudar você nesse trabalho!")
print("Cadastre cada item com duas opções receita e despesa exatamente como da escrito")
def sair():
    exit()
def saldo():
    receitas = js.loc[js['tipo'] == 'receita', 'valor'].sum()
    despesa = js.loc[js['tipo'] == 'despessa', 'valor'].sum()
    total = receitas - despesa
    print(f"Saldo Atual: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    time.sleep(0.5)
def tabela():
    print(js)
def receita():
    while True:
        escolha = input("""Escolha uma opção das opções abaixo
        1. Ver Receitas
        2. Soma das receitas 
        3. Maior valor
        4. Menor valor
        5. Média
        6. Sair
        """)
        if escolha == "1":
            ver_receita = js.loc[js['tipo'] == 'receita']
            print(ver_receita)
        elif escolha == "2":
            total_receita = js.loc[js['tipo'] == "receita", "valor"].sum()
            print(f"R$ {total_receita:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        elif escolha == "3":
            maior_valor = js.loc[js['tipo'] == 'receita'].max()
            print(maior_valor.to_string())
        elif escolha == "4":
            menor_valor = js.loc[js['tipo'] == 'receita'].min()
            print(menor_valor.to_string())
        elif escolha == "5":
            media_valor = js.loc[js['tipo'] == 'receita', 'valor'].mean()
            print(f"Média de Receitas: {media_valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        elif escolha == "6":
            inicio()
            break
        else:
            print("Digito inválido, Digite só números 1, 2, 3, 4, 5 e 6")
        time.sleep(0.5)
def despesa():
    while True:
        escolha = input("""Escolha uma opção das opções abaixo
        1. Ver Despesas
        2. Soma das despesas
        3. Maior valor
        4. Menor valor
        5. Média
        6. Sair
        """)
        if escolha == "1":
            ver_receita = js.loc[js['tipo'] == 'despesa']
            print(ver_receita)
        elif escolha == "2":
            total_despesa = js.loc[js['tipo'] == "despesa", "valor"].sum()
            print(f"R$ {total_despesa:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        elif escolha == "3":
            maior_valor = js.loc[js['tipo'] == 'despesa'].max()
            print(maior_valor.to_string())
        elif escolha == "4":
            menor_valor = js.loc[js['tipo'] == 'despesa'].min()
            print(menor_valor.to_string())
        elif escolha == "5":
            media_valor = js.loc[js['tipo'] == 'despesa', 'valor'].mean()
            print(f"Média de Receitas: {media_valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))    
        elif escolha == "6":
            inicio()
            break
        else:
            print("Digito inválido, Digite só números 1, 2 , 3, 4, 5 e 6")
        time.sleep(0.5)
def adicionar():
    novo_id = js["id"].max()+1
    tipo = input("Tipo: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: "))
    categoria = input("Categoria: ")
    data = input("Data: ")
    registro = {
        "id": novo_id,
        "tipo": tipo,
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    js.loc[len(js)] = registro
    js.to_json(
      "FIP/dados.json",
      orient="records",
      indent=3,
      force_ascii=False  
    )
    print("Feito")
    time.sleep(0.5)
def excluir():
    global js
    try:
        js = pd.read_json("FIP/dados.json")
        delete_id = int(input("Digite o id do item para deletar: "))
        print("Item deletado")
    except ValueError as i:
        print("Digite só números")
    else:
        js = js.loc[js["id"] != delete_id]
        js.to_json("FIP/dados.json", orient="records", indent=4)
        time.sleep(0.5)
def inicio():
    while True:
        escolha = input("""Escolha um dos números a seguir:
        1. Saldo
        2. Tabela
        3. Receitas
        4. Despesas
        5. Adicionar
        6. Excluir
        7. Sair
        """)
        if escolha == "1":
            saldo()
        elif escolha == "2":
            tabela()
        elif escolha == "3":
            receita()
        elif escolha == "4":
            despesa()
        elif escolha == "5":
            adicionar()
        elif escolha == "6":
            excluir()
        elif escolha == "7":
            print("Obrigado por usar o sistema")
            time.sleep(0.3)
            sair()
inicio()