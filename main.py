import os
#from PIL import ImageGrab

#Verificando se a pasta existe e criá-la se não existir.
nome_pasta = "prints"
caminho_pasta = os.path.join(os.getcwd(), nome_pasta)

if not os.path.exists(caminho_pasta):
    os.makedirs(caminho_pasta)

#Verificando se o arquivo notepad existe e criá-lo se não existir.
nome_arquivo = "anotações.txt"
caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

if not os.path.exists(caminho_arquivo):
    print(f"O arquivo '{nome_arquivo}' não existe. Criando o notepad...")
    with open(caminho_arquivo, "w") as arquivo:
        pass
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
else:
    print(f"O arquivo '{nome_arquivo}' já existe.")

#Perguntando ao usuário o que ele deseja escrever e escrever isso no notepad.
texto = input("O que você deseja escrever no notepad? ")
with open(caminho_arquivo, "a") as arquivo:
    arquivo.write(texto + "\n")
print(f"Texto adicionado com sucesso no arquivo '{nome_arquivo}'.")

#Abrindo o arquivo com o aplicativo padrão
#os.system(f"start {caminho_arquivo}")

'''
contador = 1
nome_arquivoscreen = f"screenshot_{contador}.jpg"
caminho_screenshot = os.path.join(caminho_pasta, nome_arquivoscreen)

screenshot = ImageGrab.grab()
screenshot.save(caminho_screenshot)
print(f"Screenshot {nome_arquivoscreen} salvo em {caminho_screenshot}")
'''
