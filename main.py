import json
from completude import Autor,Publicacao

def jsonReader(file):
    with open (file, 'r') as f:
        dados = json.load(f)
    return dados

fileJson = 'extrato_fiocruz.json'

dadosJson = jsonReader(fileJson)

publicacoes = []

for publicacao in dadosJson:
    titulo = publicacao.get('title')
    dataPublicacao = publicacao.get('publicationDate')
    idioma = publicacao.get('language')

    autoresJson = publicacao.get('authors', [])
    autores = []

    for autorJson in autoresJson:
        nome = autorJson.get('name')
        lattes = autorJson.get('identifier.lattes')
        orcid = autorJson.get('identifier.orcid')
        nacionalidade = autorJson.get('nationality')
        nascPais = autorJson.get('birthCountry')
        nascCidade = autorJson.get('birthCity')
        nascEstado = autorJson.get('birthState')

        autor = Autor(nome, lattes, orcid, nacionalidade, nascPais, nascCidade, nascEstado)
        autores.append(autor)
    
    publicacao_objeto = Publicacao(titulo, dataPublicacao, idioma, autores)
    publicacoes.append(publicacao_objeto)

for publicacao in publicacoes:
    print("Título: ", publicacao.title)
    print("Data de Publicação: ", publicacao.publicationDate)
    print("Idioma: ", publicacao.language)

    print("Autores:\n")
    for autor in publicacao.autores:
        print("Nome do Autor: ", autor.name)
        print("Lattes do Autor: ", autor.lattes)
        print("Orcid do Autor: ", autor.orcid)
        print("Nacionalidade do Autor: ", autor.nationality)
        print("Pais de Origem do Autor: ", autor.birthCountry)
        print("Cidade de Origem do Autor: ", autor.birthCity)
        print("Estado de Origem do Autor: ", autor.birthState)
        print("------")

    print("-----------------------------")