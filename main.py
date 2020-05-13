import datetime

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"Data abertura: {self.data_abertura}")
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)

class Conta:

    def __init__(self, numero, cliente, saldo, limite=1000.0):
        if not isinstance(cliente, Cliente):
            raise TypeError("cliente must be of type Client not {}".format(type(cliente)))
        self.titular = cliente
        self.numero = str(numero)
        self.saldo = float(saldo)
        self.limite = float(limite)
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Deposito de R$ {valor}")

    def saca(self, valor):
        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de R$ {valor}")

    def extrato(self):
        print(f"numero {self.numero} \nsaldo {self.saldo}")
        self.historico.transacoes.append(f"Tirou extrato - saldo de: R$ {self.saldo}")
        return self.saldo

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"Transferencia de R$ {valor} para conta {destino.numero}")
            return True


