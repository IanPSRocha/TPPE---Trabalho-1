import unittest
from completude import Publicacao, Autor, completude_registro_or_exclusivo, \
    completude_registro_or_inclusivo, completude_registro_atomico, completude_registro
from parameterized import parameterized_class


@parameterized_class([
    {"publicacao": Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                              [Autor('Paulo', '', 'dadsdsaads', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo'),
                                Autor('Paulo', 'lattes1', '', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo')])
        , "expected": 1.0},
    {"publicacao": Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                              [Autor('Paulo', '', 'dadsdsaads', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo'),
                                Autor('Paulo', 'lattes1', 'orcid', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo')])
        , "expected": 0.5},
    {"publicacao": Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                              [Autor('Paulo', 'lattes1', 'dadsdsaads', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo'),
                                Autor('Paulo', '', '', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                     'birthCityssspaulo',
                                     'birthStatesssspaulo')])
        , "expected": 0.0},

])
class CompletudeTestCase(unittest.TestCase):
    #Toda publicação em porcentagem
    def test_completude_registro(self):
        self.assertEqual(completude_registro(self), 1.0)

    #Espera-se um booleano sobre registros completos e incompletos
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
        self.assertEqual(completude_registro_or_inclusivo(publicacao1), 1.0)

    def test_completude_registro_atomico(self):
        publicacao1 = Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                                 [Autor('Paulo', 'lattes1', 'orcidssspaulo', 'nationalitysssspaulo',
                                        'birthCountryssspaulo', 'birthCityssspaulo', 'birthStatesssspaulo')]
                                 )
        self.assertEqual(completude_registro_atomico(publicacao1), 1.0)