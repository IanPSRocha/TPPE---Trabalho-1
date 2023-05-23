import unittest
from completude import completude_campo, completude_registro

class CompletudeTestCase(unittest.TestCase):
    def test_completude_campo(self):
        # Falsificação: Criar um cenário em que o campo está completo
        campo_completo = "Campo completo"
        self.assertTrue(completude_campo(campo_completo))

        # Duplicação: Criar um cenário em que o campo está duplicado
        campo_duplicado = "Campo duplicado"
        self.assertTrue(completude_campo(campo_duplicado))

        # Triangulação: Criar um cenário em que o campo está incompleto
        campo_incompleto = None
        self.assertFalse(completude_campo(campo_incompleto))

    def test_completude_registro(self):
        # Falsificação: Criar um cenário em que o registro está completo
        publicacao_completa = {
            'title': 'Título',
            'publicationDate': '2022-01-01',
            'language': 'Português',
            'autores': [
                {
                    'name': 'Autor 1',
                    'lattes': '123456',
                    'orcid': '',
                    'nationality': '',
                    'birthCountry': '',
                    'birthCity': '',
                    'birthState': ''
                },
                {
                    'name': 'Autor 2',
                    'lattes': '',
                    'orcid': 'abcdef',
                    'nationality': '',
                    'birthCountry': '',
                    'birthCity': '',
                    'birthState': ''
                }
            ]
        }

        self.assertEqual(completude_registro(publicacao_completa), 1.0)

        # Duplicação: Criar um cenário em que um campo do registro está duplicado
        publicacao_duplicada = {
            'title': 'Título duplicado',
            'publicationDate': '2022-02-02',
            'language': 'Inglês',
            'autores': [
                {
                    'name': 'Autor 3',
                    'lattes': '123456',
                    'orcid': '123456',
                    'nationality': '',
                    'birthCountry': '',
                    'birthCity': '',
                    'birthState': ''
                }
            ]
        }

        self.assertEqual(completude_registro(publicacao_duplicada), 1.0)

        # Triangulação: Criar um cenário em que o registro está incompleto
        publicacao_incompleta = {
            'title': '',
            'publicationDate': '',
            'language': '',
            'autores': [
                {
                    'name': 'Autor 4',
                    'lattes': '',
                    'orcid': '',
                    'nationality': '',
                    'birthCountry': '',
                    'birthCity': '',
                    'birthState': ''
                }
            ]
        }

        self.assertEqual(completude_registro(publicacao_incompleta), 0.0)

if __name__ == '__main__':
    unittest.main()
