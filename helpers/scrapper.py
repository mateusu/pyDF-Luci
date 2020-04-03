from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import json

scholar_url = "https://scholar.google.com.br/scholar?"

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


def getArtigos(keywords, page):
    artigos = []
    url = scholar_url + "start=" + page + "&q=" + quote(keywords.replace(" ", "+")) + "&hl=pt-BR"
    opener = AppURLopener()
    response = opener.open(url)
    res = BeautifulSoup(response, features="html.parser")
    lista = res.findAll(class_="gs_r gs_or gs_scl")

    for l in lista:
        sibling = lista[0].div
        sibling = sibling.next_sibling
        titulo = sibling.h3
        autor = titulo.next_sibling
        descricao = autor.next_sibling

        artigos.append({"titulo": titulo.get_text(), "autor": autor.get_text(), "descricao": descricao.get_text()})
        
    return artigos

getArtigos("maçã e", "0")