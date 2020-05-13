import unittest
from main import Conta, Cliente, Historico


class TestCliente(unittest.TestCase):
    cliente1 = Cliente("Maria", "Silva", "077.091.024-28")
    cliente2 = Cliente("João", "Santos", "011.088.986-41")

    def test_nome(self):
        self.assertEqual(self.cliente1.nome, "Maria")
        self.assertEqual(self.cliente2.nome, "João")

    def test_sobrenome(self):
        self.assertEqual(self.cliente1.sobrenome, "Silva")
        self.assertEqual(self.cliente2.sobrenome, "Santos")

    def test_cpf(self):
        self.assertEqual(self.cliente1.cpf, "077.091.024-28")
        self.assertEqual(self.cliente2.cpf, "011.088.986-41")
