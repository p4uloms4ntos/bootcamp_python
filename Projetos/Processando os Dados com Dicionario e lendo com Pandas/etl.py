import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo CSV e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_arquivo_csv,mode="r",encoding="utf-8") as arquivo: # Estou abrindo o arquivo e transformando
        # para a variável arquivo. Só que essa variável é de um tipo, e vou usar para ler isso, o próprio módulo de CSV
        leitor = csv.DictReader(arquivo) # Usa a função csv.DictReader da biblioteca csv para criar um objeto leitor que itera 
        #sobre as linhas do arquivo CSV. Cada linha do CSV é lida como um dicionário onde as chaves são os cabeçalhos das colunas.
        for linha in leitor:
            lista.append(linha)
    return lista

vendas_itens = ler_csv(path_arquivo)

def filtrar_produtos_nao_entregue(lista: list[dict]) -> list[dict]: #
    produto_nao_entregue = []
    for item in lista:
        produto = item["produto"]
        entregue = item["entregue"]
        if entregue == 'False':
            produto_nao_entregue.append(produto)
        else:
            pass
            
    return produto_nao_entregue

def linhas_produtos_nao_entregue(lista: list[dict]) -> list[dict]:
    produtos_nao_entreguem = []
    for item in lista:
        if item["entregue"] == "False":
            produtos_nao_entreguem.append(item)
    return produtos_nao_entreguem
        
linhas_produtos_nao_entregue(vendas_itens)


    

    #for item in lista:
     #   entregue = item["entregue"]
        #produto = item.get["produto"]
      #  print(entregue)
    
    #return print(entregue)

filtrar_produtos_nao_entregue(vendas_itens)


vendas_itens

for item in vendas_itens:
    entregue = item["entregue"]
    print(entregue)



