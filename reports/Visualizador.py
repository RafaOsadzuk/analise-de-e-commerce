import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class VisualizadorAmazon:
    def __init__(self, df_limpo):
        self.df = df_limpo
        sns.set_theme(style="whitegrid")

    def plotar_faturamento_mensal(self):
        self.df['date'] = pd.to_datetime(self.df['date'])

        faturamento = self.df.groupby(self.df['date'].dt.to_period('M'))['amount'].sum().reset_index()

        faturamento['date'] = faturamento['date'].astype(str)

        sns.barplot(data=faturamento, x='date', y='amount', hue='date')

        plt.title("Faturamento Mensal da Amazon (INR)", fontsize=14, pad=15)
        plt.xlabel("Mês", fontsize=12)
        plt.ylabel("Receita Total (Milhões)", fontsize=12)
        plt.tight_layout()
        plt.show()

    def plotar_categorias(self):
        top_categorias = self.df['category'].value_counts().head(10).reset_index()

        sns.barplot(data=top_categorias, x='count', y='category', hue='category')

        plt.title("Categorias de Amazon", fontsize=14, pad=15)
        plt.xlabel("Volume de Pedidos", fontsize=12)
        plt.ylabel("Categoria", fontsize=12)
        plt.tight_layout()
        plt.show()