class Banco: 
    def __init__(self, nome_banco:str, agencia:str, conta:str) -> None:
        self.nome_banco = nome_banco 
        self.agencia = agencia 
        self.conta = conta 
        self._saldo = 0.0
        self.transacao = []

    def __str__(self)-> str:
        return f'Dados:\nnome banco: {self.nome_banco}\nagencia: {self.agencia}\nconta: {self.conta}\nsaldo: {self._saldo}'

    def cadastrar(self, nova_conta:str)-> str:
        self.conta = nova_conta
        return f'Sua conta foi alterado para {nova_conta}.'
          
    def alterar_agencia(self,nova_agencia:str)-> str:
        self.agencia = nova_agencia
        return f'Sua agência foi alterada para {nova_agencia}.'
        
    def depositar(self, valor:float)-> float:
        if valor <= 0:
            return 'Valor invalido.'
        self._saldo += valor
        self.transacao.append(valor)
        return f'Saldo atualizado: {valor}'
    
    def sacar(self, valor:float)-> float:
        if valor > self._saldo:
            return "Saldo insuficiente"
        self._saldo -= valor
        self.transacao.append(-valor)
        return f'Valor sacado: {valor}, saldo atualizado {self._saldo}'
        
class Pessoa(): 
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome 
        self.idade = idade

    def __str__(self):
        return f'Dados:\nnome: {self.nome}\nidade: {self.idade}'
    

    
