# conta_bancaria_v1

Pequeno projeto Orientado a Objetos construído com o PyCharm de funcionalidades de uma conta bancária. 

Arquivo main.py:
- class Cliente: possui método construtor e é dedicada exclusivamente aos dados do cliente (nome, sobrenome, cpf);

- class Historico: possui método construtor o qual declara o momento de abertura de uma conta (usando a biblioteca datetime) e guarda as 
transações em uma lista, criando assim um pequeno histórico bancário; o método imprime tem um laço para organizar cada transação;

- class Conta: possui método construtor exclusiva aos dados da conta bancaria, já declara o limite fixo, e herda os dados da classe cliente
para o titular; os demais métodos são de funcionalidades de uma conta como: saque, extrato, transferencia e depósito. 

Arquivo test_main.py:
realiza alguns testes unitários referentes ao arquivo main.py 


