#Alguns testes

import unittest
from main import Conta, Cliente, Historico


class TestFuncionalidades(unittest.TestCase):

    def setUp(self):
        self.cliente1 = Cliente("Maria", "Silva", "047.985.412-95")
        self.cliente2 = Cliente("Joana", "Santos", "411.985.365-74")

        self.conta1 = Conta("147-9", self.cliente1, "4500.45")
        self.conta2 = Conta("179-6", self.cliente2, "5850.65", "2000")

    def tearDown(self):
        pass

    def test_deposita(self):
        self.conta1.deposita(45)
        self.conta2.deposita(100)

        self.assertEqual(self.conta1.extrato(), 4545.45)
        self.assertEqual(self.conta2.extrato(), 5950.65)

    def test_valid_client_raising_(self):
        client = Cliente("any client", "any surname", "nany_number")
        account = Conta(1, client, "2",2)
        self.assertTrue(True)

    def test_saca(self):
        self.conta1.saca(100)
        self.conta2.saca(20)

        self.assertEqual(self.conta1.extrato(), 4400.45)
        self.assertEqual(self.conta2.extrato(), 5830.65)

    def test_transfere_para(self):
        self.conta1.transfere_para(self.conta2, 200)

        self.assertEqual(self.conta1.extrato(), 4300.45)
        self.assertEqual(self.conta2.extrato(), 6050.65)






if __name__ == "__main__":
    unittest.main()