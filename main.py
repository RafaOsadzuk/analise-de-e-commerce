from data.Dados import TratativasAmazon
from analysis.Analisador import AnalisadorAmazon

def main():
    # 1. Pipeline de Engenharia (ETL)
    print("Processando e limpando dados...")
    processador = TratativasAmazon("data/Amazon_Sales.csv")
    processador.carregar_dados()
    processador.transformar_dados()

    analisador = AnalisadorAmazon(processador.df)

    print("\n--- Insights de Negócio ---")

    ticket = analisador.calcula_ticket_medio()
    print(f"Ticket Médio: INR {ticket:.2f}")

    print(f"Categoria Mais Vendida: {analisador.produto_mais_vendido()}")
    print(f"Cidade com Mais Vendas: {analisador.cidade_com_mais_vendas()}")

    print("\nTop 3 Meses com Maior Faturamento:")
    print(analisador.meses_com_maior_venda())

    print("\nAmostra da Classificação de Pedidos (1 = Alto, 0 = Normal):")
    # Imprime apenas as 5 primeiras linhas da série retornada
    print(analisador.classificar_pedidos().head())

    print("\n--- Exportação ---")
    if analisador.exportar_dados_tratados():
        print("Base final exportada com sucesso para a pasta 'reports/'.")
        print("Pronta para ser consumida em dashboards ou planilhas!")

if __name__ == "__main__":
    main()