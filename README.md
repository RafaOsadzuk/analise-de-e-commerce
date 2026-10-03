# 🛒 Amazon E-commerce Data Analysis

Este projeto consiste em uma pipeline de tratamento, limpeza e análise de uma base de dados real de vendas da Amazon, extraída do Kaggle. O foco do desenvolvimento é a aplicação de **Programação Orientada a Objetos (POO)** em Python, estruturando o código de forma modular, escalável e alinhada com as melhores práticas de Engenharia de Dados.

## 🚀 Tecnologias e Bibliotecas
* **Python**
* **Pandas:** Manipulação, limpeza e transformação do DataFrame.
* **NumPy:** Vetorização e operações condicionais de alta performance.

## ⚙️ Funcionalidades Implementadas
Através da classe `ProcessadorAmazon`, o projeto realiza de forma automatizada:
* **Padronização de Schema:** Conversão de cabeçalhos para `lower_case` e formatação de strings.
* **Tipagem de Dados:** Conversão de colunas temporais utilizando `pd.to_datetime()`.
* **Tratamento de Valores Nulos (NaN):** 
  * Isolamento inteligente de dados ausentes por regras de negócio (ex: mapeamento de pedidos cancelados atrelados à ausência de valor financeiro).
  * Limpeza de registros inconsistentes (ex: ausência de cidade/estado de destino).
* **Limpeza de Strings:** Padronização de valores categóricos (`status`, `category`, `fulfilment`) com métodos encadeados (`.str.lower()`, `.str.strip()`, `.str.replace()`).

## 📂 Estrutura do Projeto

```text
├── analysis/         # Notebooks e explorações isoladas
├── data/             # Dados brutos e classes de processamento
│   ├── Amazon_Sales.csv (ignorado no git)
│   └── Dados.py      # Contém a classe ProcessadorAmazon
├── models/           # Modelagens e regras de negócio futuras
├── reports/          # Geração de saídas e relatórios
├── .gitignore        # Proteção de arquivos sensíveis e bases locais
└── main.py           # Ponto de entrada e execução principal do projeto
