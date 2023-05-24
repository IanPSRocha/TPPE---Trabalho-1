import unittest
from completude import completude_registro, Publicacao, Autor, completude_registro_or_exclusivo


class CompletudeTestCase(unittest.TestCase):
    #Toda publicação em porcentagem
    def test_completude_registro(self):
        self.assertEqual(completude_registro(self), 1.0)


    #Espera-se um booleano sobre registros completos e incompletos
    def test_completude_registro_or_exclusivo(self):
        publicacao1 = Publicacao('titulo1', 'data de publicacao1', 'linguagem1',
                                [Autor('Paulo', 'lattes1', 'orcidssspaulo', 'nationalitysssspaulo', 'birthCountryssspaulo',
                                'birthCityssspaulo','birthStatesssspaulo')]
                                )
        self.assertFalse(completude_registro_or_exclusivo(publicacao1))


    #Espera-se um booleano sobre registros completos e incompletos
    def test_completude_registro_or_exclusivo_duplicado(self):
        publicacao2 = Publicacao('titulo2', 'data de publicacao2', 'linguagem2',
                                 [Autor('Jão', '', 'orcidsssJão', 'nationalityssssJão', 'birthCountrysssJão',
                                        'birthCitysssJão', 'birthStatessssJão')]
                                 )

        self.assertTrue(completude_registro_or_exclusivo(publicacao2))