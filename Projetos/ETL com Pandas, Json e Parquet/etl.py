import pandas as pd
import os
import glob


# Uma função de extract que lê e consolida os json

pasta = 'data'
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) # A função glob.glob retorna uma lista de arquivos que correspondem ao padrão fornecido. Neste caso, ele retorna uma lista de todos os arquivos .json no diretório data.
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# -> extrair_dados_e_consolidar(pasta)

# Uma função que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# -> calcular_kpi_de_total_de_vendas(extrair_dados_e_consolidar(pasta))

# Uma função que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser ou "CSV ou "parquet" ou "os dois"
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados_csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")

# -> carregar_dados(calcular_kpi_de_total_de_vendas(extrair_dados_e_consolidar(pasta)),["csv","parquet"])

def pipeline_calcular_kpi_de_vendas_consolidade(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)



 
 
 
 
 
 
 
if __name__ == "__main__":

    pasta_argumento: str = 'data'
    df_total = extrair_dados_e_consolidar(pasta=pasta_argumento)
    print(calcular_kpi_de_total_de_vendas(df_total))

