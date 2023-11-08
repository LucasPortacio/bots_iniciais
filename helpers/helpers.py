
import datetime as dt
import os


# Definindo a função data com base no D-1
# Formato de Data americano
def Data(Delta):

    data = dt.datetime.today() - dt.timedelta(days=Delta)
    formato_data = data.strftime('%Y-%m-%d')
    return (formato_data)


# Remover espaços em branco dos valores em todas as células.
# Aplicar a todos os elementos do DataFrame:
def remove_whitespace(Value):

    if isinstance(Value, str):  # Verifique se o valor é uma string
        return Value.strip()
    return Value


# Listar arquivos de um diretório específico
# selecionar aquele que estão na data selecionado

def lista_diretorio(diretorio, prefixo, extensao, Data_ok):

    diretorio_base_ativa = os.listdir(diretorio)

# Selecionar somente a base ativa do dia
# Base_ativa_dia é para cada arquivo que estiver no diretorio_base_ativa
# Se o arquivo começar com o prefixo_base e a Data_ok estiver no arquivo
    base_ativa_dia = [arquivo for arquivo in diretorio_base_ativa if
                      arquivo.startswith(prefixo) and Data_ok in arquivo and
                      arquivo.endswith(extensao)]

    for arquivo in base_ativa_dia:
        return arquivo


# Listar arquivos de um diretório específico
# selecionar aquele que estão na data selecionado

def lista_diretorio_range(diretorio, prefixo, extensao, Data_ini, Data_fim):

    diretorio_base_ativa = os.listdir(diretorio)

    arquivos_para_leitura = []

    for arquivo in diretorio_base_ativa:
        if arquivo.startswith(prefixo):
            # Extraia a data do nome do arquivo
            # (assumindo que a data está em uma posição específica)
            data_arquivo = arquivo[len(prefixo):len(prefixo) + len(Data_ini)]

            # Verifique se a data do arquivo está dentro do intervalo desejado
            if Data_ini <= data_arquivo <= Data_fim:
                caminho_completo = os.path.join(diretorio, arquivo)
                arquivos_para_leitura.append(caminho_completo)
    return arquivos_para_leitura
