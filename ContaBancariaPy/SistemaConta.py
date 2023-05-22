class Conta:
    def __init__(self, numConta, saldo, nomeTitular, limite, tipo, status=False):
        self.numConta = numConta
        self.saldo = saldo
        self.nomeTitular = nomeTitular
        self.limite = limite
        self.tipo = tipo
        self.status = status


    def deposito(self):

        if self.status == False:
            print("Ative sua conta para realizar transações")
        else:
            dep = int(input("Digite o valor do deposito"))
            saldofinal = (self.saldo + dep)
            return saldofinal

    def sacar(self, saque):
        if self.status == False:
            print("Ative sua conta para realizar transações")
        else:
            if saque > self.limite:
                print(f'saque nao pode exceder o limite de {self.limite}')
            else:
                saldoFinal = self.saldo - saque
                return saldoFinal

    def ativarConta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada!")

    def verSaldo(self):
        print(f' seu saldo é {self.saldo}')



conta1 = Conta("1453222","0.00","Joao Marques","3.500","Corrente")

conta1.sacar(300)
conta1.ativarConta()
conta1.verSaldo()
conta1.deposito()
conta1.verSaldo()
conta1.sacar(500)