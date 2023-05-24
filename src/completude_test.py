import unittest
from completude import completude_registro, Autor, Publicacao
from parameterized import parameterized_class


@parameterized_class([
    {"publicacao": Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                              [Autor('Paulo', '', 'orcidssspaulo', 'nationalitysssspaulo', 'birthCountryssspaulo', 'birthCityssspaulo',
                                    'birthStatesssspaulo'),
                              Autor('João', '', 'orcidsssJoão', 'nationalityssssJoão', 'birthCountrysssJoão', 'birthCitysssJoão',
                                     'birthStatessssJoão'),
                              Autor('Ian', '', 'orcidsssIan', 'nationalityssssIan', 'birthCountrysssIan', 'birthCitysssIan',
                                    'birthStatessssIan')]
                              ), "expected": 1.0},
    {"publicacao": Publicacao('titulo2', 'data de publicacao2', 'linguagem2',
                               [Autor('Paulo2', '', 'orcidssspaulo2', 'nationalitysssspaulo2', 'birthCountryssspaulo2',
                                      'birthCityssspaulo2',
                                      'birthStatesssspaulo2'),
                                Autor('João2', '', 'orcidsssJoão2', 'nationalityssssJoão2', 'birthCountrysssJoão',
                                      'birthCitysssJoão',
                                      'birthStatessssJoão'),
                                Autor('Ian2', '', 'orcidsssIan2', 'nationalityssssIan', 'birthCountrysssIan',
                                      'birthCitysssIan',
                                      'birthStatessssIan')]
                               ), "expected": 1.0}

])


class CompletudeTestCase(unittest.TestCase):
    def test_completude_registro(self):
        # Falsificação: Criar um cenário em que o campo está completo
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
