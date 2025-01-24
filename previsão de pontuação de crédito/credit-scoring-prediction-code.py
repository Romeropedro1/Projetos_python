# Passo 1: Importar a base de dados;
# Passo 2: Preparar a base de dados;
# Passo 3: Treinar o modelo de IA -> Criar modelo "Nota de crédito";
# Passo 4: Escolher qual o modelor projeto (Modelo);
# Passo 5: Usar o melhor modelo para a previsão.  

# Passo 1: Importar a base de dados utilizando a biblioteca pandas. 
# Apelidada como "pd". E instalar a biblioteca scikit-learn, utilizada para treinamentos de modelos de Inteligência Artificial. 
# Importar a biblioteca pandas com o apelido de "pd" e ler o arquivo "Aula03 - clientes.csv" e armazenar na variável "Tabela".
#!pip install scikit-learn pandas
import pandas as pd
Tabela = pd.read_csv("Aula03 - clientes.csv")   

# Exibir a tabela de dados.
print(Tabela)

# Passo 2: Preparar a base de dados: 
# Itens do tipo (int, float e object) são respectivamente inteiros, flutuantes(números reais) e objetos (texto).
# Exibir informações sobre a tabela de dados.
print(Tabela.info())

# Comando abaixo serve para excluir a coluna "id_cliente" da base de dados.
# Possibilitando assim uma base de dados melhor preparada para treinar o modelo de IA em específico deste projeto. 
Tabela = Tabela.drop(columns = "id_cliente")

# Exibir informações sobre a tabela de dados agora sem a coluna "id_cliente".
print(Tabela.info())

# Próximo passo de tratamento de dados será transformar as colunas do tipo object (texto) em float (flutuante/real).
# No processo de aprendizado, uma IA (inteligência artificial) não consegue aprender com colunas. 
# Colunas Profissão/ Mix_credito/ Comportamento_pagamento serão codificadas em valores numéricos utilizando o "label_encoder". 

# Cada item em valor texto terá um novo valor numérico atribuido pelo processo de "Label_encoder".
# Por exemplo a coluna "Profissão" que contém os seguintes valores: 
# Cientista -> 1
# Bombeiro -> 2
# Engenheiro -> 3
# Dentista -> 4
# Mecânico -> 5
# Artista -> 6

# Importar a biblioteca scikit-learn com o apelido de "sk".
import sklearn as sk
# Importar a biblioteca sklearn e importar a função LabelEncoder que atribui um valor a uma coluna de texto. 
# Importar a função LabelEncoder com o apelido de "LE".
from sklearn.preprocessing import LabelEncoder as LE

# Atribuir a função LabelEncoder() como LE() as variáveis "codificador_profissao", "codificador_mixcredito" e "codificador_pagamento".
codificador_profissao = LE()
codificador_mixcredito = LE()
codificador_pagamento = LE()

# As colunas que devem ser convertidas receberam a função do LabelEncoder() as LE()
# A coluna "profissao" da tabela de dados recebe a função do LabelEncoder() as LE() e a função fit_transform() que transforma a coluna de texto em números.
Tabela["profissao"] = codificador_profissao.fit_transform(Tabela["profissao"])

# Comando acima e comandos abaixo significam que o NOVO valor da coluna profissão da nossa tabela é = a o VELHO valor da coluna profissão, porém agora codificada(transformada em codificador). 
# A coluna "mix_credito" da tabela de dados recebe a função do LabelEncoder() as LE() e a função fit_transform() que transforma a coluna de texto em números.

Tabela["mix_credito"] = codificador_mixcredito.fit_transform(Tabela["mix_credito"]) 
# A coluna "comportamento_pagamento" da tabela de dados recebe a função do LabelEncoder() as LE() e a função fit_transform() que transforma a coluna de texto em números.
Tabela["comportamento_pagamento"] = codificador_pagamento.fit_transform(Tabela["comportamento_pagamento"])

# Exibir informações sobre a tabela de dados agora com as colunas "profissao", "mix_credito" e "comportamento_pagamento" convertidas em números. (int)
print(Tabela.info())

# Nota-se agora visualizando a tabela com o comando "display(Tabela.info())" que os valores texto (object) foram codificados, ou, convertidos para valores numéricos(int64).

# Separar dados treinamento/teste (train/test):
# 1° Etapa:
# Coluna que quero prever = "Y"
# Colunas utilizadas para realizar a previsão = "X"
# 2° Etapa: Separação dos dados deverá ocorrer como a seguir: 
# X de treino + Y de treino (Colunas utilizadas para prever e coluna prevista)
# X de teste + Y de teste
# SE coluna que quero prever = "Y" ENTÃO:

# A variável "Y" recebe a coluna "score_credito" da tabela de dados.
Y = Tabela["score_credito"]

# SE coluna que será utilizada para prever = "X" ENTÃO:
# Quero utilizar minha tabela inteira MENOS a coluna "Score_credito", que já foi utilizada como quem eu quero prever ->
# A variável "X" recebe a tabela de dados sem a coluna "score_credito".
X = Tabela.drop(columns = "score_credito")

# Separar dados já com os valores que serão UTILIZADOS em train/test
from sklearn.model_selection import train_test_split 
# Importar a função train_test_split da biblioteca scikit-learn.

X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size = 0.28)
# Esta é uma ordem padrão a se seguir utilizando a função train_test_split (x, x, y, y) - (X_treino, X_teste, Y_treino, Y_teste).
# A função train_test_split divide a base de dados em duas partes, uma para treino e outra para teste.
# A função train_test_split divide a base de dados em 4 partes, X_treino, X_teste, Y_treino e Y_teste.
# A função train_test_split divide a base de dados em 4 partes, X_treino, X_teste, Y_treino e Y_teste, sendo que 28% da base de dados será utilizada para teste.

# Passo 3: Treinar o modelo de IA -> Criar modelo "Nota de crédito": 
# Importar a IA 
# Criar a IA
# Treinar a IA

# Agora iremos importar o modelo de IA a ser utilizado para o treinamento. 
# Importar o modelo de IA RandomForestClassifier e KNeighborsClassifier da biblioteca scikit-learn.
# importar a IA: 
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

# Atribuir o modelo de IA RandomForestClassifier a variável "modelo_arvoredecisao" e o modelo de IA KNeighborsClassifier a variável "modelo_knn".
# Criar a IA
modelo_arvoredecisao = RandomForestClassifier()
modelo_knn = KNeighborsClassifier()

# Treinar o modelo de IA RandomForestClassifier com a função fit() utilizando as variáveis X_treino e Y_treino.
# Treinar o modelo de IA KNeighborsClassifier com a função fit() utilizando as variáveis X_treino e Y_treino.
# A FUNÇÃO fit() é utilizada para treinar o modelo de IA.
# Treinar a IA
modelo_arvoredecisao.fit(X_treino, Y_treino)
modelo_knn.fit(X_treino, Y_treino)

# Passo 4: Escolher qual o melhor projeto (Modelo):
previsao_arvoredecisao = modelo_arvoredecisao.predict(X_teste)  
previsao_knn = modelo_knn.predict(X_teste)

# A variável "previsao_arvoredecisao" recebe a função predict() do modelo de IA RandomForestClassifier utilizando a variável X_teste.
# A variável "previsao_knn" recebe a função predict() do modelo de IA KNeighborsClassifier utilizando a variável X_teste.
# A função PREDICT() é utilizada para prever o resultado do modelo de IA e ela utiliza apenas a variavel X e não a Y porque ela é a variável que queremos prever.

# Calcular a acurácia dos modelos de IA
# Importar a função accuracy_score da biblioteca scikit-learn.
from sklearn.metrics import accuracy_score

print(accuracy_score(Y_teste, previsao_arvoredecisao))    
print(accuracy_score(Y_teste, previsao_knn))

# Exibir a acurácia do modelo de IA RandomForestClassifier utilizando a função accuracy_score() com as variáveis Y_teste e previsao_arvoredecisao.
# Exibir a acurácia do modelo de IA KNeighborsClassifier utilizando a função accuracy_score() com as variáveis Y_teste e previsao_knn.
# A função accuracy_score() é utilizada para calcular a acurácia do modelo de IA.
# A acurácia é a porcentagem de acertos do modelo de IA.
# Quanto mais próximo de 1, melhor é o modelo de IA.
# Quanto mais próximo de 0, pior é o modelo de IA.
# A acurácia é um dos indicadores de qualidade do modelo de IA.

# Passo 5: Importar novos clientes para análise:

# A partir do modelo agora treinado, quero utilizá-lo para prever o score de crédito de um novo cliente.
# 1° Importar os novos clientes:
Tabela_novos_clientes = pd.read_csv("Aula03 - novos_clientes.csv")

# Importar a tabela de dados "Aula03 - novos_clientes.csv" e armazenar na variável "Tabela_novos_clientes".
# Exibir a tabela de dados "Tabela_novos_clientes".
print(Tabela_novos_clientes)
Tabela_novos_clientes["profissao"] = codificador_profissao.transform(Tabela_novos_clientes["profissao"])
# Comando acima e comandos abaixo significam que o NOVO valor da coluna profissão da nossa tabela nova é = a o VELHO valor da coluna profissão, porém agora codificada(transformada com o codificador). 
# A coluna "profissao" da tabela de dados "Tabela_novos_clientes" recebe a função do LabelEncoder() as LE() e a função transform() que transforma a coluna de texto em números.
Tabela_novos_clientes["mix_credito"] = codificador_mixcredito.transform(Tabela_novos_clientes["mix_credito"]) 
# A coluna "mix_credito" da tabela de dados "Tabela_novos_clientes" recebe a função do LabelEncoder() as LE() e a função transform() que transforma a coluna de texto em números.
Tabela_novos_clientes["comportamento_pagamento"] = codificador_pagamento.transform(Tabela_novos_clientes["comportamento_pagamento"])
# A coluna "comportamento_pagamento" da tabela de dados "Tabela_novos_clientes" recebe a função do LabelEncoder() as LE() e a função transform() que transforma a coluna de texto em números.
print(Tabela_novos_clientes)

# Exibir a tabela de dados "Tabela_novos_clientes" agora com as colunas "profissao", "mix_credito" e "comportamento_pagamento" convertidas em números. (int)
print(Tabela_novos_clientes)

# Exibir a tabela de dados "Tabela_novos_clientes" agora com as colunas "profissao", "mix_credito" e "comportamento_pagamento" convertidas em números. (int)
nova_previsao = modelo_arvoredecisao.predict(Tabela_novos_clientes) 
print(nova_previsao)

# A variável "nova_previsao" recebe a função predict() do modelo de IA RandomForestClassifier utilizando a variável Tabela_novos_clientes.
# A função predict() é utilizada para prever o resultado do modelo de IA.
# A variável "nova_previsao" é a previsão do score de crédito dos novos clientes.
# Exibir a previsão do score de crédito dos novos clientes.


