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


def completude_registro(self):
    return 1.0


def completude_registro_or_exclusivo(self):
    return 1.0




