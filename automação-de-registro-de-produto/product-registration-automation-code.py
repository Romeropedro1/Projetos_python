import pandas as pd  # Renomeando pandas para pd, é uma convenção mais comum
import pyautogui
import time

# Configurações iniciais do pyautogui
pyautogui.PAUSE = 1  # Intervalo de 1 segundo entre cada comando do pyautogui

# Passo 1: Abrir o sistema da empresa
pyautogui.press("Win")  # Pressiona a tecla Windows (Menu Iniciar)
pyautogui.write("edge")  # Digita "edge" para abrir o Microsoft Edge
pyautogui.press("enter")  # Pressiona Enter para abrir o navegador
time.sleep(3)  # Espera 3 segundos para o navegador carregar

# Passo 2: Fazer login no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # Digita o link de login
pyautogui.press("enter")  # Pressiona Enter para acessar o site
time.sleep(2)  # Aguarda 2 segundos para a página carregar

# Preencher os campos de login
pyautogui.click(x=525, y=403)  # Clica no campo de email (ajuste as coordenadas conforme necessário)
pyautogui.write("pythonimpressionador@gmail.com")  # Digita o e-mail
pyautogui.press("tab")  # Move para o campo de senha
pyautogui.write("Sua senha")  # Digita a senha (substitua pela senha real)
pyautogui.press("enter")  # Pressiona Enter para fazer o login
time.sleep(3)  # Aguarda 3 segundos para o sistema carregar

# Passo 3: Importar a base de dados dos produtos
Tabela = pd.read_csv("Produtos.csv")  # Lê o arquivo CSV com os dados dos produtos
print(Tabela)  # Exibe a tabela para verificar se os dados foram carregados corretamente

time.sleep(2)  # Aguarda 2 segundos para garantir que o sistema esteja pronto para os cadastros

# Passo 4: Cadastrar os produtos
for linha in Tabela.index:
    # Clicar no campo de código do produto
    pyautogui.click(x=511, y=282)  # Ajuste as coordenadas conforme necessário

    # Preencher os campos do formulário
    codigo = Tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))  # Preenche o campo "código"
    pyautogui.press("tab")  # Move para o próximo campo

    marca = Tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))  # Preenche o campo "marca"
    pyautogui.press("tab")  # Move para o próximo campo

    tipo = Tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))  # Preenche o campo "tipo"
    pyautogui.press("tab")  # Move para o próximo campo

    categoria = Tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))  # Preenche o campo "categoria"
    pyautogui.press("tab")  # Move para o próximo campo

    preco_unitario = Tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))  # Preenche o campo "preço unitário"
    pyautogui.press("tab")  # Move para o próximo campo

    custo = Tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))  # Preenche o campo "custo"
    pyautogui.press("tab")  # Move para o próximo campo

    obs = str(Tabela.loc[linha, "obs"])
    if obs != "nan":  # Verifica se o campo "obs" não está vazio (NaN)
        pyautogui.write(obs)  # Preenche o campo "observações"
    pyautogui.press("tab")  # Move para o próximo campo

    # Enviar o formulário
    pyautogui.press("enter")  # Envia o formulário
    pyautogui.scroll(10000)  # Rola a página para cima (para visualizar o próximo cadastro)
    time.sleep(1)  # Espera 1 segundo antes de cadastrar o próximo produto

print("Cadastro de produtos concluído com sucesso!")

# Fechar o navegador após concluir o processo
pyautogui.hotkey('alt', 'f4')  # Fecha o navegador (ajuste se necessário)
