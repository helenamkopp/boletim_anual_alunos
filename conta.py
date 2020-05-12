class Conta():

    def __init__(self, numero, titular, saldo, limite):
        conta = {"número": numero, "titular": titular, "saldo": saldo, "limite": limite}
        return

    def deposita(self, conta, valor):
        conta["saldo"] += valor

    def sacar(self, conta, valor):
        conta["saldo"] -= valor

    def extrato(self, conta):
        print(f"numero: {[c]]} \nsaldo: {[conta[} ")





