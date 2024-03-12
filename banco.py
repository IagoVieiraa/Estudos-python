class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def ver_saldo(self):
        msg = f'O saldo atual é: {self.saldo}'
        return msg

    def depositar(self, valor, codigo_da_conta):
         if codigo_da_conta == 1:
             self.saldo += valor
             print(f'Operação de depósito realizada com sucesso! O novo saldo da conta é {self.saldo}')
             return
         else:
            return 'Código da conta incorreto'
        


    def sacar(self, valor):
        self.saldo -= valor
        print(f'O saque foi realizado com sucesso! O novo saldo da conta é {self.saldo}')
        


if __name__ == '__main__':
    c1 = Conta(1, 'Iago')
    c2 = Conta(2, 'Alessandra')  

