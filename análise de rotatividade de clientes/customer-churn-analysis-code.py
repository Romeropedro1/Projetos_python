# Passo 1: Importar a base de dados;
# Passo 2: Visualizar a base de dados (Identificar problemas e entender a base de dados);
# Passo 3: Corrigir os problemas da base de dados;
# Passo 4: Análise inicial -> Quantos clientes cancelaram e qual a % de clientes que cancelaram;
# Passo 5: Análise da CAUSA do cancelamento.
# Extensão JUPYTER, arquivo formato Ipynb
# Passo 1, Importar a base de dados:

#pip install nbformat>=4.2.0 ipykernel plotly pandas numpy openpyxl
# Comando acima instala biblitecas mais utilizadas em Python ^^

# Importa a biblioteca pandas utilizada para leitura da tabela(cancelamentos.csv).
import pandas as pd 
# Comando realiza a leitura da tabela(cancelamentos.csv).
pd.read_csv("cancelamentos_sample.csv")
# Atribui o valor dentro da tabela(cancelamentos.csv) para dentro de uma variável chamada "Tabela".
Tabela = pd.read_csv("cancelamentos_sample.csv")

# Passo 2, Visualizar a base de dados: 

# Utilize o comando PRINT ou DISPLAY (Válido apenas na extensão.ipynb) para exibir a tabela. 
# Recomendo comando display.
print(Tabela)

# Passo 3, Corrigir os problemas das bases de dados:

# Comando exclui a coluna "CustomerID" que se mostra ineficiente para o treinamento que iremos realizar.
Tabela = Tabela.drop(columns=["CustomerID"])

# Comando exibe informações da tabela.
# Comando mostra todas as colunas e também linhas ocupadas e vazias dentro da Tabela.
# Além das linhas, espaços e colunas vazias, este comando também mostra o type (tipo) de item em cada coluna. Object, float64 e int64 são os tipos mais comuns.
print(Tabela.info())

# Variável Tabela agora contém o valor da antiga tabela porém SEM os espaços vazios encontrados a partir da análise do display(Tabela.info())
# Comando exclui todas as linhas que possuem valores vazios. (DROPA)
Tabela = Tabela.dropna()

# Comando mostra todas as colunas e também linhas ocupadas e vazias dentro da Tabela.
# Além das linhas, espaços e colunas vazias, este comando também mostra o type (tipo) de item em cada coluna. Object, float64 e int64 são os tipos mais comuns.
print(Tabela.info())

# Passo 4, Análise inicial dos dados: Quantos clientes cancelaram e qual a % de cancelamento:

# Comando mostra a quantidade de valores que a coluna "cancelou" possui.
Tabela["cancelou"].value_counts()

# Comando mostra a quantidade de valores que a coluna "cancelou" possui, porém, em porcentagem. %%
(Tabela["cancelou"].value_counts(normalize=True))

# Passo 5, Análise da CAUSA de cancelamento dos clientes: 

# Comparar colunas COM a coluna de cancelamentos para entender qual ou o que causa mais impacto nos cancelamentos.
# Comando abaixo instala a biblioteca Plotly, que será utilizada para a criação de gráficos.
#!pip install plotly


# Importar a biblioteca "Plotly" para geração e visualização de gráficos
# Nbformat é uma biblioteca que permite a leitura e escrita de notebooks Jupyter. Que são arquivos .ipynb.
import plotly.express as px
import nbformat

# Comando cria um gráfico de histograma, onde o eixo X é a duração do contrato e o eixo Y é a quantidade de cancelamentos.
Grafico = px.histogram(Tabela, x = "duracao_contrato", color = "cancelou")

# Comando cria um loop que percorre todas as colunas da Tabela e cria um gráfico de histograma para cada uma delas.
# Comando text_auto = True, mostra a quantidade de cancelamentos em cada barra do gráfico.
# Comando Grafifo.show(renderer="notebook") exibe o gráfico na extensão .ipynb.
for coluna in Tabela.columns:
    Grafico = px.histogram(Tabela, x = coluna, color = "cancelou", text_auto = True)    
    Grafico.show(renderer="browser")


# 1° Insight: Todos os clientes do plano mensal cancelaram. 
# 2° Todos os clientes a partir de 50 anos cancelaram.
# 3° Maior taxa de cancelamento do público feminino do que no público masculino.
# 4° Todos os clientes que ligaram no call_center mais de 4 vezes cancelaram. 

# 5° Uusuários que atrasaram o pagamento por mais de 20 dias cancelaram.
# PROBLEMAS A RESOLVER: 
# Duração_contrato -> Precisa ser diferente de mensal; != "Monthly"
# Ligações_callcenter -> Precisa ser menor que 4; < 4
# Atraso_pagamento -> Precisa ser menor que 20 dias. < 20

Tabela = Tabela[Tabela["duracao_contrato"] != "Monthly"]
(Tabela["cancelou"].value_counts())

# Duração_contrato -> Precisa ser diferente de mensal; != "Monthly"

# OBS: Este é o resultado que pode ser alcançado resolvendo a taxa de cancelamento dos planos "mensais". 

Tabela = Tabela[Tabela["ligacoes_callcenter"] < 4]
(Tabela["cancelou"].value_counts())

# Ligações_callcenter -> Precisa ser menor que 4; < 4


# OBS: Este é o resultado que pode ser alcançado resolvendo a taxa de cancelamento dos clientes que tomaram esta atitude após mais que 4 ligações no CallCenter da empresa. 

Tabela = Tabela[Tabela["dias_atraso"] < 20]
(Tabela["cancelou"].value_counts())
# OBS: Este é o resultado que pode ser alcançado resolvendo a taxa de cancelamento dos clientes que atrasaram o pagamento em mais de 20 dias. 


print(Tabela["cancelou"].value_counts(normalize=True))

# Este é o resultado final, após a limpeza e organização dos dados e resolução dos problemas encontrados a partir dos insights.
