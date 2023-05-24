import unittest
from completude import completude_registro, Publicacao, Autor, completude_registro_or_exclusivo, \
    completude_registro_or_inclusivo, completude_registro_atomico
from parameterized import parameterized_class


@parameterized_class([
    {"publicacao": Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                              [Autor('Paulo', 'lattes1', '', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo')])
        , "expected": True},
    {"publicacao": Publicacao('titulo2', 'data de publicacao2', 'linguagem2',
                              [Autor('Paulo2', 'lattes2', '', 'nationalitysssspaulo2', 'birthCountryssspaulo2',
                                     'birthCityssspaulo2',
                                     'birthStatesssspaulo2')])
        , "expected": True},
    {"publicacao": Publicacao('titulo3', 'data de publicacao3', 'linguagem3',
                              [Autor('Paulo3', 'lattes3', 'orcidsss3', 'nationalitysssspaulo3', 'birthCountryssspaulo3',
                                     'birthCityssspaulo3',
                                     'birthStatesssspaulo3')])
        , "expected": False}

])
class CompletudeTestCase(unittest.TestCase):
    # Toda publicação em porcentagem
    def test_completude_registro(self):
        self.assertEqual(completude_registro(self), 1.0)

    # Espera-se um booleano sobre registros completos e incompletos
    def test_completude_registro_or_exclusivo(self):
        publicacao1 = Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                                 [Autor('Paulo', 'lattes1', 'orcidssspaulo', 'nationalitysssspaulo',
                                        'birthCountryssspaulo',
                                        'birthCityssspaulo', 'birthStatesssspaulo')]
                                 )
        self.assertFalse(completude_registro_or_exclusivo(publicacao1))

    # Espera-se um booleano sobre registros completos e incompletos
    def test_completude_registro_or_exclusivo_duplicado(self):
        publicacao2 = Publicacao('titulo2', 'data de publicacao2', 'linguagem2',
                                 [Autor('Jão', '', 'orcidsssJão', 'nationalityssssJão', 'birthCountrysssJão',
                                        'birthCitysssJão', 'birthStatessssJão')]
                                 )

        self.assertTrue(completude_registro_or_exclusivo(publicacao2))

    # Espera-se um booleano sobre os registros complestos e incompletos
    def test_completude_registro_or_exclusivo_triangulado(self):
        self.assertEqual(completude_registro_or_exclusivo(self.publicacao), self.expected)

    # Espera-se um booleano sobre os registros complestos e incompletos
    def test_completude_registro_or_inclusivo(self):
        publicacao1 = Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                                 [Autor('Paulo', 'lattes1', 'orcidssspaulo', 'nationalitysssspaulo',
                                        'birthCountryssspaulo', 'birthCityssspaulo', 'birthStatesssspaulo')]
                                 )
        self.assertTrue(completude_registro_or_inclusivo(publicacao1))

    def test_completude_registro_atomico(self):
        publicacao1 = Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                                 [Autor('Paulo', 'lattes1', 'orcidssspaulo', 'nationalitysssspaulo',
                                        'birthCountryssspaulo', 'birthCityssspaulo', 'birthStatesssspaulo')]
                                 )
        self.assertEqual(completude_registro_atomico(publicacao1), 1.0)