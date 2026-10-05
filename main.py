import pandas as pd
from data.Dados import TratativasAmazon
from analysis.Analisador import AnalisadorAmazon
from reports.Visualizador import VisualizadorAmazon

def main():
    # 1. Pipeline de Engenharia (ETL)
    print("Processando e limpando dados...")
    processador = TratativasAmazon("data/Amazon_Sales.csv")
    processador.carregar_dados()
    processador.transformar_dados()

    df_pronto = pd.read_csv("reports/Amazon_Sales_Clean.csv")
    visualizar = VisualizadorAmazon(df_pronto)
    visualizar.plotar_faturamento_mensal()
    visualizar.plotar_categorias()

"""    print("\n--- Exportação ---")
    if analisador.exportar_dados_tratados():
        print("Base final exportada com sucesso para a pasta 'reports/'.")
        print("Pronta para ser consumida em dashboards ou planilhas!")

    """

if __name__ == "__main__":
    main()