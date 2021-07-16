from zipfile import ZipFile
import os
import shutil

dict = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", 
        "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}

def manga_livre(arquivo_nome):
    with ZipFile(f"{arquivo_nome}", 'r') as zipObj:
        zipObj.extractall()
        zipObj.close()
        os.remove(arquivo_nome)
            
    nome_manga = ""
    for palavra in arquivo_nome.split("-"):
        if palavra.isdigit():
            break
        else:
            palavra = palavra.replace("_", "")
            if palavra in lista_cap:
                break
            else:
                nome_manga += f" {palavra}"

    for word in arquivo_nome.split("_"):
        word = word.replace("-", "")
        if word.isdigit():
            capitulo = word
    pasta_final = f"Capitulo {capitulo} {nome_manga}"
            
    os.rename("content", pasta_final)
    pasta = os.listdir(pasta_final)
    num_prov = 0

    for imagem in pasta:
        num_pag = ""
        if len(imagem) < 5:
            for letra in imagem:
                
                if letra in dict:
                    num_pag += dict[letra]
        num_pag = imagem
                    
        os.rename(f"{pasta_final}/{imagem}", f"{pasta_final}/Pagina {num_pag} de {len(pasta)}.png") 

def siteGringo(arquivo_nome):
    capitulo = arquivo_nome.replace(".zip", "")
    capitulo = f"Capitulo {capitulo} None"
    os.mkdir(capitulo)
    shutil.move(arquivo_nome, capitulo)
    with ZipFile(f"{capitulo}/{arquivo_nome}", 'r') as zipObj:
        zipObj.extractall(capitulo)
        zipObj.close()
        os.remove(f"{capitulo}/{arquivo_nome}")
    
    pasta = os.listdir(capitulo)
    
    numero_paginas = len(pasta)
    for imagem in pasta:    
        if imagem.endswith(".png"):
            imagem_final = imagem.replace(".png", "")
        elif imagem.endswith(".jpg"):
            imagem_final = imagem.replace(".jpg", "")
            
        os.rename(f"{capitulo}/{imagem}", f"{capitulo}/Pagina {imagem_final} de {numero_paginas}.png") 

lista_cap = []
for i in range(0, 1500):
    lista_cap.append(str(i))
mangas = os.listdir()

for arquivo_nome in mangas:
    if arquivo_nome.endswith(".zip"):
        if len(arquivo_nome) > 9:
            manga_livre(arquivo_nome)
        else:
            siteGringo(arquivo_nome)
    else:
        pass