import pandas as pd

class TratativasAmazon:

    def __init__(self, caminho):
        self.caminho = caminho
        self.df = None
        self.df_pedidos_cancelados = None

    def carregar_dados(self):
        try:
            self.df = pd.read_csv(self.caminho)
            print("arquivo carregado")
            return self.df
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None

    def transformar_dados(self):

        if self.df is None:
            print("Erro: Carregue os dados antes de transformá-los.")
            return None

        try:
            self.df.columns = self.df.columns.str.lower().str.strip().str.replace(' ', '_').str.replace('-', '_')
            self.df['category'] = self.df['category'].str.strip().str.title()
            self.df['fulfilment'] = self.df['fulfilment'].str.lower().str.strip().str.replace('merchant', 'vendedor')
            self.df['date'] = pd.to_datetime(self.df['date'], dayfirst=True)


            if self.df['amount'].isnull().any():
                self.df_pedidos_cancelados = self.df[self.df['amount'].isnull()]
                self.df = self.df.dropna(subset=['amount'])

            if self.df[['ship_city', 'ship_state', 'ship_postal_code' ]].isnull().any().any():
               self.df = self.df.dropna(subset=['ship_city', 'ship_postal_code', 'ship_state'])

            return self.df

        except Exception as e:
            print(f"Erro ao transformar dados: {e}")
            return None

