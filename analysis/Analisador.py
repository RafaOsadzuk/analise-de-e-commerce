import pandas as pd
import numpy as np

class AnalisadorAmazon:
    def __init__(self, df_limpo):
        self.df = df_limpo


    def calcula_ticket_medio(self):
        return self.df.groupby('order_id')['amount'].sum().mean()

    def produto_mais_vendido(self):
        return self.df['category'].value_counts().index[0]

    def cidade_com_mais_vendas(self):

        return self.df['ship_city'].value_counts().index[0]

    def meses_com_maior_venda(self):
        # Agrupa pela data (mês) e soma a faturação (amount)
        # Retorna os 3 melhores meses, ordenados do maior para o menor
        return self.df.groupby(self.df['date'].dt.to_period('M'))['amount'].sum().sort_values(ascending=False).head(3)

    def classificar_pedidos(self):
        ticket_medio = self.calcula_ticket_medio()
        #encoding: Algoritmos de Machine Learning e Inteligência Artificial não leem textos, apenas números
        self.df['perfil_medio'] = np.where(self.df['amount'] > ticket_medio, 1, 0)
        return self.df['perfil_medio']

    def exportar_dados_tratados(self, caminho_destino="reports/Amazon_Sales_Clean.csv"):
        try:
            # O index=False impede que o Pandas crie uma coluna extra com os números das linhas
            self.df.to_csv(caminho_destino, index=False)
            return True
        except Exception as e:
            print(f"Erro ao exportar o relatório: {e}")
            return False


