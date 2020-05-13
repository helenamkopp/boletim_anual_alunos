from main import Conta, Cliente

cliente1 = Cliente("Helena", "Kopp", "075.091.024-28")
cliente2 = Cliente("Romulo", "Rosa", "011.087.986-41")

conta1 = Conta("123-4", cliente1, 1000.0)
conta2 = Conta("123-5", cliente2, 1000.0)

conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2, 200.0)
conta1.extrato()

conta1.historico.imprime()
print("----------------")
conta2.historico.imprime()