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

def filtrar_produtos_nao_entregue(lista: list[dict]) -> list[dict]: 
    """
    Função que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == 'True':
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados
            
def somar_valores_dos_produtos(lista: list[dict]) -> int:
    """
    Função que soma os valores dos produtos que estão na lista
    """
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("price"))
    return valor_total



