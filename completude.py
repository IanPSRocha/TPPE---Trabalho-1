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




