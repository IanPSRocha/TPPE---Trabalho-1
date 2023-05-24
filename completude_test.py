import unittest
from completude import completude_registro


class CompletudeTestCase(unittest.TestCase):
    def test_completude_registro_falsificado(self):
        # Falsificação: criação de testes com resultados esperados falsificados,
        # ou seja, onde os resultados esperados são definidos previamente,
        # mesmo que a implementação ainda não tenha sido feita.
        self.assertEqual(completude_registro(self), 1.0)

    def test_completude_registro_or_exclusivo_falsificado(self):
        # Falsificação: criação de testes com resultados esperados falsificados,
        # ou seja, onde os resultados esperados são definidos previamente,
        # mesmo que a implementação ainda não tenha sido feita.
        self.assertEqual(completude_registro(self), 1.0)

