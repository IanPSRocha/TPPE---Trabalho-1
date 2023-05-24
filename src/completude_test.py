import unittest
from completude import completude_registro, Autor, Publicacao
from parameterized import parameterized, parameterized_class


@parameterized_class([
    {"publicacao": Publicacao('titulo', 'data de publicacao', 'linguagem',
                              Autor('Paulo', '', 'orcidsss', 'nationalityssss', 'birthCountrysss', 'birthCitysss',
                                    'birthStatessss')), "expected": 1.0}
])
class CompletudeTestCase(unittest.TestCase):
    def test_completude_registro(self):
        # Falsificação: Criar um cenário em que o campo está completo
        # autor1 = Autor(title, publicationDate, language)
        # autor2 = Autor('Jão', 'late2', '', 'nationalitysss2', 'birthCountryssss2', 'birthCityssss2', 'birthStatesss2')
        # autores = [autor1, autor2]
        # publicacao = Publicacao('titulo', 'data de publicacao', 'linguagem', autores)
        print(completude_registro(self))
        self.assertEqual(completude_registro(self), 1.0)

        # # Duplicação: Criar um cenário em que o campo está duplicado
        # campo_duplicado = "Campo duplicado"
        # self.assertTrue(completude_campo(campo_duplicado))
        #
        # # Triangulação: Criar um cenário em que o campo está incompleto
        # campo_incompleto = None
        # self.assertFalse(completude_campo(campo_incompleto))

    # def test_completude_registro(self):
    #     # Falsificação: Criar um cenário em que o registro está completo
    #     publicacao_completa = {
    #         'title': 'Título',
    #         'publicationDate': '2022-01-01',
    #         'language': 'Português',
    #         'autores': [
    #             {
    #                 'name': 'Autor 1',
    #                 'lattes': '123456',
    #                 'orcid': '',
    #                 'nationality': '',
    #                 'birthCountry': '',
    #                 'birthCity': '',
    #                 'birthState': ''
    #             },
    #             {
    #                 'name': 'Autor 2',
    #                 'lattes': '',
    #                 'orcid': 'abcdef',
    #                 'nationality': '',
    #                 'birthCountry': '',
    #                 'birthCity': '',
    #                 'birthState': ''
    #             }
    #         ]
    #     }
    #
    #     self.assertEqual(completude_registro(publicacao_completa), 1.0)
    #
    #     # Duplicação: Criar um cenário em que um campo do registro está duplicado
    #     publicacao_duplicada = {
    #         'title': 'Título duplicado',
    #         'publicationDate': '2022-02-02',
    #         'language': 'Inglês',
    #         'autores': [
    #             {
    #                 'name': 'Autor 3',
    #                 'lattes': '123456',
    #                 'orcid': '123456',
    #                 'nationality': '',
    #                 'birthCountry': '',
    #                 'birthCity': '',
    #                 'birthState': ''
    #             }
    #         ]
    #     }
    #
    #     self.assertEqual(completude_registro(publicacao_duplicada), 1.0)
    #
    #     # Triangulação: Criar um cenário em que o registro está incompleto
    #     publicacao_incompleta = {
    #         'title': '',
    #         'publicationDate': '',
    #         'language': '',
    #         'autores': [
    #             {
    #                 'name': 'Autor 4',
    #                 'lattes': '',
    #                 'orcid': '',
    #                 'nationality': '',
    #                 'birthCountry': '',
    #                 'birthCity': '',
    #                 'birthState': ''
    #             }
    #         ]
    #     }
    #
    #     self.assertEqual(completude_registro(publicacao_incompleta), 0.0)

if __name__ == '__main__':
    unittest.main()
