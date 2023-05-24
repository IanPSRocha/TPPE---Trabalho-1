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
    return 1.0


def completude_registro_or_exclusivo(self):
    """Função para calcular a completude de um registro OR Exclusivo
       Retorna a quantidade de registros completos e incompletos"""

    # Verificar completude dos campos aninhados OR exclusivo
    for i in range(len(self.autores)):
        if completude_campo(self.autores[i].lattes) != completude_campo(self.autores[i].orcid):
            return True
        else:
            return False


def completude_registro_or_inclusivo(self):
    """Função para calcular a completude de um registro OR Inclusivo
       Retorna a quantidade de registros completos e incompletos"""

    # Verificar completude dos campos aninhados OR inclusivo
    for autor in range(len(self.autores)):
        if ((completude_campo(self.autores[autor].nationality)) or (
        completude_campo(self.autores[autor].birthCountry))
                or (completude_campo(self.autores[autor].birthCity) or (
                completude_campo(self.autores[autor].birthState)))):
            return True
        else:
            return False

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