from zipfile import ZipFile
import os
import shutil

dict = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": 
        "5", "6": "6", "7": "7", "8": "8", "9": "9"}

def mangaLivre(arquivoNome):
    with ZipFile(f"{arquivoNome}", 'r') as zipObj:
        zipObj.extractall()
        zipObj.close()
        os.remove(arquivoNome)
            
    nomeManga = ""
    for palavra in arquivoNome.split("-"):
        if palavra.isdigit():
            break
        else:
            palavra = palavra.replace("_", "")
            if palavra in listaCap:
                break
            else:
                nomeManga += f" {palavra}"

    for word in arquivoNome.split("_"):
        word = word.replace("-", "")
        if word.isdigit():
            capitulo = word
    pastaFinal = f"Capitulo {capitulo} {nomeManga}"
            
    os.rename("content", pastaFinal)
    pasta = os.listdir(pastaFinal)
    numProv = 0

    for imagem in pasta:
        numPag = ""
        if len(imagem) < 5:
            for letra in imagem:
                
                if letra in dict:
                    numPag += dict[letra]
        numPag = imagem
                    
        os.rename(f"{pastaFinal}/{imagem}", f"{pastaFinal}/Pagina {numPag} de {len(pasta)}.png") 

def siteGringo(arquivoNome):
    capitulo = arquivoNome.replace(".zip", "")
    capitulo = f"Capitulo {capitulo} None"
    os.mkdir(capitulo)
    shutil.move(arquivoNome, capitulo)
    with ZipFile(f"{capitulo}/{arquivoNome}", 'r') as zipObj:
        zipObj.extractall(capitulo)
        zipObj.close()
        os.remove(f"{capitulo}/{arquivoNome}")
    
    pasta = os.listdir(capitulo)
    
    numeroPaginas = len(pasta)
    for imagem in pasta:    
        if imagem.endswith(".png"):
            imagemFinal = imagem.replace(".png", "")
        elif imagem.endswith(".jpg"):
            imagemFinal = imagem.replace(".jpg", "")
            
        os.rename(f"{capitulo}/{imagem}", f"{capitulo}/Pagina {imagemFinal} de {numeroPaginas}.png") 

listaCap = []
for i in range(0, 1500):
    listaCap.append(str(i))
mangas = os.listdir()

for arquivoNome in mangas:
    if arquivoNome.endswith(".zip"):
        if len(arquivoNome) > 9:
            mangaLivre(arquivoNome)
        else:
            siteGringo(arquivoNome)
    else:
        pass
    
'''
Isso é um teste
'''