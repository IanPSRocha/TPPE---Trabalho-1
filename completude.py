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
    if campo or campo != '':
        return True
    return False

def completude_registro(self):
    porcentagem_atomica = completude_registro_atomico(self)
    porcentagem_or_exclusivo = completude_registro_or_exclusivo(self)
    porcentagem_or_inclusivo = completude_registro_or_inclusivo(self)
    porcentagem_total = ((porcentagem_atomica + porcentagem_or_exclusivo + porcentagem_or_inclusivo) / 3 ) * 100

    return round(porcentagem_total, 2)

def completude_registro_or_exclusivo(self):
    """Função para calcular a completude de um registro OR Exclusivo
       Retorna a quantidade de registros completos e incompletos"""
    exclusivo_completo = []
    exclusivo_incompleto = []
    # Verificar completude dos campos aninhados OR exclusivo
    for i in range(len(self.autores)):
        if self.autores[i].lattes is None:
            self.autores[i].lattes = ''
        if self.autores[i].orcid is None:
            self.autores[i].orcid = ''
        if completude_campo(self.autores[i].lattes) != completude_campo(self.autores[i].orcid):
            exclusivo_completo.append(self.autores[i])
        else:
            exclusivo_incompleto.append(self.autores[i])

    return len(exclusivo_completo) / len(exclusivo_completo + exclusivo_incompleto)


def completude_registro_or_inclusivo(self):
    """Função para calcular a completude de um registro OR Inclusivo
       Retorna a quantidade de registros completos e incompletos"""

    inclusivo_completo = []
    inclusivo_incompleto = []
    # Verificar completude dos campos aninhados OR inclusivo
    for i in range(len(self.autores)):
        if self.autores[i].nationality is None:
            self.autores[i].nationality = ''
        if self.autores[i].birthCountry is None:
            self.autores[i].birthCountry = ''
        if self.autores[i].birthCity is None:
            self.autores[i].birthCity = ''
        if self.autores[i].birthState is None:
            self.autores[i].birthState = ''
        if ((completude_campo(self.autores[i].nationality)) or (
        completude_campo(self.autores[i].birthCountry))
                or (completude_campo(self.autores[i].birthCity) or (
                completude_campo(self.autores[i].birthState)))):
            inclusivo_completo.append(self.autores[i])
        else:
            inclusivo_incompleto.append(self.autores[i])

    return len(inclusivo_completo) / len(inclusivo_completo + inclusivo_incompleto)

def completude_registro_atomico(self):
    """Função para calcular a completude de um registro atômico       
    Retorna a quantidade de registros completos e incompletos"""    

    # Verificar completude dos campos atômicos    atomico_completo = []
    atomico_incompleto = []
    atomico_completo = []
    campos_atomicos = [self.title, self.publicationDate, self.language]

    for campo in campos_atomicos:
        if completude_campo(campo):
            atomico_completo.append(campo)
        else:
            atomico_incompleto.append(campo)
    
    return len(atomico_completo) / len(atomico_incompleto + atomico_completo)