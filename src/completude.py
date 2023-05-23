class Autor:
    def __init__(self, name, lattes, orcid, nationality, birthCountry, birthCity, birthState):
        self.name = name
        self.lattes = lattes
        self.orcid = orcid
        self.nationality = nationality
        self.birthCountry = birthCountry
        self.birthCity = birthCity
        self.birthState = birthState

class Publicacao:
    def __init__(self, title, publicationDate, language, autores):
        self.title = title
        self.publicationDate = publicationDate
        self.language = language
        self.autores = autores

def completude_campo(campo):
    # Verificar completude do campo
    if campo:
        return True
    return False

def completude_registro(publicacao):
    # Verificar completude dos campos atômicos
    atomico_completo = []
    atomico_incompleto = []
    campos_atomicos = [publicacao.title, publicacao.publicationDate, publicacao.language]
    
    for campo in campos_atomicos:
        if completude_campo(campo):
            atomico_completo.append(campo)
        else:
            atomico_incompleto.append(campo)    
            

    # Verificar completude dos campos aninhados OR exclusivo
    or_exclusivo_completo = []
    or_exclusivo_incompleto = []
    for autor in publicacao.autores:
        if completude_campo(publicacao.autores[autor].lattes) != completude_campo(publicacao.autores[autor].orcid):
            or_exclusivo_completo.append(autor)
        else:
            or_exclusivo_incompleto.append(autor)    

    # Verificar completude dos campos aninhados OR inclusivo
    or_inclusivo_completo = []
    or_inclusivo_incompleto = []

    for autor in publicacao.autores:
        if ((completude_campo(publicacao.autores[autor].nationality)) or (completude_campo(publicacao.autores[autor].birthCountry))
        or (completude_campo(publicacao.autores[autor].birthCity) or (completude_campo(publicacao.autores[autor].birthState)))):
            or_exclusivo_completo.append(autor)
        else:
            or_exclusivo_incompleto.append(autor)    

    campos_completos = atomico_completo + or_exclusivo_completo + or_inclusivo_completo
    campos_incompletos = atomico_incompleto + or_exclusivo_incompleto + or_inclusivo_incompleto
    
    porcentagem_completude = len(campos_completos) / len(campos_completos + campos_incompletos)

    return porcentagem_completude

